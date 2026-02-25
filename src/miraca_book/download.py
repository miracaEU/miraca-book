import requests
from tqdm import tqdm
from pathlib import Path
import logging
import shutil

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
    # Zenodo URLs have '?download=1' at the end, for cleaner filenames we remove it
    download_file = miraca_folder / url.split('/')[-1].replace('?download=1', '')
    local_file = download_file.parent / download_file.name.replace('.zip', '')
    if local_file.exists():
        logging.info(f'{local_file} already exists. Not downloading again.')
        return local_file

    response = requests.get(url, stream=True)
    
    with tqdm(
        unit='iB',
        unit_scale=True,
        total=int(response.headers.get("content-length", 0)),
    ) as progress_bar, download_file.open("wb") as fout:
        for chunk in response.iter_content(chunk_size=4096):
            fout.write(chunk)
            progress_bar.update(len(chunk))

    if download_file.suffix == '.zip':
        shutil.unpack_archive(download_file, local_file)
        download_file.unlink()

    return local_file
