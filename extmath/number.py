# Description:
# number.py contains number theory related
# functions
# 
# Author:
# Calvin Yeung (dbydt)

from math import sqrt
from sys import setrecursionlimit

# set recursion limit of gcd function
setrecursionlimit(100000)

# checks if number is prime
def is_prime(n):
	if n <= 1:
		return False
	if n == 2:
		return True
	for x in [2] + range(3, int(sqrt(n) + 1), 2):
		if n % x == 0:
			return False
	return True

# check if two numbers have any common factors	
def is_relatively_prime(m, n):
	return gcd(m, n) == 1

# returns the next prime after the given number
def next_prime(n):
	while True:
		n += 1
		if is_prime(n):
			return n

# returns a list of all primes less than n		
def prime_list(n):
	p = []
	for x in range(n):
		if is_prime(x):
			p.append(x)
	return p

# returns the prime factorization of a number
def prime_factors(n):
	p = []
	num = 2
	count = 0
	added = False
	
	while n != 1 or not added:
		if n % num == 0:
			n /= num
			count += 1
			added = False
		else:
			if count > 0:
				p.append((num, count))
				count = 0
				added = True
				
			num = next_prime(num)
	
	return p

# returns the greatest common denominator of two numbers
def gcd(m, n):
	if n == 0:
		return m
	return gcd(n, m % n)
	