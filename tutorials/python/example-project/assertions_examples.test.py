import unittest

class AssertExamplesTestTest(unittest.TestCase):

    """
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
    """
    def test_compare_strings_expected_to_be_equal(self):
        self.assertEqual('abcde', 'abcde')

    """
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual
    """
    def test_compare_strings_expected_to_be_not_equal(self):
        self.assertNotEqual('abc', 'def')

    """
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue
    """
    def test_assert_true_boolean_expression(self):
        self.assertTrue(len("abcde") > 2)

    """
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse
    """
    def test_assert_false_boolean_expression(self):
        self.assertFalse(len("abcde") < 2)

if __name__ == '__main__':
    unittest.main()
