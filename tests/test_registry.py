import unittest

import readwrite
import readwrite.handlers.csv
import readwrite.registry

registry = readwrite.registry.get_global_registry()


class RegistryTest(unittest.TestCase):
    def test_get_from_path(self):
        self.assertIsInstance(registry.get("a.csv"), readwrite.handlers.csv.CsvHandler)

    def test_get(self):
        self.assertIsInstance(registry.get("csv"), readwrite.handlers.csv.CsvHandler)

    def test_get_not_found(self):
        self.assertRaises(
            readwrite.registry.UnknownExtension, lambda: registry.get("abcdef")
        )
