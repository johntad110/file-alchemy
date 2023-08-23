import os
import shutil
import unittest
from sort_file import sort_files


class FileSortingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.config = {
            'downloads_folder': 'test_data',
            'file_types': [
                {
                    'folder': 'test_data/Documents',
                    'extensions': ['.txt', '.doc', '.docx']
                },
                {
                    'folder': 'test_data/Pictures',
                    'extensions': ['.jpg', '.png']
                },
                {
                    'folder': 'test_data/Others',
                    'extensions': ['']
                }
            ],
            'others': 'test_data/Others',
            'blacklist': ['test_data/test.txt']
        }

        # Create test files
        os.makedirs('test_data/Documents')
        os.makedirs('test_data/Pictures')
        os.makedirs('test_data/Others')
        open('test_data/test.txt', 'w').close()  # Blacklisted file
        open('test_data/test.doc', 'w').close()
        open('test_data/test.jpg', 'w').close()
        open('test_data/test.pdf', 'w').close()

    def tearDown(self) -> None:
        # Clean up test files
        shutil.rmtree('test_data')

    def test_sort_files(self):
        sort_files(self.config)

        # check if the files are sorted correctly
        print(list(os.walk('test_data/')))
        self.assertTrue(os.path.exists('test_data/Documents/test.doc'))
        self.assertTrue(os.path.exists('test_data/Pictures/test.jpg'))
        self.assertTrue(os.path.exists('test_data/Others/test.pdf'))
        self.assertFalse(os.path.exists('test_data/Documents/test.txt'))


if __name__ == '__main__':
    unittest.main()
