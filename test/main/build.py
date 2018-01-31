from . import createname
from ..resource import phone
from . import change
from . import prefix_sure

#调用函数生成随机姓名与电话

def create1(chartype1,chartype2,f,l,s,str1):
    n = []
    for x in range(s): 
        name1 = createname.namelen1(chartype1,f)
        name2 = createname.namelen1(chartype2,l)
        n = phone.create_number(1)
        m1 = ''
        m2 = ''
       # print (name1)
        change.change_name(name1,name2,n,m1,m2,str1)    
def create2(chartype1,chartype2,f,l,s,str1):
    n = []
    for x in range(s): 
        name1 = createname.namelen1(chartype1,f)
        name2 = createname.namelen1(chartype2,l)
        n = phone.create_number(1)
        m1 = prefix_sure.create_fix(x,s)
        m2 = ''
       # print (name1)
        change.change_name(name1,name2,n,m1,m2,str1)  
def create3(chartype1,chartype2,f,l,s,str1):
    n = []
    #print (chartype)
    for x in range(s): 
        name1 = createname.namelen1(chartype1,f)
        name2 = createname.namelen1(chartype2,l)
        n = phone.create_number(1)
        m1 = prefix_sure.create_fix(x,s)
        m2 = prefix_sure.create_fix(x,s)
       # print (name1)
        change.change_name(name1,name2,n,m1,m2,str1)  
def create4(chartype1,chartype2,f,l,s,str1):
    n = []
    for x in range(s): 
        name1 = createname.namelen1(chartype1,f)
        name2 = createname.namelen1(chartype2,l)
        n = phone.create_number(1)
        m1 = ''
        m2 = prefix_sure.create_fix(x,s)
       # print (name1)
        change.change_name(name1,name2,n,m1,m2,str1)  