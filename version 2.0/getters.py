import json
from typing import Tuple


def getDimensions(config_file: str) -> Tuple[int, int]:
    """
    Returns the dimensions of the grid stored in the config_file.

    Parameters:
            file (str): The file path where the grid representation is stored.

    Returns:
            tuple: The dimensions of the grid.
    """
    with open(config_file, "r") as config_file:
        config = json.load(config_file)
    (n, p) = config["grid"]["default_size"]
    return n, p


def getGridFile(config_file: str) -> str:
    """
    Returns the grid representation stored in the file.

    Parameters:
            file_path (str): The file path where the grid representation is stored.

    Returns:
            str: The grid representation.
    """
    with open(config_file, "r") as config_file:
        config = json.load(config_file)
    file_name = config["grid"]["grid_file"]
    return file_name

def getTitle(config_file: str) -> str:
	"""
	Returns the title of the game stored in the config_file.

	Parameters:
			file (str): The file path where the grid representation is stored.

	Returns:
			str: The title of the game.
	"""
	with open(config_file, "r") as config_file:
		config = json.load(config_file)
	title = config["window"]["title"]
	return title
