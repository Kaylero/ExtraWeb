#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web for www.packtpub.com/packt/offers/free-learning/

It gives you the name of the book in sale today.

@author pedrocalero@ieslallitera.com
'''

import sys
import argparse
import urllib2
from bs4 import BeautifulSoup
import re


class client():
	def get_web(self, web):
		"""Gets the html"""
		f = urllib2.urlopen(web)
		html = f.read()
		f.close()
		return html

	def get_book(self, html):
		""" Get the name of the book"""
		soup = BeautifulSoup(html, 'html.parser')
		elements = str(soup.find_all("div", "dotd-title"))
		return elements

	def get_name(self, element):
		items = element.split("\\t")
		for item in items:
			if "[" not in item and "]" not in item and item != "":
				return item

	def print_book_name(self, name):
		print "Look at this sale: '" + str(name) + "' Totally FREE."

	def run(self):
		html =self.get_web(
			"https://www.packtpub.com/packt/offers/free-learning/")
		element = str(self.get_book(html))
		
		name =self.get_name(element)
		self.print_book_name(name)


if __name__ == "__main__":
	client = client()
	client.run()