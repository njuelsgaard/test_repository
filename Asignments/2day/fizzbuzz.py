#!/usr/bin/env pthon

def fizzbuzz(s):
  if s %3 ==0 and s % 5 == 0:
    return "fizzbuzz"
  if s % 3 == 0:
    return "fizz"
  if s %5 == 0:
    return "buzz"
  return s