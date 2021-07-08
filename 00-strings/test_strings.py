import unittest
import strings

class TestStrings(unittest.TestCase):

    def test_get_string_length(self):
        self.assertEqual(strings.length(''), 0)
        self.assertEqual(strings.length('foo'), 3)

    def test_get_string_without(self):
        # implement strings.without that will remove given characters
        self.assertEqual(strings.without('abba', 'a'), 'bb')
        self.assertEqual(strings.without('abba', 'cd'), 'abba')
        self.assertEqual(strings.without('foobar', 'ob'), 'far')

    def test_count_discint_chars(self):
        # implement strings.count_distinct that will count the number of distinct characters
        self.assertEqual(strings.count_distinct('abba'), 2)
        self.assertEqual(strings.count_distinct('abcdfda'), 5)

    def test_tokens(self):
        # implement strings.tokens that will return a list of substrings split from . and removes empty tokens
        self.assertEqual(strings.tokens('foo.bar'), ['foo', 'bar'])
        self.assertEqual(strings.tokens('..foo..bar..'), ['foo', 'bar'])
        self.assertEqual(strings.tokens('hello'), ['hello'])

if __name__ == '__main__':
    unittest.main()
