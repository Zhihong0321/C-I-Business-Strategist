#!/usr/bin/env python3
"""Check that every number and link in an HTML report appears in its markdown extract.

Usage: python -I check_coverage.py <report.html> <extract.md>

Numbers are compared by value (so "1,648,000" matches "1648000" and "5.0" matches "5").
Script lines that are pure chart styling (fonts, sizes, canvas drawing) are skipped.
Anything printed under MISSING is either a real omission or noise to be judged by hand.
"""
import html as htmlmod
import re
import sys

NUM_RE = re.compile(r'(?<![\w.#])[-+−]?\d[\d,]*(?:\.\d+)?')
STYLE_KEYS = (
    'font', 'size:', 'borderwidth', 'tension', 'pointradius', 'pointhoverradius', 'height', 'width',
    'maxtickslimit', 'boxwidth', 'borderradius', 'rotate', 'translate', 'fillrect', 'strokerect',
    'rgba', 'tofixed', 'substr', 'settimeout', 'math.pi', 'linewidth', 'offset', 'moveto', 'lineto',
    'maxrotation', 'fractiondigits', 'slice(', '.length', 'for (', 'idx', 'pxpermeter', 'bessw', 'bessh',
    'gappx', 'wallx', 'liney', 'beginpath', 'filltext', 'clearrect', 'x +=', "'#", '"#', 'pct <',
    'tolocalestring', 'getcontext', 'beginatzero',
)


def values(text):
    out = []
    for m in NUM_RE.finditer(text):
        tok = m.group(0).replace('−', '-').lstrip('+').replace(',', '')
        try:
            out.append((abs(float(tok)), m.group(0), m.start()))
        except ValueError:
            pass
    return out


def split_html(raw):
    raw = re.sub(r'<style.*?</style>', ' ', raw, flags=re.S | re.I)
    raw = re.sub(r'<script[^>]*src=[^>]*>\s*</script>', ' ', raw, flags=re.I)
    raw = re.sub(r'<link[^>]*>', ' ', raw, flags=re.I)
    scripts = []

    def grab(m):
        body = m.group(1)
        if 'tailwind.config' not in body:
            scripts.append(body)
        return ' '
    raw = re.sub(r'<script[^>]*>(.*?)</script>', grab, raw, flags=re.S | re.I)
    comments = ' '.join(re.findall(r'<!--(.*?)-->', raw, flags=re.S))
    raw = re.sub(r'<!--.*?-->', ' ', raw, flags=re.S)
    urls = re.findall(r'href="(https?://[^"]+)"', raw)
    attrs = []
    for tag in re.findall(r'<(?:input|option)\b[^>]*>', raw, flags=re.I):
        for name, val in re.findall(r'\b(value|min|max|step)="([^"]*)"', tag):
            attrs.append(f'{name}={val}')
    text = re.sub(r'<[^>]+>', ' ', raw)
    text = htmlmod.unescape(re.sub(r'\s+', ' ', text))
    script_lines = [ln for s in scripts for ln in s.splitlines()
                    if ln.strip() and not any(k in ln.lower() for k in STYLE_KEYS)]
    return text, '\n'.join(script_lines), comments, ' '.join(attrs), urls


def report(label, source, md_vals, width=40):
    missing = {}
    for val, tok, pos in values(source):
        if val in md_vals:
            continue
        ctx = source[max(0, pos - width): pos + len(tok) + width].replace('\n', ' ')
        missing.setdefault(tok, ctx)
    print(f'\n== {label}: {len(missing)} missing ==')
    for tok, ctx in missing.items():
        print(f'  {tok:>12}  …{ctx.strip()}…')
    return len(missing)


def main():
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    html_path, md_path = sys.argv[1], sys.argv[2]
    raw = open(html_path, encoding='utf-8').read()
    md = open(md_path, encoding='utf-8').read()
    md_vals = {v for v, _, _ in values(md)}
    text, script, comments, attrs, urls = split_html(raw)
    total = 0
    total += report('VISIBLE TEXT', text, md_vals)
    total += report('SCRIPT DATA / LOGIC', script, md_vals)
    total += report('INPUT DEFAULTS (value/min/max/step)', attrs, md_vals)
    total += report('HTML COMMENTS (design notes, low priority)', comments, md_vals)
    missing_urls = [u for u in dict.fromkeys(urls) if u not in md]
    print(f'\n== LINKS: {len(missing_urls)} of {len(set(urls))} missing ==')
    for u in missing_urls:
        print('  ', u)
    print(f'\nTOTAL missing numbers: {total}; missing links: {len(missing_urls)}')


if __name__ == '__main__':
    main()
