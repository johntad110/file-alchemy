# File Alchemy

## Overview

The File Sorting Script is a simple Python utility designed to help you organize your files effortlessly. By providing it a target folder, the script automatically sorts the files within it based on their file extensions into separate subfolders. This saves you time and ensures that your files are neatly organized for easy access and better file management.

## Features

- **Efficient File Sorting**: The script quickly and efficiently sorts files in a specified folder based on their file extensions.

- **Automatic Organization**: Files are automatically categorized into separate subfolders according to their file extensions, resulting in a well-structured and organized file system.

- **Customizable Configuration**: You can easily customize the script's behavior by editing the configuration file to define the desired sorting rules according to your preferences.

## Usage

1. Clone the repository to your local machine using the following command:

```

git clone https://github.com/johntad110/file-alchemy.git

```

2. `cd` into the cloned repo's directory on your machine.

3. Install the project dependencies by running the following command:

```

pip install -r requirements.txt

```

This command will install the necessary Python packages required for the File Sorting Script to run properly.

4. Edit the configuration file (`config.yaml`) to define the desired sorting rules. You can specify the target folder, file extensions, and corresponding subfolders in the configuration file. Open the `config.yaml` file in a text editor and modify the values according to your requirements.

5. Run the script by executing the following command:

```

python main.py

```

The script will use the configuration defined in the `config.yaml` file to sort the files in the target folder based on the specified sorting rules.

## Example

If you have a folder named "Documents" containing various files such as "report.docx," "presentation.pptx," and "image.jpg," you can customize the `config.yaml` file to specify the target folder as "Documents" and define the desired sorting rules. Running the `main.py` file will automatically create subfolders like "Documents/Docs," "Documents/Presentations," and "Documents/Images." The corresponding files will be moved into their respective subfolders based on their file extensions.

## Contributing

Contributions to the File Alchemy Project are welcome! If you encounter any issues or have suggestions for improvements, please submit them through the [issue tracker](https://github.com/johntad110/file-alchemy/issues). You can also contribute directly by submitting pull requests with your proposed changes.

## License

The File Alchemy Project is open-source software licensed under the [MIT License](https://opensource.org/licenses/MIT). Please see the [LICENSE](https://github.com/johntad110/file-alchemy/blob/main/LICENSE) file for more details.

---

Thank you for using the File Alchemy. We hope this utility simplifies your file organization process and helps you maintain a tidy file system. For any questions or support, please [contact](mailto:johntad110@gmail.com).
