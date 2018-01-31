from ..resource import character

#判断姓名的长度是否为1、3、5、13，以此判断调用混合或单一类型的字符

def namelen1(chartype,i):
    if chartype == 1 or chartype == 3 or chartype == 5 or chartype == 13:
        #print (chartype)
        name = character.create_signle_type(chartype,i)
        return name
    else:
        #print (chartype)
        #print (i)
        name = character.create_mix_type(chartype,i)
        #print (name)
        return name