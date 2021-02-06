# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:09:10 2021

@author: Thomas Stocks
"""

class motec_data:
    def __init__(self, file_path):
        """
        A wrapper for Gotzl's ldparser designed to simplify the import process for this repository and its tools. 
        
        REQUIREMENTS: ldparser.py must be in the python path (https://github.com/gotzl/ldparser.git)
        
        INPUTS: file_path (str) a path to the MoTeC file to be processed and analyzed
        """
        from ldparser import ldData
        
        self.file_path = file_path
        self.ld_object = ldData.fromfile(file_path)
        