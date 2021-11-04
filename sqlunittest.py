#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
#import init_db
import os
import sqlite3

class storedbTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        #init_db
        pass

    def tearDown(self):
        """
        if os.path.exists("database.db"):
            os.remove("database.db")
        """
        pass
            
    def test_init(self):
        pass

    def test_name(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.execute("SELECT uname from contacts WHERE id = 1")
        self.assertEqual(cursor.fetchone()[0], 'First Name')
        conn.close()
        
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
