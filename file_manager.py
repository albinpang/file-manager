import os
import shutil
from pathlib import Path
from house_units import Cm06


# --------------------------- File management -----------------------------

def get_destination(file, destination_root, default_case_folder=None):

    """
    Sorts a file based on various parameters and moves it to a specified destination.
    
    Args:
        file (Path): A pathlib.Path object representing the file to be sorted and moved.
        destination_root (Path): A destination path where the file will be moved to.
        side (str): A string representing the side of the file (e.g "CENTER", "RIGHT").
        part_type (str): a string representing the type of part the file belongs to (e.g. "EXT_WALL", "FLOOR").
        level (int): An integer representing the level of the file (e.g. 1, 2).
        default_case_folder (str, optional): A path to use as destination for the default case. Defaults to None.
    
    Returns:
        None
    """
    # Get the parent name of the file and its dimensions
    parent = file.parent.name
    dim = get_dimensions(file)
    dim_string = get_dim_string(file)

    # If the side parameter is defined, add it to the destination
    destination = destination_root
    if side:
        destination = destination_root / side
    if not level:
        level = "DEFAULT_LEVEL"

    # Sort the file based on the part type, level, and dimensions
    match part_type, level, dim:

        case "EXT_WALL", level, (28, 70):
            destination = destination / 'BATTEN' / 'EXT_WALL' / level / dim_string / 'BATTEN'

        case "EXT_WALL", level, (45, 45):
            destination = destination / 'BATTEN' / 'EXT_WALL' / level / dim_string / 'BATTEN'

        case "FLOOR", level, (28, 70):
            destination = destination / 'BATTEN' / 'FLOOR' / level / parent / 'BATTEN'

        case "ROOF", _, (28, 70) | (45, 45):
            destination = destination / 'BATTEN' / 'ROOF' / dim_string / parent / 'BATTEN'

        case "ROOF", _, (20, _):
            destination = destination / 'BATTEN' / 'ROOF' / 'RASPANT' / parent

        case "EXT_WALL", _, (21, 145):
            destination = destination / 'CLADDING' / 'EXT_WALL' / parent / '4.8m'

        case "EXT_WALL", _, (45, 195):
            destination = destination / 'FRAME' / 'EXT_WALL' / parent / 'FRAME'

        case "FLOOR", level, (45, 220):
            destination = destination / 'FRAME' / 'FLOOR' / level / parent / 'FRAME'

        case "INT_WALL", level, (_, _):
            destination = destination / 'FRAME' / 'INT_WALL' / dim_string / level / parent / 'FRAME'

        case "LGHA", _, (_, _):
            destination = destination / 'FRAME' / 'LGHA' / parent / 'FRAME'

        case "ROOF", _, (45, 145) | (45, 245):
            destination = destination / 'FRAME' / 'ROOF' / dim_string / parent / 'BEAM'

        case "ROOF", _, _:
            destination = destination / 'FRAME' / 'ROOF' / 'TOP_BOTTEN' / parent / 'TOP_BOTTEN'

        case _:
            destination = default_case_folder

    # Return destination.
    return destination


def combine_duplicates(folder, start_at_row, ptc_string):
    """
    Combines duplicate files in the specified folder, starting at the specified row.
    
    Parameters:
        folder (Path): The path to the folder containing the duplicate files.
        start_at_row (int): The row number to start searching for duplicates.
        ptc_string (str): The string representing the pieces to cut in the file.
    
    Returns:
        None
    """
    # Get a list of duplicate files in the specified folder, starting at the specified row
    duplicates = get_duplicates(folder, start_at_row)

    # Iterate through each group of duplicates
    for files in duplicates:

        # Print the name of the files that are being combined
        print(f"Combining : {files}")

        # Update the line in the first file with the combined pieces to cut value
        update_line_in_file(ptc_string, sum_pieces_to_cut(files), files[0])

        # Delete all the remaining duplicates
        for file in files[1:]:
            file.unlink()


def name_files_by_dim_and_index(folder):
    """
    Renames all files in the specified folder by their dimdimensions and index.
    
    Parameters:
        folder (Path): The path to the folder containing the files.
    
    Returns:
        None
    """
    # Iterate through each file in the folder
    for i, file in enumerate(list_dir(folder), 1):
        # Generate the new name based on the file's dimensions and index number.
        new_name = folder / f"{folder}-{get_dim_string(file)}" / f".{str(i).zfill(3)}"
        # Rename the file.
        file.rename(new_name)
        # Print the old and new name of the file.
        print(f"Renaming file: {file.name} to {new_name}")
    # Print an empty line for readability.
    print()


