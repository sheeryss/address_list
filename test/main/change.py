import string
import codecs

#转化成标准联系人格式并保存
number = []
def change_name(last_name,first_name,number,prefix1,prefix2,str1):
	i1 = str(prefix1)
	i2 = str(prefix2)
	s = ['BEGIN:VCARD','VERSION:3.0',
	"FN:" + i2 + first_name + ' ' + i1 + last_name,
	'TEL;TYPE=HOME:'+number[0],'TEL;TYPE=CELL:'+number[1],
	'TEL;TYPE=WORK:'+number[2],"TEL;TYPE=WORK;TYPE=FAX:" + number[3],
	"TEL;TYPE=HOME;TYPE=FAX:" + number[4],"TEL;TYPE=PAGER:" + number[5],
	"TEL;TYPE=OTHER:" + number[6],"TEL;TYPE=CALLBACK:" + number[7],
	"TEL;TYPE=CAR:" + number[8],"TEL;TYPE=COMPANY_MAIN:" + number[9],
	"TEL;TYPE=ISDN:" + number[10],"TEL;TYPE=MAIN:" + number[11],
	"TEL;TYPE=OTHER_FAX:" + number[12],"TEL;TYPE=RADIO:" + number[13],
	"TEL;TYPE=TELEX:" + number[14],"TEL;TYPE=TTY_TDD:" + number[15],
	"TEL;TYPE=WORK_MOBILE:" + number[16],"TEL;TYPE=WORK_PAGER:" + number[17],
	"TEL;TYPE=ASSISTANT:" + number[18],"TEL;TYPE=MMS:" + number[19],
	"TEL;TYPE=self define:" + number[20],'X-WDJ-STARRED:0','END:VCARD'
	]
	with codecs.open(str1+'.vcf','a','utf-8') as fp:
		for i in range(26):
			fp.write(s[i] + '\n')
	
	fp.close()