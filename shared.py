from pathlib import Path
import shutil


def prepare_raw_dir(raw_dir_path: Path):
    if raw_dir_path.exists():
        shutil.rmtree(raw_dir_path.absolute())
    raw_dir_path.mkdir(parents=True)


def validate_and_get_path(raw_path):
    path = Path(raw_path)
    if not path.exists():
        raise ValueError("Directory does not exists!")
    return path


def iterdir(path: Path):
    for file in path.iterdir():
        yield file
