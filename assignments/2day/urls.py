#!/usr/bin/env python

'''
    This program will take a filepath and return a specified number of urls

'''


import sys
import random
import argparse

parser = argparse.ArgumentParser(description = "This program returns a chosen number of urls",
                                       usage = "return_urls",
                                      epilog = "this is the epilog")

parser.add_argument('-f','--file', help="file to open", required=True)
parser.add_argument('-l','--lines', help="number of lines to return", type=int, required=True)
args = parser.parse_args()

print(len(sys.argv))

if len(sys.argv[1:])==0:
  print()
  parser.print_help()
  print()
  parser.exit()

#filepath = r"C:\Users\njuelsgaard\Desktop\SciCoder\SciCoder-2019-Keck\Data Files\sdss_spectra_links.txt"
#number_randoms = 20;
#f = open(filepath)
#urls = f. readlines()
#f.close()

with open(args.file) as file:
    urls = file.readlines()

number_randoms = int(args.lines)
assert number_randoms<len(urls), "Number requested larger than number of files"
randurls = list()

for i in range(number_randoms):
  randurls.append(urls.pop(random.randint(0,len(urls))))

print("\n"+"\n")
for url in randurls:
  print(url)