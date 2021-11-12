import unittest
import assignment_seven


class MyTestCase(unittest.TestCase):
    def test_encode_one(self):
        self.assertEqual("sbwkrq", assignment_seven.encode("python", 3))
        self.assertEqual("vjcv ycu eqqn", assignment_seven.encode("that was good", 2))
        self.assertEqual("tff zb!", assignment_seven.encode("see ya!", 1))

    def test_decode_one(self):
        self.assertEqual("python", assignment_seven.encode("sbwkrq", 3))
        self.assertEqual("that was good", assignment_seven.encode("vjcv ycu eqqn", 2))
        self.assertEqual("see ya!", assignment_seven.encode("tff zb!", 1))
    def test_encode_two(self):
        self.assertEqual("wcescjdpek", assignment_seven.encode("hello world", "python"))

    def test_option_three(self):
        pass



if __name__ == '__main__':
    unittest.main()
