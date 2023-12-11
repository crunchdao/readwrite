import logging
import unittest

import readwrite


class ModuleTest(unittest.TestCase):

    def test_read(self):
        self.assertIsNotNone(readwrite.read)

    def test_read_as(self):
        self.assertIsNotNone(readwrite.read_as)

    def test_write(self):
        self.assertIsNotNone(readwrite.write)

    def test_write_as(self):
        self.assertIsNotNone(readwrite.write_as)

    def test_debug(self):
        self.assertIsNotNone(readwrite.debug)

        self.assertEqual(logging.NOTSET, readwrite.LOGGER.level)

        readwrite.debug(True)
        self.assertEqual(logging.DEBUG, readwrite.LOGGER.level)

        readwrite.debug(False)
        self.assertEqual(logging.NOTSET, readwrite.LOGGER.level)
