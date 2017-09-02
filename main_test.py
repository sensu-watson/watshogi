import unittest
from main import *

class MainRoopTest(unittest.TestCase):
    def setUp(self):
        self.mainRoop = main.MainRoop()
        mainRoop.response(['usi'])

if __name__ == '__main__':
    unittest.main()
