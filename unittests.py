#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import coroutine
import unittest
import init_db
import os
import sqlite3
import re
import pandas
import textExchange

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
        init_db
        if not os.path.exists("database.db"):
            raise AssertionError(".db does not exist")
        else:
            pass

    def test_name(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.execute("SELECT uname from contacts WHERE id = 1")
        self.assertEqual(cursor.fetchone()[0], 'First Name')
        conn.close()

    def test_email(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.execute("SELECT email from contacts WHERE id = 2")
        self.assertEqual(cursor.fetchone()[0], 'second@gmail')
        conn.close()
        
    def test_content(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.execute("SELECT content from contacts WHERE email = 'first@gmail'")
        self.assertEqual(cursor.fetchone()[0], 'Content for the first name')
        conn.close()
    
    def test_swapCoordinates(self):
        l = [[],'South America','Africa','Europe','Australia','North America','Asia']
        
        for i in l:
            #get what is currently in place for long and lat
            current_text = textExchange.getCurrentCorrdinates()
            #swap out cordinates for new ones given country
            textExchange.swapCoordinates(i)
            #get coordinates after swap
            afterSwap_text = textExchange.getCurrentCorrdinates()
            #print(current_text == afterSwap_text)
            self.assertFalse(current_text == afterSwap_text)

    def testCheckCoordinates_swapCoordinates(self):
        l = ['Asia','Africa','Europe','Australia','North America','South America']
        coordinates =[[89.2343748, 51.2086975], [17.7578122, 11.5024338],[10.0, 51.0],[134.755, -24.7761086], [-109.0, 51.0000002], [-61.0006565, -21.0002179]]
        #check coordinates input to html are what was requested
        #change coordinates one at a time and check if they are accuart for the requested country
        for i in range(len(l)):
            #swap out cordinates for new ones given country
            textExchange.swapCoordinates(l[i])
            afterSwap_text = textExchange.getCurrentCorrdinates()
            expectedText = 'fromLonLat('+str(coordinates[i])+')'
            #check that the swap is consistent to the known coordinates in the list coordinates
            self.assertTrue(expectedText==afterSwap_text[0])

    def test_GetIframe(self):
        l = ['Happy','Mellow','Energetic','Relaxing']
        for i in l:
            with open("templates/index.html", 'r+') as f:
                text = f.read()
                oldIframe = re.findall(r'(?:<iframe[^>]*)(?:(?:\/>)|(?:>.*?<\/iframe>))',text)
                #print(oldIframe)
            
            textExchange.exchangeIframe(i)

            with open("templates/index.html", 'r+') as f:
                text = f.read()
                newIframe = re.findall(r'(?:<iframe[^>]*)(?:(?:\/>)|(?:>.*?<\/iframe>))',text)
            #if the iframe was properly exchanged for a new one the oldIframe and newIframe variables will differe
            #therefore check the statment is false
            self.assertFalse(oldIframe == newIframe)


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
