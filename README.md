# pr-buddy

A command-line tool that reviews GitHub pull requests with an LLM and posts the review as a comment.
Learning project, built step by step.

## Install (development)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

```bash
pr-buddy hello
```

## Roadmap

- [x] Project structure and CLI
- [ ] Fetch a pull request from the GitHub API
- [ ] Tests
- [ ] Docker
- [ ] CI with GitHub Actions
- [ ] LLM review
- [ ] Run automatically on pull requests
- [ ] Deploy to Kubernetes
