# Miraca Book

Jupyter book for the Miraca project

## Building this book

After cloning this repo, you need to initialize the submodule by running:

```bash
git submodule update --init --recursive
```

You can build the pages of the book by running `jupyter-book build miraca-book`. Before consecutive builds, clean the build folder with `jupyter-book clean miraca-book/`. As recommended in the [jupyter-book docs](https://jupyterbook.org/en/stable/start/build.html#aside-source-vs-build-files), the built HTML pages are gitignored on the main branch but can be committed to the `gh-pages` branch by running

```bash
ghp-import -n -p -f miraka-book/_build/html
```

To add custom jupyter-book tags e.g. to toggle code cells run `python add_tags.py`

You can find more on the publishing process in the [Jupyter Book docs](https://jupyterbook.org/en/stable/start/publish.html#publish-your-book-online-with-github-pages).

### Adding and updating submodules

To add a new submodule you can run something like this

```bash
git submodule add <url to repo> <path inside book>
```

For update an already added submodule, simply checkout or pull the commit of interest e.g. the latest main version inside the miraca-book repo and commit the change.

## Funding Note

MIRACA (Multi-hazard Infrastructure Risk Assessment for Climate Adaptation) is a research project building an evidence-based decision support toolkit that meets real world demands.

This project has received funding from the European Union’s Horizon Europe research programme under grant agreement No 101004174.
