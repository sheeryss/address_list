import string 

#在前缀的构建
def create_fix(x,size):
    l1 = str(x)
    l2 = str(size)
    m = len(l2)
    s = l1.zfill(m)
    
    return s