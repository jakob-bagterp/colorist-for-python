# MkDocs Documentation 📚
The documentation template and build pipeline is based on [MkDocs](https://www.mkdocs.org), and this directory contains the source files for building the documentation.

## Configuration
Find the MkDocs configuration in the `mkdocs.yml` file in the root of the project.

## Dependencies
Overview of the dependencies:

* Build tool: [MkDocs](https://www.mkdocs.org/)
* Theme: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
* Plugins: Various [theme extensions](https://squidfunk.github.io/mkdocs-material/extensions/) and [mkdocstrings](https://mkdocstrings.github.io) for source code documentation

You can find all the dependencies in the `/docs/requirements.txt` file. How to install them from the root of the project:

```bash
pip install -r ./docs/requirements.txt
```

## Build Pipeline
All build steps and documentation testing are automated using [GitHub Actions](https://github.com/features/actions).

You can find the workflow files in the `/.github/workflows` directory. For example:

* `test_docs.yml`
* `docs.yml`
* etc.

## Useful Commands
### Build
Basic build command:

```bash
mkdocs build
```

For more verbose output and stricter checks, use the following command:

```bash
mkdocs build --strict --verbose
```

### Local Development and Previewing
To preview the documentation hosted on a local machine, use the following command:

```bash
mkdocs serve
```

### Troubleshooting
If you're running a virtual environment with [`venv`](https://docs.python.org/3/library/venv.html) (e.g. created with the command `python3 -m venv .venv`), sometimes the  MkDocs dependencies break for unknown reasons.

After activating the virtual environment with the `source .venv/bin/activate` command, try using the following commands instead:

```bash
python3 -m mkdocs build
python3 -m mkdocs serve
```

Or trying executing the commands with a specific version of Python:

```bash
python3.11 -m mkdocs build
python3.11 -m mkdocs serve
```
