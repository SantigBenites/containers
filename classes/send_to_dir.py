import os, shutil, subprocess, glob, pathlib

# Consts
CURRENT_DIR = os.getcwd()
ACTIVE_DIRECTORY = f"/opt/containers/"
WORKING_DIR = f"{CURRENT_DIR}/classes"

# File Directories
DEFAULT_DIR = "/opt/containers"
DESKTOP_DIR = "/usr/local/share/applications/fcul"
ICONS_DIR = "/usr/local/share/icons/fcul"
SIFS_DIR = "/opt/sifs"

def get_extension(filename):
    """Return the extension of a given filename."""
    try:
        return filename.rsplit(".", 1)[1]
    except IndexError:
        return ""

def is_whitelisted(name):
    """Return True if the given node should be processed, False otherwise."""
    extensions = ["desktop", "ico", "png", "xpm","sif","def"]
    whitelist = [
        "run.sh",
        "run_cli.sh",
        "run_gui.sh",
        "apptainer-fcul.conf",
        "bash.bashrc",
        "supervisord.conf"
    ]
    return (
        name in whitelist
        or get_extension(name) in extensions
    )

def get_absolute_file_paths(folder_path):
    absolute_file_paths = []
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            absolute_file_path = os.path.join(foldername, filename)
            absolute_file_paths.append(absolute_file_path)
    return absolute_file_paths

def utility_folders(file_path):
    ignored_dirs = ["template","utils"]
    for dir in ignored_dirs:
        if dir in file_path:
            return True
    return False

def relative_path(file_path):
    root_path = "/containers/classes/"
    index = file_path.find(root_path)
    if index != -1:
        return file_path[index + len(root_path):]
    else:
        return file_path
    
def get_file_copy_location(file_name,file_path):
    
    extension = get_extension(file_name)
    
    if extension == "sif":
        return f"{SIFS_DIR}/{file_name}"
    elif extension == "png":
        return f"{ICONS_DIR}/{file_name}"
    elif extension == "desktop":
        return f"{DESKTOP_DIR}/{file_name}"
    else:
        return f"{DEFAULT_DIR}/{file_path}"

def main():
    """Get container scripts, icons and desktop shortcuts from git repository."""

    files_absolute_path = get_absolute_file_paths(WORKING_DIR)
    
    for file in files_absolute_path:
        if utility_folders(file):
            continue
        
        file_path = relative_path(file)
        file_name = file_path.split("/")[-1]
        
        
        if is_whitelisted(file_name):
            
            SOURCE = file_path
            DESTINATION = get_file_copy_location(file_name,file_path)
            
            directory = "".join(file_path.split("/")[:-1])
            os.makedirs(f"{DEFAULT_DIR}/{directory}",exist_ok=True)
            
            shutil.copy2(file, DESTINATION)
        


if __name__ == "__main__":
    main()