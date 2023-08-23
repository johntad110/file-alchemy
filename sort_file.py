import os
import shutil
import yaml
import logging

logging.basicConfig(filename="file_alchemy.log", level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def load_config(config_file):
    """Loads the YAML configuration file."""
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config


def create_folder(folder):
    """Create a folder if it doesn't exist"""
    if not os.path.exists(folder):
        os.makedirs(folder)


def move_file(source, destination):
    """Move a file to the destination folder."""
    try:
        shutil.move(source, destination)
        logging.info(f"Moved file: {source} to {destination}")
    except Exception as e:
        logging.error(f"Error moving file: {source}. Reason: {str(e)}")


def get_file_list(directory) -> list:
    """Get a list of all files in the specified directory"""
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
        break
    return file_list


def get_file_destination(file_path, config):
    """Return: file path and destination path based on the config."""
    file_path = os.path.normpath(file_path)
    for f_type in config.get('file_types', []):
        create_folder(f_type['folder'])

        if os.path.splitext(file_path)[1].lower() in f_type['extensions']:
            return file_path, os.path.normpath(f_type['folder'])
    return file_path, os.path.normpath(config.get('others', 'folder'))


def sort_files(config):
    """Sort files based on the configuration."""
    downloads_folder = config['downloads_folder']
    blacklist = config.get('blacklist', [])
    blacklist = [os.path.normpath(x) for x in blacklist]
    files = get_file_list(downloads_folder)

    for file in files:
        f_p, f_d = get_file_destination(file, config)
        if f_p not in blacklist:
            move_file(f_p, f_d)
