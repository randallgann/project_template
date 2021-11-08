import unittest
import sys, os.path, re

sys.path.insert(0, 'object_path')
bin_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.abspath(bin_path)

import object_name

class Testdb_client(unittest.TestCase):

    def setUp(self):
        mode = 'unittest'
        self.app = object_name.function()


if __name__=='__main__':
    unittest.main()