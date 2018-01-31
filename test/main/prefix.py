#!/usr/bin/python
from . import build

#判断所需要的前缀类型（“nn”：姓与名前缀都不要，“yy”姓与名前缀都要，“yn”只要姓的前缀，“ny”只要名的前缀）

def prefix(chartype1,chartype2,ans,f,l,size,str1):  
    #print (chartype)
    if ans == 'yn':
        build.create2(chartype1,chartype2,f,l,size,str1)
    elif ans == 'nn':
        build.create1(chartype1,chartype2,f,l,size,str1)
    elif ans == 'yy':
        build.create3(chartype1,chartype2,f,l,size,str1)
    elif ans == 'ny':
        build.create4(chartype1,chartype2,f,l,size,str1)
    else :
        return ''