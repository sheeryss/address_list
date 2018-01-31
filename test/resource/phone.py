import random

#随机生成电话号码函数

def create_number(i): 
    arr = []
    for i in range(21):
        area_num = ['187','186','158','155','156','155','152','151','134','135','136','137','138','139','131','130','133','153']
        area_number = random.choice(area_num)  #随机生成号码的三位数开头

        seed = '1234567890'
        sa = []
        for i in range(8):
            sa.append(random.choice(seed)) #随机生成号码后8位
        last_num = "".join(sa)

        num = area_number + last_num
        arr.append(num)
    #print (num)
    #print (arr)
    return arr
