import sys
sys.path.append('../')
# sys.path.insert(0, '/path/to/application/app/folder')
# from flask import Flask
#from flask_testing import TestCase
import unittest
from unittest import TestCase
import read_ini

# class MyTest(TestCase):
#     def create_app(self):
#         app = Flask(__name__)
#         app.config['TESTING'] = True
#         return app
#     

class TestDBcon(TestCase):
    def setUp(self):
        TestCase.setUp(self)
         
    def test_settings_ini_has_all_required_keys(self):
        expected_keys = ['name', 'age' , 'height']
        filename = '../settings.ini'
        ini_to_dict = read_ini.convert_settings_ini_to_dict(filename)
        keys_retrived_from_ini_file = list(ini_to_dict) # or [*ini_to_dict]
        for k in expected_keys:
            self.assertIn(k, 
                      keys_retrived_from_ini_file,
                      'we got %s' % 
                             keys_retrived_from_ini_file)
#         self.assertListEqual(keys_retrived_from_ini_file,
#                              expected_keys, 'we got %s' % 
#                              keys_retrived_from_ini_file)
                
        
    
    def test_get_value_from_settings_ini_file(self):
        expected_result = 'bhujay'
        self.assertEqual(read_ini.get_value_from_settings_ini_file('name'), 
                         expected_result, 'Test result is % s' % 
                         read_ini.get_value_from_settings_ini_file('name'))
        
        
if __name__ == '__main__':
    unittest.main()