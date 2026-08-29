# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal **TIL (Today I Learned)** notes repository, written in Korean. It is content, not an
application: 72 Markdown notes, 24 standalone Python coding-test solutions, and 23 diagram images.
There is **no build system, no package manifest, no test runner, no linter, and no dependencies** —
do not look for or introduce one. "Working on this repo" means writing or editing notes and adding
solution files.

## Commands

There is nothing to build or run. The only executable content is `CodingTest/**/*.py`, and each file
defines a bare `solution(...)` with no `__main__` block, matching the Programmers submission template.
To exercise one:

```bash
python3 -c 'exec(open("CodingTest/Programmers/Lv. 1/추억 점수.py").read()); print(solution(["may","kein"],[5,10],[["may"],["kein"]]))'
```

Every path in this repo contains spaces and/or Korean characters — **always quote paths** in shell
commands, and prefer `find ... -exec sh -c '... "$1"' _ {} \;` over `for f in $(find ...)`, which
word-splits and fails here.

## Structure and where content goes

- `Book/<책 제목>/` — one directory per book. Two layouts coexist; follow whichever the target book
  already uses:
  - Chapters at the book root: `클린 아키텍처/3부 - 설계 원칙.md`, `스위프트 프로그래밍(야곰, 3판)/07. 함수.md`
  - Chapters in a subdirectory: `꼼꼼한 재은 씨의 스위프트 기본편/Chapters/CHAPTER 03.md`
- `RxSwift/Chapters/NN. Title.md` — numbered, English titles.
- `CodingTest/<플랫폼>/…` — currently only `Programmers/Lv. 0/` and `Lv. 1/`. `Baekjoon/` and
  `LeetCode/` exist but are empty. Filename = the Korean problem title, e.g. `옹알이 (1).py`.
- `Interview/` — `CS.md` and `Swift, iOS.md` are empty placeholders awaiting content.

Images live in an `Images/` directory **beside** the notes that use them (`RxSwift/Chapters/Images/`,
`Book/클린 아키텍처/Images/`, `Book/꼼꼼한 재은 씨의 스위프트 기본편/Chapters/Images/`) and are referenced
with a relative path: `![Images/zip.png](Images/zip.png)`.

## The README index chain (easy to forget)

Each level has a README acting as a 목차 (table of contents), and adding a note means updating its
parent:

- Root `README.md` links to each book/section directory.
- `RxSwift/README.md` is a Markdown table: number, emoji + link, and a summary of the operators covered.
- Each book README lists its chapters.

These TOC links are **absolute `https://github.com/lygon55555/til/...` URLs with percent-encoded
Korean and spaces**, not relative paths — match that form when adding an entry. (Note the mixed
`til` / `TIL` casing already present in root `README.md`; GitHub treats it as the same repo.)

Several READMEs are currently empty (`CodingTest/README.md`, `Interview/README.md`, and the two
`꼼꼼한 재은 씨…` book READMEs), as is `RxSwift/Chapters/14. RxCocoa Basics.md`. Empty means
"not written yet", not "deleted".

## Note-writing conventions

- Korean, terse note-taking voice ending in `~함 / ~임 / ~하는 역할` — not polite `~합니다` prose.
- Emphasis is done with inline backticks around the key term (`` `새로운 Observable을 리턴` ``), not bold.
- Two trailing spaces for a soft line break; `<br/>` on its own line to separate sections.
- Code fences are tagged by language (```swift, ```python).
- RxSwift chapters open with an emoji-only `# 👋` line, then `# NN. Title`, then — for operator
  chapters — a table whose entries are anchor links (`[filter](#filter)`) to the sections below.
- Book chapters open with `# CHAPTER 03 – …` or `# 3부 - …` matching that book's numbering scheme,
  and use the book's own section numbering (`## 7.1 함수와 메서드`) for subheadings.
- Python solutions are plain and imperative — no imports, no type hints, no comments, no helper
  functions; build an `answer` variable and return it.

## Commits

History uses short Korean subject lines describing the content added, with no type prefix and no
body: `챕터7 추가`, `Lv. 1 추가`, `Interview 추가`, `폴더 추가`, `코드 수정`. GitHub-web edits appear
as `Update README.md`. Follow the Korean style for consistency with the log.

There is no `.gitignore`; a stray `.DS_Store` sits untracked at the root — leave it out of commits.
