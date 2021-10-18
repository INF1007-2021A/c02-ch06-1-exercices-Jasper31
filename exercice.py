#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	max_liste = []
	for liste in numbers:
		max_liste.append(max(liste))
	return max_liste

def join_integers(numbers):
	return ''.join([str(elem) for elem in numbers])

def generate_prime_numbers(limit):
	prime = []
	numbers = list(range(2,(limit+1)))
	while len(numbers) != 0:
		prime.append(numbers[0])
		numbers = [values for values in numbers if values % numbers[0] != 0]
	return prime

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	combined = []
	numbers = list(range(1,num_combinations + 1))
	if excluded_multiples != None:
		numbers = [values for values in numbers if values % excluded_multiples != 0]
	for values in numbers:
		for elem in strings:
			combined.append(elem + str(values))
	return combined

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
