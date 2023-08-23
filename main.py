import logging
from sort_file import sort_files, load_config

# Setup logging
logging.basicConfig(filename="file_alchemy.log", level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def main():
    config_file = 'config.yaml'
    config = load_config(config_file)

    try:
        sort_files(config)
        logging.info("File sorting completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred during file sorting. Reason: {str(e)}")


if __name__ == '__main__':
    main()
