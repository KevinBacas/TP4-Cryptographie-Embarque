#!/usr/bin/env python
# coding: utf-8

from utils import multiplication_entiere, produit, affiche_table_multiplicative

if __name__ == '__main__':
	print "Hello world!"

	print "multiplication_entiere(2, 5) =", multiplication_entiere(2, 5)

	n = 8
	poly = (0b1 << 8) ^ (0b1 << 4) ^ (0b1 << 3) ^ (0b1 << 1) ^ 0b1
	print produit(n, poly, 45, 72)

	affiche_table_multiplicative(3, poly & 0b1111)
