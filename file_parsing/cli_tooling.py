import argparse
import sys


def read_filepath(
    description: str = "Read path to file or folder with running data.",
) -> str:
    """Read filepath from CLI.


    Returns:
        String representation of the input filepath.

    """
    (arg_parser := argparse.ArgumentParser(prog=description)).add_argument(
        "path", type=str, help="Path to the run data file or folder of run data files."
    )
    filepath = arg_parser.parse_args().path

    return filepath
