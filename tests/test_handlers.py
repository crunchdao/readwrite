import json
import os
import pickle
import unittest

import pandas
import toml
import yaml

import readwrite
import readwrite.registry


def fixture_path(name: str):
    return os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        name
    )


registry = readwrite.registry.get_global_registry()


class HandlerBinaryTest(unittest.TestCase):

    handler = registry.get("bin")
    content = "world".encode("ascii")

    def test_read(self):
        path = fixture_path("hello.bin")
        x = self.handler.read(path)

        self.assertEquals(self.content, x)

    def test_write(self):
        path = "/tmp/hello.bin"
        self.handler.write(self.content, path, index=0)

        with open(path, "rb") as fd:
            self.assertEquals(self.content, fd.read())


class HandlerCsvTest(unittest.TestCase):

    handler = registry.get("csv")
    content = pandas.DataFrame([42], columns=["world"])

    def test_read(self):
        path = fixture_path("hello.csv")
        x = self.handler.read(path)

        self.assertTrue(self.content.equals(x))

    def test_write(self):
        path = "/tmp/hello.csv"
        self.handler.write(self.content, path, index=0)

        self.assertTrue(self.content.equals(pandas.read_csv(path)))


class HandlerExcelTest(unittest.TestCase):

    handler = registry.get("xlsx")
    content = pandas.DataFrame([42], columns=["world"])

    def test_read(self):
        path = fixture_path("hello.xlsx")
        x = self.handler.read(path)

        self.assertTrue(self.content.equals(x))

    def test_write(self):
        path = "/tmp/hello.xlsx"
        self.handler.write(self.content, path, index=False)

        self.assertTrue(self.content.equals(pandas.read_excel(path)))


class HandlerJsonTest(unittest.TestCase):

    handler = registry.get("json")
    content = {"world": 42}

    def test_read(self):
        path = fixture_path("hello.json")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.json"
        self.handler.write(self.content, path)

        with open(path) as fd:
            x = json.load(fd)

        self.assertEqual(self.content, x)


class HandlerParquetTest(unittest.TestCase):

    handler = registry.get("parquet")
    content = pandas.DataFrame([42], columns=["world"])

    def test_read(self):
        path = fixture_path("hello.parquet")
        x = self.handler.read(path)

        self.assertTrue(self.content.equals(x))

    def test_write(self):
        path = "/tmp/hello.parquet"
        self.handler.write(self.content, path, index=0)

        self.assertTrue(self.content.equals(pandas.read_parquet(path)))


class HandlerPickleTest(unittest.TestCase):

    handler = registry.get("pickle")
    content = {"world": 42}

    def test_read(self):
        path = fixture_path("hello.pickle")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.pickle"
        self.handler.write(self.content, path)

        with open(path, "rb") as fd:
            x = pickle.load(fd)

        self.assertEqual(self.content, x)

    def test_read_pandas(self):
        path = fixture_path("hello.pickle")
        x = self.handler.read(path, pandas=True)

        self.assertEqual(self.content, x)

    def test_write_pandas(self):
        path = "/tmp/hello.pickle"
        self.handler.write(self.content, path, pandas=True)

        x = pandas.read_pickle(path)

        self.assertEqual(self.content, x)


class HandlerTomlTest(unittest.TestCase):

    handler = registry.get("toml")
    content = {"world": 42}

    def test_read(self):
        path = fixture_path("hello.toml")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.toml"
        self.handler.write(self.content, path)

        with open(path) as fd:
            x = toml.load(fd)

        self.assertEqual(self.content, x)


class HandlerTextTest(unittest.TestCase):

    handler = registry.get("txt")
    content = "world"

    def test_read(self):
        path = fixture_path("hello.txt")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.txt"
        self.handler.write(self.content, path)

        with open(path) as fd:
            x = fd.read()

        self.assertEqual(self.content, x)


class HandlerYamlTest(unittest.TestCase):

    handler = registry.get("yaml")
    content = {"world": 42}

    def test_read(self):
        path = fixture_path("hello.yaml")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.yaml"
        self.handler.write(self.content, path)

        with open(path) as fd:
            x = yaml.full_load(fd)

        self.assertEqual(self.content, x)
