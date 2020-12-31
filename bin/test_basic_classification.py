"""Test basic_classification file
"""
from basic_classification import basic_classification

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-12-30"

def test():
	"""Tests the basic_classification function in the basic_classification class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert basic_classification() != "", "test failed"
	#assert basic_classification.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
