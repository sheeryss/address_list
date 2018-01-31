from test.main import prefix
import time 

#主界面输入
#1.第一行输入“nn”：姓与名前缀都不要，“yy”姓与名前缀都要，“yn”只要姓的前缀，“ny”只要名的前缀
#2.第二行输入想要生成姓的长度
#3.第三行输入想要生成名的长度
#4.第四行输入想要生成多少个联系人
#5.第五行输入姓名的字符组合数（'CHINESE': 1, 'ENGLISH': 3, 'NUMBER': 5, 'SYMBOL': 13），取需要字符的数字相加。

print('----------使用说明------------')
print ('此程序用于生成随机数量、不同字符类型和长度的联系人，具体参数及使用步骤如下：')
print('1.第一行判断姓前面是否加序号，是填y，否填n')
print('2.第二行判断名前面是否加序号，是填y，否填n')
print('3.第三行输入想要生成姓的长度')
print('4.第四行输入想要生成名的长度')
print('5.第五行输入想要生成多少个联系人')
print('6.第六行联系人的名字需要什么格式?（中文输入1, 英文输入3, 数字输入5, 符号输入13）若是组合取对应的的数字相加。')
print('是否阅读清楚?(请输入 y/n)')

an = input()
if an == 'y':
    print ('姓是否需要前缀序号?(y/n)')
    ans1 = input()
    print ('名是否需要前缀序号?(y/n)')
    ans2 = input()
    print ('姓需要多长字符?')
    f = int(input())
    print ('联系人的姓需要什么格式?（中文: 1, 英文: 3, 数字: 5, 符号: 13）若是组合取对应的的数字相加。')
    chartype1 = int(input())
    print ('名需要多长字符?')
    l = int(input())
    print ('联系人的名需要什么格式?（中文: 1, 英文: 3, 数字: 5, 符号: 13）若是组合取对应的的数字相加。')
    chartype2 = int(input())
    print ('需要生成多少联系人?')
    s = int(input())
    print('输入生成的文件名：')
    str1 = input()
    ans = ans1 + ans2
    prefix.prefix(chartype1,chartype2,ans,f,l,s,str1)
    #print (chartype)
else:
    print('请联系工作人员，联系方式90909098')
    time.sleep(3)
    print('请重新启动程序')
    time.sleep(3)



