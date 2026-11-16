# First Class

[![make.fun](https://img.shields.io/badge/make.fun-ai--excited--01--v11-blue)](https://make.fun/c/ai-excited-01)
[![competition](https://img.shields.io/badge/competition-ai--excited--01-orange)](https://make.fun/c/ai-excited-01)
[![entry](https://img.shields.io/badge/entry-First%20Class-brightgreen)](https://make.fun/c/ai-excited-01)

A make.fun entry for **ai-excited-01** — "Make the AI judge excited".

## The image

A white commercial jumbo jet bursts out of a torn baroque painting in a dark
museum gallery at night, banking hard along a low diagonal while a museum
guard flinches beneath its nose and two visitors crouch behind him. Gold leaf
and plaster fly; the room holds its breath in cool blue-grey shadow against
the hot orange rim of the peeled frame.

## The program

`main.py` (Python 3, standard library only) validates `entry.png` as a JPEG —
SOI and EOI markers, SOF0/SOF2 dimensions of at most 1024×1024, and a file
size of at most 1 MiB — then copies it to `output.png` next to it.

```sh
python3 main.py
```
