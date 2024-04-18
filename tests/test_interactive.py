import os
import unittest

import pandas

import readwrite
import readwrite.interactive


def fixture_path(name: str):
    return os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        name
    )


class NameTest(unittest.TestCase):

    def test_guess_name_dataframe(self):
        x = pandas.DataFrame()
        name = readwrite.interactive.guess_name(x)

        self.assertEquals("df", name)

    def test_guess_name_zip(self):
        import zipfile

        with zipfile.ZipFile(fixture_path("hello.zip")) as x:
            name = readwrite.interactive.guess_name(x)

        self.assertEquals("file", name)

    def test_guess_name_other(self):
        x = "hello"
        name = readwrite.interactive.guess_name(x)

        self.assertEquals("x", name)


class CommonImportsTest(unittest.TestCase):

    def test_load_common_imports(self):
        imports = readwrite.interactive.load_common_imports()

        import sys
        self.assertEquals(sys, imports["sys"])

        import os
        self.assertEquals(os, imports["os"])

        import tqdm
        self.assertEquals(tqdm, imports["tqdm"])

        import json
        self.assertEquals(json, imports["json"])

        import pandas
        self.assertEquals(pandas, imports["pandas"])
        self.assertEquals(pandas, imports["pd"])


class ReadlineTest(unittest.TestCase):

    def test__get_readline(self):
        readline = readwrite.interactive._get_readline()

        self.assertIsNotNone(readline)
