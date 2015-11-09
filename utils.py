#!/usr/bin/env python
# coding: utf-8

def multiplication_entiere(x, y):
	p = 0
	while y != 0:
		if (y & 0b1) == 1:
			p = p + x
		x = x << 1
		y = y >> 1
	return p

def produit(n, poly, x, y):
	p = 0
	while y != 0:
		if y & 0b1:
			p = p ^ x
		x = x << 1
		if x & (0b1 << n):
			x = x ^ poly
		y = y >> 1
	return p

def affiche_table_multiplicative(n, poly) :
	for i in range(1 << n) :
		for j in range(1 << n) :
			print produit(n, poly, i, j), 
		print

def exp(n, poly, x, k):
	res = x
	b = bin(k)[3:]
	for ki in b:
		res = produit(n, poly, res, res)
		if ki == "1":
			res = produit(n, poly, res, x)
	return res

def inverse(n, poly, x):
	k = (0b1 << n) - 2
	return exp(n, poly, x, k)

def subgroup(n, poly, x):
	res = [x]
	new_elem = x
	while new_elem != 1:
		new_elem = produit(n, poly, new_elem, x)
		res.append(new_elem)
	return res
