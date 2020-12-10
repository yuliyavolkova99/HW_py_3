import unittest
class fun_test(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max(2, 8, 10), 10)

    def test_min(self):
        self.assertEqual(min(2, 8, 10), 2)

    def test_int(self):
        self.assertEqual('python'.upper(), 'PYTHON')
        
    def test_true(self):
        self.assertTrue('python'.islower())
        self.assertFalse('python'.isupper())

if __name__ == '__main__':
    unittest.main()
