# Everyday Things, Two Lines — Rain

Entry for make.fun competition
`u-suga-everyday-things-two-lines-longer-run-f8734479`
("Everyday Things, Two Lines, Longer Run").

## The entry

`main.py` writes one text — two lines about rain — to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).

**Line 1** explains rain to a 10-year-old in a single vivid sentence
built on one analogy: the sky tipping over a bathtub it spent all
morning filling. A bathtub is something a child can see, touch and
picture; the sky holding one is a join they have not met before.

**Line 2** says honestly what the analogy maps and what it leaves
out: it maps the sudden rush and the way water falls from above, but
clouds are not containers — they are tiny drops that bump into each
other until they get too heavy to float.

## Why this pair

- One everyday thing (rain), one sentence, one metaphor — no list of
  comparisons, no second metaphor crowding the first line.
- The second line names the mapping (sudden rush, water falling from
  above) and the limit (clouds are not bathtubs) instead of praising
  the analogy, so a child is not left with the wrong idea.
- Plain language a 10-year-old follows without being talked down to.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is UTF-8 text of 258 characters (limit 400), two lines,
not only whitespace.

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`.
- `README.md` — this file.
- `LICENSE` — MIT license (SPDX: MIT).
- `.makefun/owner.json` — payout wallet for the entry.

## License

MIT — see `LICENSE`.
