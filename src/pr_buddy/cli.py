"""Command-line entry point for pr-buddy."""  # a docstring: describes the file
import argparse  # standard library module for reading command-line options
import sys       # gives access to sys.exit (the program's exit code)

from pr_buddy import __version__  # the version from __init__.py (you'll use it in step 7)


def build_parser() -> argparse.ArgumentParser:   # "-> X" is a type hint: this function returns X
    parser = argparse.ArgumentParser(
        prog="pr-buddy",                          # the name shown in help and errors
        description="Review GitHub pull requests with an LLM.",
    )
    # Subcommands, like git's "git commit" / "git push". Ours: "pr-buddy hello".
    subcommands = parser.add_subparsers(dest="command", required=True)
    # dest="command": the chosen subcommand's name is stored in args.command
    # required=True: running plain "pr-buddy" is an error
    subcommands.add_parser("hello", help="check that pr-buddy is installed")
    return parser


def main(argv: list[str] | None = None) -> int:
    # argv=None means "read the real command line". Tests (step 3) pass a list instead.
    parser = build_parser()
    args = parser.parse_args(argv)   # reads the options; on bad input prints an error and exits 2
    if args.command == "hello":
        print("Hello, world! pr-buddy is ready.")
    return 0                         # 0 = success, exactly like exit codes in Bash


if __name__ == "__main__":           # true only when you run this file directly
    sys.exit(main())                 # turn main()'s return value into the exit code