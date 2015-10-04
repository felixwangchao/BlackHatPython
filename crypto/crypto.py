#!/usr/bin
# Filename: crypto.py

import random,os,sys,re

dict1 = {}
dict2 = {}


def genereDict():
    global dict1,dict2
    String = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    for val in  String:
        dict1[val] = i
        dict2[i] = val
        i= i+1

def enchiffrement(String,Key):
    global dict1,dict2
    crypto = ""
    for i in range(0,len(String)):       
        crypto = crypto + dict2[((dict1[String[i]]+dict1[Key[i]]) % 26)]
    
    return crypto    


def dechiffrement(key,crypto):
    global dict1,dict2
    clair = ""
    for i in range(0,len(key)):
        clair = clair + dict2[((26-dict1[key[i]])+dict1[crypto[i]])%26]
    print clair    
    return clair 
    



def genereKey(n):
    global dict1,dict2
    
    key = ""
    for i in range(0,n+1):
        key = key + dict2[random.randint(0,25)]

    return key

def Usage():
    print
    print
    print "Small application for cryptography"
    print "Usage: python crypto.py thereisagoogidea"
    print "Usage: python crypto.py tomorroweveningthereoclock"
    print
    print


def main():
    
    if len(sys.argv) < 2 or len(sys.argv)>2:
        Usage()
        sys.exit(0)
    

    m = re.search(r'[^a-z]+',sys.argv[1])

    if m:
        Usage()
        sys.exit(0)
    
    String = sys.argv[1]          
    genereDict()
    key = genereKey(len(String)-1)
    f = open("key.txt",'w')
    f.write(key)
    f.close()
    crypto = enchiffrement(String,key)
    print
    print "The crypto is:"
    print "============================"
    print crypto
    print "============================"

    while 1:
        input_key = raw_input("please input the key to dechiffre:")
        m = re.search(r'[^a-z]+',input_key)
        if m:
            print "key error"
            continue
        if len(input_key) != len(key):
            print "key error"
            continue
        if String == dechiffrement(input_key,crypto):
            print "key is right"
            break;
        else:
            print "key error" 
            continue
    
main()    



