import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(), 5)

if __name__ == "__main__":
    unittest.main()