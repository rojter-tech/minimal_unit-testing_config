import unittest
import src

class ImportTest(unittest.TestCase):

    def test_module_import(self):
        try:
            module_import = src.module_import
        except:
            module_import=False
        self.assertTrue(module_import)