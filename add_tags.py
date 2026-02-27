import nbformat as nbf
from argparse import ArgumentParser
from pathlib import Path


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--path",
        type=Path,
        help="Path to the notebooks.",
        default=Path("./miraca-book/"),
    )
    return parser.parse_args()


# Text to look for in adding tags
text_search_dict = {
    "# HIDDEN": "remove-cell",  # Remove the whole cell
    "# NO CODE": "remove-input",  # Remove only the input
    "# HIDE CODE": "hide-input",  # Hide the input w/ a button to show
}


def add_tags_to_notebook(path):
    ntbk = nbf.read(path, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        cell_tags = cell.get("metadata", {}).get("tags", [])
        for key, val in text_search_dict.items():
            if key in cell["source"]:
                if val not in cell_tags:
                    cell_tags.append(val)
        if len(cell_tags) > 0:
            cell["metadata"]["tags"] = cell_tags

    nbf.write(ntbk, path)


if __name__ == "__main__":
    args = parse_args()
<<<<<<< HEAD
    notebooks = args.path.rglob("*.ipynb")
=======
    notebooks = args.path.rglob("**/*.ipynb")
>>>>>>> 348d0873714231051cd577e27af98b4809a9d1f0
    # Search through each notebook and look for the text, add a tag if necessary
    for nb in notebooks:
        print(nb)
        add_tags_to_notebook(nb)
