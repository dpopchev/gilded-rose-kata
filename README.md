# devbg2024

Notes and code for my [devbg talk](https://dev.bg/event/python-metaprogramming-or-what-i-should-have-known-from-the-start/).

## Installation

### Requirements

- pandoc
- some tex libs, tbd

### Install

```
git clone --depth 1 https://github.com/dpopchev/devbg2024.git
cd devbg2024
make development
make check
make presentation
```

## Agenda

- Software engineering background: NATO conference 68 and UNIX vs agile
- Test vs Behaviour driven development
- OOP vs FP
- Metaclasses (career development vs reduction)

## Usage

### Live presentation rebuild

While making the presentation I found useful to trigger build of the
presentation on changes under `docs`.

```bash
ls docs/* | entr sh -c 'echo compile: $(date +%H:%M:%S) && make presentation && echo compile: end && pkill -HUP mupdf && echo REFRESHED'
```

## Acknowledgement

- [Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main)

## License

[MIT](LICENSE)
