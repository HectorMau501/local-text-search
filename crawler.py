import os

def find_txt_files(directory: str) -> list[str]:
    """
    Recursively find all .txt files in the given directory.

    Args:
        directory (str): The directory to search for .txt files.
    Returns:
        list[str]: A list of paths to .txt files found in the directory.
    """
    txt_files = []
    folder = os.listdir(directory) #list of names in the directory
    for name in folder:
        name_path = os.path.join(directory, name)#for each name in the folder
        #Validate if the current path is a directory or a .txt file
        if os.path.isdir(name_path):
            txt_files.extend(find_txt_files(name_path)) # Recursively search in subdirectory
        elif os.path.isfile(name_path) and name_path.endswith(".txt"):
            txt_files.append(name_path) #Add .txt file to the list
    return txt_files




