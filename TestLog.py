import unittest
from Log import Log
import logging
class TestLog(unittest.TestCase):
    def test_Singleton(self):
        l1 = Log()
        l2 = Log()
        self.assertTrue(l1 is l2)
        self.assertTrue(l1 is Log())
    def test_Handler(self):
        self.assertTrue(Log().Logger.hasHandlers())
    def test_Logger(self):
        self.assertEqual(logging.DEBUG, Log().Logger.getEffectiveLevel())
        Log().Logger.setLevel(logging.INFO)
        self.assertEqual(logging.INFO, Log().Logger.getEffectiveLevel())

