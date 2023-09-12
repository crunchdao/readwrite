import unittest
import readwrite


class ModuleTest(unittest.TestCase):

    def test_read(self):
        self.assertIsNotNone(readwrite.read)

    def test_write(self):
        self.assertIsNotNone(readwrite.write)
