import unittest
import main
from main.services.converterService import ConverterService

class TestConverterService(unittest.TestCase):

    def setUp(self):
        self.converterSrv = ConverterService()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_simple(self):
        self.assertEqual(self.converterSrv.fonction_a_tester(1,1), 2)

if __name__ == '__main__':
    unittest.main()