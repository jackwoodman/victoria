from pathlib import Path
from typing import List

from file_parsing.cli_tooling import read_filepath


def get_filepaths_from_folder(
    target_directory: Path, target_file_extension: str
) -> List[Path]:
    target_file_extension = "tcx"
    filepaths = [file for file in target_directory.glob(f"*.{target_file_extension}")]

    return filepaths


def get_target_filepaths_from_cli() -> List[Path]:
    target_path = Path(read_filepath())
    target_extension = ".tcx"

    if target_path.is_dir():
        return get_filepaths_from_folder(
            target_directory=target_path, target_file_extension=target_extension
        )
    else:
        if target_path.is_file() and target_path.suffix == target_extension:
            return [target_path]
        else:
            return []
