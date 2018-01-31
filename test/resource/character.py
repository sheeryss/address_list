# -*- coding: utf-8 -*-
import random

CHAR_TYPE = {'CHINESE': 1, 'ENGLISH': 3, 'NUMBER': 5, 'SYMBOL': 13}

def chinese():
    """
        随机创建单个中文字符
    """
    val = random.randint(0x4e00, 0x9fbf)
   
    return chr(val)
def english():
    """
        随机创建单个英文字符
    """
    # pylint: disable=C0301
    englishs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return englishs[random.randint(0, len(englishs) - 1)]

def number():
    """
        随机创建单个数字字符
    """
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return numbers[random.randint(0, len(numbers) - 1)]

def symbol():
    """
        随机创建单个符号字符
    """
    # pylint: disable=C0301
    symbols = [' ', '!', '"', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    return symbols[random.randint(0, len(symbols) - 1)]

def create_english(size):
    """
        随机创建size个英文字符
    """
    result = ''
    # pylint: disable=W0612
    for index in range(size):
        result = result + english()
    return result

def create_chinese(size):
    """
         随机创建size个中文字符
    """
    result = ''
    # pylint: disable=W0612
    for index in range(size):
        result = result + chinese()
    return result
    print (result)
def create_number(size):
    """
         随机创建size个数字字符
    """
    result = ''
    # pylint: disable=W0612
    for index in range(size):
        result = result + number()
    return result

def create_symbol(size):
    """
         随机创建size个符号字符
    """
    result = ''
    # pylint: disable=W0612
    for index in range(size):
        result = result + symbol()
    return result

def create_signle_type(chartype, size):
    """
        根据chartype类型创建size个字符
    """
    #result = ''
    ''' print "char type is " + str(chartype) '''
    # pylint: disable=W0612
    for index in range(size):
        if chartype ==CHAR_TYPE['CHINESE']:
            result = create_chinese(size)
        elif chartype == CHAR_TYPE['ENGLISH']:
            result = create_english(size)
        elif chartype == CHAR_TYPE['NUMBER']:
            result = create_number(size)
        elif chartype == CHAR_TYPE['SYMBOL']:
            result = create_symbol(size)
        else:
            result = ''
    return result

def create_mix_type(chartype, size):
    """
        根据chartype类型（多个）创建size个字符
    """
    """print "mix char type is " + str(chartype)"""
    result = ''
    if chartype == CHAR_TYPE["CHINESE"] + CHAR_TYPE["ENGLISH"]:
        result = get_char_from_pool(size, CHAR_TYPE["CHINESE"], CHAR_TYPE["ENGLISH"])
    elif chartype == CHAR_TYPE["CHINESE"] + CHAR_TYPE["NUMBER"]:
        result = get_char_from_pool(size, CHAR_TYPE["CHINESE"], CHAR_TYPE["NUMBER"])
    elif chartype == CHAR_TYPE["CHINESE"] + CHAR_TYPE["SYMBOL"]:
        result = get_char_from_pool(size, CHAR_TYPE["CHINESE"], CHAR_TYPE["SYMBOL"])
    elif chartype == CHAR_TYPE["ENGLISH"] + CHAR_TYPE["NUMBER"]:
        result = get_char_from_pool(size, CHAR_TYPE["ENGLISH"], CHAR_TYPE["NUMBER"])
    elif chartype == CHAR_TYPE["ENGLISH"] + CHAR_TYPE["SYMBOL"]:
        result = get_char_from_pool(size, CHAR_TYPE["ENGLISH"], CHAR_TYPE["SYMBOL"])
    elif chartype == CHAR_TYPE["NUMBER"] + CHAR_TYPE["SYMBOL"]:
        result = get_char_from_pool(size, CHAR_TYPE["NUMBER"], CHAR_TYPE["SYMBOL"])
    elif chartype == CHAR_TYPE["CHINESE"] + CHAR_TYPE["ENGLISH"] + CHAR_TYPE["NUMBER"]:
        # pylint: disable=C0301
        result = get_char_from_pool(size, CHAR_TYPE["CHINESE"], CHAR_TYPE["ENGLISH"], CHAR_TYPE["NUMBER"])
    elif chartype == CHAR_TYPE["CHINESE"] + CHAR_TYPE["ENGLISH"] + CHAR_TYPE["SYMBOL"]:
        # pylint: disable=C0301
        result = get_char_from_pool(size, CHAR_TYPE["CHINESE"], CHAR_TYPE["ENGLISH"], CHAR_TYPE["SYMBOL"])
    elif chartype == CHAR_TYPE["CHINESE"] + CHAR_TYPE["NUMBER"] + CHAR_TYPE["SYMBOL"]:
        # pylint: disable=C0301
        result = get_char_from_pool(size, CHAR_TYPE["CHINESE"], CHAR_TYPE["NUMBER"], CHAR_TYPE["SYMBOL"])
    elif chartype == CHAR_TYPE["ENGLISH"] + CHAR_TYPE["NUMBER"] + CHAR_TYPE["SYMBOL"]:
        # pylint: disable=C0301
        result = get_char_from_pool(size, CHAR_TYPE["ENGLISH"], CHAR_TYPE["NUMBER"], CHAR_TYPE["SYMBOL"])
    # pylint: disable=C0301
    elif chartype == CHAR_TYPE["CHINESE"] + CHAR_TYPE["ENGLISH"] + CHAR_TYPE["NUMBER"] + CHAR_TYPE["SYMBOL"]:
        result = get_char_from_pool(size, CHAR_TYPE["CHINESE"], CHAR_TYPE["ENGLISH"], CHAR_TYPE["NUMBER"], CHAR_TYPE["SYMBOL"])
    else:
        pass
    return result

def get_char_from_pool(size, *types):
    """
        从字符串池中取数据
    """
    result = ''
    charspool = setpool(size, *types)
    # pylint: disable=C0103
    # pylint: disable=W0612
    for x in range(size):
        result = result + charspool[random.randint(0, len(charspool) - 1)]
    return result


def setpool(size, *types):
    """
        根据*types类型创建字符池
    """
    result = []
    # pylint: disable=C0103
    for x in types:
        # pylint: disable=W0612
        for j in range(size * 100):
            result.append(create_signle_type(x, 1))
    return result


#print (create_mix_type(CHAR_TYPE["CHINESE"] + CHAR_TYPE["ENGLISH"] + CHAR_TYPE["NUMBER"] + CHAR_TYPE["SYMBOL"],  122))
