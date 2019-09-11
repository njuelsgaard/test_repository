#!/usr/bin/env python

from fizzbuzz import fizzbuzz

def test_fizz_for1():
  assert fizzbuzz(1) == 1, "fizzbuzz(1) doesn't equal 1"
  
def test_fizz_for2():
  assert fizzbuzz(2) == 2, "fizzbuzz(2) doesn't equal 2"
  
def test_fizz_for3():
  assert fizzbuzz(3) == "fizz", "fizzbuzz(3) doesn't equal fizz"
  
def test_fizz_for4():
  assert fizzbuzz(4) == 4, "fizzbuzz(4) doesn't equal 4"
  
def test_fizz_for5():
  assert fizzbuzz(5) == "buzz", "fizzbuzz(5) doesn't equal buzz"
  
def test_fizz_for6():
  assert fizzbuzz(6) == "fizz", "fizzbuzz(6) doesn't equal fizz"
  
def test_fizz_for7():
  assert fizzbuzz(7) == 7, "fizzbuzz(7) doesn't equal 7"
  
def test_fizz_for8():
  assert fizzbuzz(8) == 8, "fizzbuzz(8) doesn't equal 8"

def test_fizz_for9():
  assert fizzbuzz(9) == "fizz", "nope"

def test_fizz_for10():
  assert fizzbuzz(10) == "buzz", "nope"

def test_fizz_for11():
  assert fizzbuzz(11) == 11, "nope"

def test_fizz_for12():
  assert fizzbuzz(12) == "fizz", "nope"

def test_fizz_for13():
  assert fizzbuzz(13) == 13, "nope"

def test_fizz_for14():
  assert fizzbuzz(14) == 14, "nope"

def test_fizz_for15():
  assert fizzbuzz(15) == "fizzbuzz", "nope"

def test_fizz_for16():
  assert fizzbuzz(16) == 16, "nope"

def test_fizz_for17():
  assert fizzbuzz(17) ==17, "nope"

def test_fizz_for18():
  assert fizzbuzz(18) == "fizz", "nope"

def test_fizz_for19():
  assert fizzbuzz(19) == 19, "nope"