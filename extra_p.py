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


class client():
	def get_web(self, web):
		"""Gets the html"""
		f = urllib2.urlopen(web)
		html = f.read()
		f.close()
		return html

	def get_book(self):
		pass

	def run(self):
		html =self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
		print html
		pass
		# Get the name of the book
		# Print the name


if __name__ == "__main__":
	client = client()
	client.run()