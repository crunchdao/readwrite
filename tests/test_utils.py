import io
import logging
import unittest

import readwrite
import readwrite.utils


class MeasureDurationTest(unittest.TestCase):

    def setUp(self):
        readwrite.debug(True)

        self._log_output = io.StringIO()
        self._stream_handler = logging.StreamHandler(self._log_output)
        readwrite.constants.LOGGER.addHandler(self._stream_handler)

    def tearDown(self):
        readwrite.debug(False)

        readwrite.constants.LOGGER.removeHandler(self._stream_handler)
        del self._log_output
        del self._stream_handler
    
    @property
    def log_output(self):
        return self._log_output.getvalue()

    def test_ok(self):
        with readwrite.utils.measure_duration("a", "b", "c"):
            self.assertIn("a - handler=b path=`c`\n", self.log_output)

        self.assertIn("a - handler=b path=`c` duration=", self.log_output)

    def test_continue_raise(self):
        message = "hello world"

        with self.assertRaises(ValueError) as context:
            with readwrite.utils.measure_duration("a", "b", "c"):
                self.assertIn("a - handler=b path=`c`\n", self.log_output)
                raise ValueError(message)

        self.assertIn("a - handler=b path=`c` duration=", self.log_output)
        self.assertEquals(str(context.exception), message)
