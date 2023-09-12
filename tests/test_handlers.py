import os
import unittest
import pandas
import json
import pickle
import readwrite
import readwrite.registry


def dummy_path(name: str):
    return os.path.join(
        os.path.dirname(__file__),
        "dummy",
        name
    )


registry = readwrite.registry.get_global_registry()


class HandlerCsvTest(unittest.TestCase):

    handler = registry.get("csv")
    content = pandas.DataFrame([42], columns=["world"])

    def test_read(self):
        path = dummy_path("hello.csv")
        x = self.handler.read(path)

        self.assertTrue(self.content.equals(x))

    def test_write(self):
        path = "/tmp/hello.csv"
        self.handler.write(self.content, path, index=0)

        self.assertTrue(self.content.equals(pandas.read_csv(path)))


class HandlerJsonTest(unittest.TestCase):

    handler = registry.get("json")
    content = {"world": 42}

    def test_read(self):
        path = dummy_path("hello.json")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.csv"
        self.handler.write(self.content, path, index=0)

        with open(path) as fd:
            x = json.load(fd)

        self.assertEqual(self.content, x)


class HandlerParquetTest(unittest.TestCase):

    handler = registry.get("parquet")
    content = pandas.DataFrame([42], columns=["world"])

    def test_read(self):
        path = dummy_path("hello.parquet")
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
        path = dummy_path("hello.pickle")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.pickle"
        self.handler.write(self.content, path, index=0)

        with open(path, "rb") as fd:
            x = pickle.load(fd)

        self.assertEqual(self.content, x)


class HandlerTxtTest(unittest.TestCase):

    handler = registry.get("txt")
    content = "world"

    def test_read(self):
        path = dummy_path("hello.txt")
        x = self.handler.read(path)

        self.assertEqual(self.content, x)

    def test_write(self):
        path = "/tmp/hello.txt"
        self.handler.write(self.content, path)

        with open(path) as fd:
            x = fd.read()

        self.assertEqual(self.content, x)
