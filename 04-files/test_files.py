import unittest
import files

class TestFiles(unittest.TestCase):

    def test_read_file_contents(self):
        self.assertEqual(files.read('test.txt'),
"""Beautiful is better than ugly.
Explicit is better than implicit.""")
        self.assertEqual(len(files.read('zen.txt')), 856)

    def test_file_contains(self):
        # implement files.contains that will check whether a file contains some text
        self.assertTrue(files.contains('better', 'test.txt'))
        self.assertFalse(files.contains('Hello', 'test.txt'))
        self.assertTrue(files.contains('a', 'zen.txt'))
        self.assertFalse(files.contains('invalid', 'test.txt'))

    def test_return_only_rows_starting_with(self):
        # implement files.file_rows_starting_with which will return only those rows from a file that start with some string
        self.assertEqual(files.file_rows_starting_with('Beautiful', 'test.txt'),
"""Beautiful is better than ugly.
""")
        self.assertEqual(files.file_rows_starting_with('E', 'zen.txt'),
"""Explicit is better than implicit.
Errors should never pass silently.
""")

if __name__ == "__main__":
    unittest.main()
