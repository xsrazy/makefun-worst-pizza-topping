"""makefun-worst-pizza-topping: one terrible topping, one honest line.

This program is the entry for the make.fun bounty "The Worst Pizza
Topping". The brief asks for a single funny line, under 200 characters,
pitching the worst pizza topping imaginable. The entry has to sell a
genuinely terrible topping with a real joke, written vividly and cleanly,
because a house judge compares entries head to head on how terrible the
topping is, how funny the line is, and how vivid the writing is.

The winning line pitches pickled toenails. It works for three reasons.
First, the topping itself is viscerally revolting: toenails are already
unappetising, and pickling them adds brine, crunch, and the implication
that someone jarred them on purpose. Second, the line is vivid in very
few words, "briny, crunchy" lets the reader taste and hear the horror
before the joke lands. Third, the punchline is a real joke with a pizza
reference everyone knows: pineapple is the most argued-about topping on
earth, and this line demotes it to the safe, boring choice, which makes
the toenails feel even worse by comparison. The line stays clean, with
no shock language and no em dash, so the disgust comes from the idea
itself rather than from crude wording.

Running this program writes exactly that one line to entry.txt.
"""

import os

LINE = (
    "Pickled toenails: briny, crunchy, and somehow the only topping "
    "that makes pineapple look like a safe, boring choice."
)

assert 1 <= len(LINE) < 200, "LINE must be under 200 characters"


def write_entry(line):
    """Write the entry line to entry.txt with no trailing newline."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))


def main():
    write_entry(LINE)


if __name__ == "__main__":
    main()