def name_files_by_index(directory):
    """
    Renames all files in the specified folder by their dimensions and index.
    
    Parameters:
        directory (Path): The path to the folder containing the files.
    
    Returns:
        None
    """
    # Iterate through each file in the folder
    for i, file in enumerate(list_dir(directory), 1):
        # Generate the new name based on the file's index number
        new_name = directory / directory.name / f".{str(i).zfill(3)}"
        # Rename the file.
        os.rename(file, new_name)
        print(f"Renaming file: {file.name} to {new_name}")
    # Print an empty line for readability.
    print()


# -------------------------------
# --- Misc helper functions -----
# -------------------------------


def get_letters(string: str) -> str:
    """
    Extracts all the letters from the given string and return them as a single string.
    """
    letters = "".join([char for char in string if char.isalpha()])
    return letters


def get_numbers(string: str) -> int:
    """
    Extracts all the numeric characters from the given string and return them as an integer.
    """
    numbers = "".join([char for char in string if char.isnumeric()])
    return int(numbers)


def get_dimensions(file: Path):
    """
    Returns a tuple with the height and width of the given file.
    """
    return get_height(file), get_width(file)


def get_dim_string(file):
    """
    Returns a string with the dimensions of the given file in the format "height x width".
    """
    return f"{get_height(file)}x{get_width(file)}"


def get_height(file, height_str="fdtHeight :="):
    """
    Returns the height of the given file as an integer.
    """
    return line_value(height_str, file)


def get_width(file, width_str="fdtWidth :="):
    """
    Returns the width of the given file as an integer.
    """
    return line_value(width_str, file)


def files_in_folder(folder):
    """
    Returns the number of files in a directory as an integer.
    """
    return len([child for child in list_dir(folder) if child.is_file()])


def get_duplicates(path, start_at=7):
    """
    Returns a list of lists, where each inner list contains duplicate files found in the given path.
    Duplicates are determined by comparing the contents of the directory, starting from the specified line (start_at).
    
    Parameters:
        path (Path): The path to search for duplicate files.
        start_at (int, optional): Ignore reading all lines before this line number. Default is 7.

    Returns (List)
    """
    # Create a dictionary to store the contents of each directory
    file_contents = {}

    # Iterate through all the files in path
    for directory in path.iterdir():

        # Open the directory and read its contents into a list
        with open(directory, 'r') as f:
            lines = f.readlines()

        # Create a key for this directory's contents by joining all the lines starting from start_at
        key = ''.join(lines[start_at:])

        # If this key already exists in the dictionary, append the directory name to the list of files with this content
        if key in file_contents:
            file_contents[key].append(directory)
        # If the key does not yet exist in the dictionary, create a new entry for it with a single directory name
        else:
            file_contents[key] = [directory]

    # Return the dictionary of directory contents and the corresponding list of directory names
    return [duplicates for duplicates in file_contents.values() if len(duplicates) > 1]


def move_file(file_path, destination_path):
    """
    Moves the file at the given file path to the destination path and prints a message about the move.

    Parameters:
        file_path (Path): The path to the file to move.
        destination_path (Path): The destination path for the file.

    Returns:
        None
    """
    # Create the parent directory if it doesn't exist
    if not destination_path.exists():
        os.makedirs(destination_path)

    # Move the file
    shutil.move(file_path, destination_path)

    # Print a message about the move
    print(f"Copying {file_path} ---> {destination_path}")


def combine_file_names(root_dir):
    """
    Combines all the files in the given root directory into a single file and removes the original directories.

    Parameters:
        root_dir (pathlib.Path): The root directory containing the files to combine.

    Returns:
        None
    """
    # Get a list of all the directories in the root directory
    folders = list_dir(root_dir)

    # Sort the directories by the numeric characters in their names
    folders.sort(key=get_numbers)

    # Create a new name for the combined file.
    # # Concatenate the first part of each directory name and the second part of the first directory name
    new_name = f"{' '.join([folder.name.split()[0] for folder in folders])} {folders[0].name.split()[1]}"
    new_name = root_dir / new_name

    # Get a list of all the files in the root directory
    files = get_files_in_dir(root_dir)

    # Move each file to the new directory
    for file in files:
        move_file(file, new_name)

    # Delete the original directories, but skip the new directory
    for old_folder in folders:
        if old_folder != new_name:
            shutil.rmtree(old_folder)


def combine_parent_dirs(root_dir):
    """
    Combine all subdirectories in the root directory into a single directory.

    Args:
        root_dir (Path): The root directory containing the subdirectories to combine.

    Returns:
        None
    """

    # Get a list of subdirectories in the root directory
    subdirectories = [d for d in root_dir.iterdir() if d.is_dir()]

    # Iterate over the subdirectories
    for subdir in subdirectories:
        # Create a new directory name by combining the subdirectory names
        new_dir_name = ' '.join(subdir.name for subdir in subdirectories)
        new_dir_path = root_dir / new_dir_name

        # Create the new directory
        new_dir_path.mkdir(exist_ok=True)

        # Move all the files in the subdirectory to the new directory
        for file in subdir.iterdir():
            file.rename(new_dir_path / file.name)

        # Remove the empty subdirectory
        subdir.rmdir()


