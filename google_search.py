# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:46:24 2023

@author: Abdur Rahman F R
"""

try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")


# to search
query = "Abdur Rahman F R"


for j in search(query, tld="co.in", num=5, stop=5, pause=2):
	print(j)