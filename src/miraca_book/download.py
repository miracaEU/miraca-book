import requests
from tqdm import tqdm
from pathlib import Path

def download(url: str):
    """Download a file with progress from a URL and save it to the local .miraca folder.

    Parameters
    ----------
    url : str
        A valid URL pointing to the file to be downloaded.

    Returns
    -------
    out : Path
        The local path where the downloaded file is saved.
    """
    miraca_folder = Path('~/.miraca').expanduser()
    miraca_folder.mkdir(parents=True, exist_ok=True)
    local_file = miraca_folder / url.split('/')[-1]
    response = requests.get(url, stream=True)

    with tqdm.wrapattr(
        local_file.open("wb"),
        "write",
        miniters=1,
        total=int(response.headers.get("content-length", 0)),
    ) as fout:
        for chunk in response.iter_content(chunk_size=4096):
            fout.write(chunk)
    
    return local_file
