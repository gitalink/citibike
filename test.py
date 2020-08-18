import sys
import csv

for line in csv.reader(sys.stdin):
	print(type(line))
	print(line)


def parse(thing):
	return thing

def stdin():
	while std_in_is_full:
		yield get_row_from_std_in()

def reader(iterable):
	for thing in iterable:
		yield parse(thing)