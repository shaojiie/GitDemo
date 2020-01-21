import pandas as pd
import time

start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
t1 = time.time()
pd.set_option('display.max_columns', 500)
#pd.options.display.maxcolum = 99
#sheetname = "Sheet2"

def isNumber(x):
	#if isinstance(x,(int,float)):
	if isinstance(x,int):
		print("iiiiiiiii")
		return x
	if isinstance(x,str):
		return 0

def is_number(s):
	# if len(s) > 0:
	# 	return True
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False

sheetname = "已认证"
people = pd.read_excel('kd.xlsx',sheet_name=sheetname)
people.replace('\s+','',regex=True,inplace=True)
#people.columns = ['a','b','c','d','e','f','g','h']
#people.columns = ['a','b','c','d','e ','f','g','h','i','j','k','l','m']
people.columns = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
print(people.dtypes)
#print(people.iloc[0:3,0:3])
print(people.head())
print('isisissisisisisissisisisis')
people.e= people.e.fillna('0')
print(people['e'])
people['x'] = people['f'].map(is_number)
#loandata['emp_length'].apply(lambda x: x. isdigit ())
#pl = people['e'].map(isNumber)
print('plplplplplplplplplplplplplpl')
pl = people[ ~people['g'].map(is_number)]
print(people.loc[0:20,])
print(pl.loc[0:20,])
print(people.groupby('b')['f','g'].sum())

'''
#print(people.iloc[4,:])  data.groupby('race')['signs_of_mental_illness'].value_counts()
#print (people.groupby(by='b').sum())
print('------------------------------')
print(people.groupby('a')['e','f'].sum())
print('------------------------------')
#people['f'] = people['f'].str.strip()
groups = people.groupby(['a'])
print("gggggggggggggggggg")
#print(groups['e'])
s = groups['e'].sum()
s2 = groups['f'].sum()
print("gggggggggggggggggg")

pt2 = pd.DataFrame({'ee':s,'ff':s2})
print(pt2)
#people.dropna(subset=['f'])
#people['f'] = people['f'].astype('float32')

#print (people.groupby(by='b').agg({'f':sum,'g':sum}).reset_index())
print (people.groupby(by='a').agg({'e':sum,'f':sum}).reset_index())

print('people.columns[4]')
print('hhhhhhhhhhhhh')
print(people.head())

end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
t2 = time.time()


print(time.strftime('%H:%M:%S',time.localtime(t2-t1)))
'''