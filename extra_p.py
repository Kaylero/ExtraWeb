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
		""" Get the html """
		f = urllib2.urlopen(web)
		html = f.read()
		f.close()
		return html

	def get_book(self, html):
		""" Get the name of the book """
		soup = BeautifulSoup(html, 'html.parser')
		element = soup.find("div", "dotd-title").text
		return element.strip()

	def print_book_name(self, name):
		""" This function prints the book name. Yes it does """
		print "Look at this sale: '" + str(name) + "' TOTALLY FREE."

	def run(self):
		html =self.get_web(
			"https://www.packtpub.com/packt/offers/free-learning/")
		element = self.get_book(html)
		self.print_book_name(element)

if __name__ == "__main__":
	client = client()
	client.run()