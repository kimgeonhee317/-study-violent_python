#!/bin/python 
import crypt

string1 = 'HX' #salt
string2 = 'egg' #plain text
print(crypt.crypt(string2, string1)) #Hash digested
 