def get_files_in_dir(path):
    """
    Get a list of files in the specified directory.

    Args:
        path (Path): The directory to search for files.

    Returns:
        List[Path]: A list of Path objects representing the files in the directory.
    """
    return path.glob("*.*")


def get_subdirs(path):
    """
    Get a list of subdirectories in the specified directory.

    Args:
        path (Path): The directory to search for subdirectories.

    Returns:
        List[Path]: A list of Path objects representing the subdirectories in the directory.
    """
    return [item for item in path.iterdir() if item.is_dir()]


def get_parent_dirs(path):
    """
    Get a list of parent directories in the specified directory that contain at least one file.

    Args:
        path (Path): The directory to search for parent directories.

    Returns:
        List[Path]: A list of Path objects representing the parent directories in the directory.
    """
    return [subdir for subdir in path.iterdir() if any([sub.is_file() for sub in subdir])]
        

def read_lines(path):
    """
    Read the lines of a file.

    Args:
        path (Path): The file to read.

    Returns:
        List[str]: A list of strings representing the lines of the file.
    """
    with path.open() as f:
        return f.readlines()


def line_value(find, path) -> int:
    """
    Find the value of a line in a file.

    Args:
        find (str): The string to search for in the file.
        path (Path): The file to search.

    Returns:
        int: The value of the line as an integer. If the string is not found in the file, returns None.
    """
    for line in read_lines(path):
        if find in line:
            return int(line.split()[-1])


def sum_pieces_to_cut(file_paths, ptc="fdtNr_Of_Pieces_To_Cut := "):
    """
    Sum the values of the "fdtNr_Of_Pieces_To_Cut" lines in a list of files.

    Args:
        file_paths (List[Path]): The list of files to search.
        ptc (str): The string to search for in the files (default is "fdtNr_Of_Pieces_To_Cut := ").

    Returns:
        int: The sum of the values of the lines in the files.
    """
    return sum([line_value(ptc, path) for path in file_paths])


def update_line_in_file(replace, value, file_path):
    """
    Reads the file at the given file path and finds the first line that contains the given string.
    Replaces whatever comes after the first space in that line with the given value.

    Parameters:
        replace (str): The string to search for in the file.
        value (int): The value to use as a replacement for the text after the first space.
        file_path (Path): The path to the file to modify.

    Returns:
        None
    """
    # Open the file in read mode
    with file_path.open("r") as f:
        # Read the lines of the file into a list
        lines = f.readlines()

    # Find the first line that contains the string we want to replace
    for i, line in enumerate(lines):
        if replace in line:
            # Split the line into variable and value using the space character as a delimiter
            words = line.split()
            # Replace the value (index -1) with the new value
            words[-1] = str(value)
            # Join the words back into a single string, separated by spaces
            lines[i] = " ".join(words)
            break

    # Open the file in write mode
    with file_path.open("w") as f:
        # Write the modified lines back to the file
        f.writelines(lines)


def same_lines(file_1, file_2):
    """
    Determine if two files have the same lines.

    Args:
        file_1 (Path): The first file to compare.
        file_2 (Path): The second file to compare.

    Returns:
        bool: True if the files have the same lines, False otherwise.
    """
    return read_lines(file_1) == read_lines(file_2)


def reset_from_backup(root_path, backup_path):
    """
    Reset a directory to its state in a backup directory.

    Args:
        root_path (Path): The root directory to reset.
        backup_path (Path): The backup directory to restore from.

    Returns:
        None
    """
    if root_path.exists():
        shutil.rmtree(root_path)
    shutil.copytree(backup_path, root_path)


def list_dir(path):
    """
    List the items in a directory.

    Args:
        path (Path): The directory to list.

    Returns:
        List[Path]: A list of Path objects representing the items in the directory.
    """
    return list(path.iterdir())

# Recommended order:
# reset_active_folder_from_backup(root_path, backup_path)
# sort_all(source_path, destination_path)
# combine_all_duplicates(destination_path)
# rename_all(destination_path)

def main(base_path, house_unit):
    """
    Main function.

    Recommended order of use:

    reset_from_backup

    """
    active = base_path / "active"
    backup = base_path / "backup"

    root_path = active / "root"
    destination_path = active / "destination"
    default_dest = active / "default"

    reset_from_backup(active, backup)

    for directory in root_path.iterdir():
        side, part_type, level = house_unit.get_categories(directory)
        for file in directory.iterdir():
            
            destination = get_destination(file, destination_path)
            print(f"name: {file}: {(side, part_type, level)}\n---> {destination}\n")
            move_file(file, destination)


if __name__ == "__main__":
    base_path = Path.cwd() / "assets"
    house_unit = Cm06()
    main(base_path, house_unit)

