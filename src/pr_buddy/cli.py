"""Command-line entry point for pr-buddy."""  # a docstring: describes the file
import argparse  # standard library module for reading command-line options
import sys       # gives access to sys.exit (the program's exit code)

from pr_buddy import __version__  # the version from __init__.py


def build_parser() -> argparse.ArgumentParser:   # "-> X" is a type hint: this function returns X
    parser = argparse.ArgumentParser(
        prog="pr-buddy",                          # the name shown in help and errors
        description="Review GitHub pull requests with an LLM.",
    )
    parser.add_argument("--version", action="version", version=f"{parser.prog} {__version__}")
    # Subcommands, like git's "git commit" / "git push". Ours: "pr-buddy hello".
    subcommands = parser.add_subparsers(dest="command", required=True)
    # dest="command": the chosen subcommand's name is stored in args.command
    # required=True: running plain "pr-buddy" is an error
    hello = subcommands.add_parser("hello", help="check that pr-buddy is installed")
    hello.add_argument("--name", default="world", help="who to greet")
    return parser


def main(argv: list[str] | None = None) -> int:
    # argv=None means "read the real command line". Tests (step 3) pass a list instead.
    parser = build_parser()
    args = parser.parse_args(argv)   # reads the options; on bad input prints an error and exits 2
    if args.command == "hello":
        print(f"Hello, {args.name}! pr-buddy is ready.")
    return 0                         # 0 = success, exactly like exit codes in Bash


if __name__ == "__main__":           # true only when you run this file directly
    sys.exit(main())                 # turn main()'s return value into the exit code
