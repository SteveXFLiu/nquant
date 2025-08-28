# Notes on Quantitative Investments

## Tools
These notes are written with [Quarto](https://quarto.org), and are rendered to PDF by default.

The Python environment is managed with [uv](https://docs.astral.sh/uv/) and is defined in the [pyproject.toml](./pyproject.toml) file. It can be replicated with the command:
```{sh}
uv sync
```
The Python interpreter will be `.venv/bin/python`.

The R environment is installed systematically (e.g. with Homebrew on MacOS). The libraries needed are listed in the file [rlibs](./rlibs).