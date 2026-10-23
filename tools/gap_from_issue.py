#!/usr/bin/env python3
"""Turn a GitHub "knowledge-gap" issue into gaps/open/<date>-issue-<n>-<slug>.md.

Called by .github/workflows/gap-from-issue.yml with ISSUE_NUMBER, ISSUE_TITLE, ISSUE_BODY, ISSUE_URL.
Skips issues that already have a gap file.
"""
import datetime
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAPS = ROOT / 'gaps'


def field(body, label):
    m = re.search(r'### ' + re.escape(label) + r'\s*\n+(.*?)(?=\n### |\Z)', body, re.S)
    value = m.group(1).strip() if m else ''
    return '' if value == '_No response_' else value


def main():
    number = os.environ['ISSUE_NUMBER']
    title = os.environ.get('ISSUE_TITLE', '').strip()
    body = (os.environ.get('ISSUE_BODY') or '').replace('\r\n', '\n')
    url = os.environ.get('ISSUE_URL', '')

    if any(GAPS.glob(f'*/*-issue-{number}-*.md')):
        print(f'issue #{number} already has a gap file')
        return

    question = field(body, 'Question') or re.sub(r'^gap:\s*', '', title, flags=re.I)
    question = ' '.join(question.split()).replace('"', "'")
    priority = field(body, 'Priority').lower()
    priority = priority if priority in ('high', 'medium', 'low') else 'medium'
    related = field(body, 'Related topics and conflicts').replace('[', '').replace(']', '')
    asked_via = field(body, 'Asked via').replace('"', "'") or 'GitHub issue'
    date = datetime.date.today().isoformat()
    slug = re.sub(r'[^a-z0-9]+', '-', question.lower()).strip('-')[:50] or 'gap'

    text = f'''---
id: GAP-{date}-issue-{number}
question: "{question}"
asked_via: "{asked_via}"
date: {date}
status: open
priority: {priority}
related: [{related}]
source_issue: {url}
---

## Why the repo can't answer it
{field(body, "Why the repo can't answer it")}

## What would answer it
{field(body, 'What would answer it')}

## Interim answer given (unverified)
{field(body, 'Interim answer given (unverified)')}

## Raw GAP block
{field(body, 'Raw GAP block (optional)')}
'''
    path = GAPS / 'open' / f'{date}-issue-{number}-{slug}.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(f'wrote {path.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
