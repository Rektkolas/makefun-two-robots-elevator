"""Make.fun entry: Two Robots in an Elevator. Writes /output/entry.txt."""
import os

LINE = "I like your firmware. I mean — that came out wrong. Please don't report me to maintenance."


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        local = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(local), exist_ok=True)
        with open(local, "w", encoding="utf-8") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
