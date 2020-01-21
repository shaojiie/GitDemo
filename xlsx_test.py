#coding: utf-8
import xlsxwriter
import pypyodbc
import datetime
import telnetlib
from telnet_test import TelnetClient

#command = 'sh /app1/yn5301/sj/main/wj_hs/wj_1201.sh'
command = 'wc -l /app1/yn5301/sj/friday/bak/shenzhou/shenzhou_wj.csv'
print(command)
t =TelnetClient()
c_result = t.cmd_run(command)
print('============'+c_result)

yesterday = datetime.date.today() + datetime.timedelta(-1)
#print(yesterday2.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
month = yesterday.strftime("%m")
day = yesterday.strftime("%d")

name = '截止'+str(month)+'.'+str(day)+'未决清理汇总'
print(name)

workbook = xlsxwriter.Workbook(name+'.xlsx')
worksheet = workbook.add_worksheet('sheet1')

worksheet.set_column('A:A',17)
worksheet.set_row(0,20)
a1format = workbook.add_format({
    'bold':     True,
    'font_size':18,  #字体大小
    'border':   1,
    'align':    'center',#水平居中
    'valign':   'vcenter',#垂直居中
    #'fg_color': '#D7E4BC',#颜色填充
})

worksheet.merge_range('A1:H1',name,a1format)

b2_format = workbook.add_format({'align': 'center',
				    'valign': 'vcenter',
				    'border': 1,
				    'bold': True,
    				'font_size':14,
    				'font_name':'宋体'})

worksheet.merge_range('B2:D2',u'万元以下',b2_format)
worksheet.merge_range('E2:G2',u'万元以上',b2_format)
worksheet.set_column('H:H',10)
worksheet.merge_range('H2:H3',u'合计清理率',workbook.add_format({'align': 'center',
								   'valign': 'vcenter',
								   'border': 1,
								   'bold':     True,
    								'font_size':11}))

A3_format = workbook.add_format({'align': 'center',
				    'valign': 'vcenter',
				    'border': 1,
				    'bold': True,
    				'font_size':11,
    				'font_name':'宋体'})
worksheet.set_column('B:G',9)

expenses = ['片组','未决总数','清理数量','清理率','未决总数','清理数量','清理率']
# 从第一个单元格开始，行和列的索引均为0
row = 2
col = 0
# 迭代数据并逐行写入
for col in range(len(expenses)):
	worksheet.write(row, col,expenses[col],A3_format)
	col += 1

sql = "select * from wj_hs where version = '1201' and inputtime = today -1"
print(sql)
conn =pypyodbc.connect('DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=yndbsvr3;DATABASE=yn5301;UID=query;PWD=query333'\
	,encoding='GBK',unicode_results=False)

cr = conn.cursor()
results = cr.execute(sql).fetchall()
count_len = len(results)
row2 = 3
count = 0
A4_format = workbook.add_format({'align':'center',
'valign':'vcenter',
'border':1,
'font_size':11,
'font_name':'宋体'})

A5_format = workbook.add_format({'align':'center',
'valign':'vcenter',
'border':1,
'font_size':11,
'font_name':'宋体',
'num_format':'0.00%'})

A6_format = workbook.add_format({'align':'center',
'valign':'vcenter',
'bold':True,
'border':1,
'font_size':14,
'font_name':'宋体'})

A7_format = workbook.add_format({'align':'center',
'valign':'vcenter',
'bold':True,
'border':1,
'font_size':14,
'font_name':'宋体',
'num_format':'0.00%'})
for rd in results:
	col2 = 0
	if count < count_len -1:
		worksheet.write(row2, col2,rd[0].decode('GBK').strip(),A4_format)
		worksheet.write(row2, col2+1,rd[1],A4_format)
		worksheet.write(row2, col2+2,rd[2],A4_format)

		cell = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+1)
		cell1 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+2)

		worksheet.write_formula(row2,col2+3,'='+cell1+'/'+cell,A5_format)
		worksheet.write(row2, col2+4,rd[3],A4_format)
		worksheet.write(row2, col2+5,rd[4],A4_format)

		cell3 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+4)
		cell4 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+5)
		worksheet.write_formula(row2,col2+6,'='+cell4+'/'+cell3,A5_format)
		worksheet.write_formula(row2,col2+7,'='+'('+cell4+'+'+cell1+')'+'/'+'('+cell3+'+'+cell+')',A5_format)

	else:
		sz_total = rd[1] + rd[3]
		sz_done = rd[2] + rd[4]

		worksheet.write(row2, col2,u'车险分部合计',A6_format)
		worksheet.write_formula(row2, col2+1,'=SUM(B4:B14)',A6_format)
		worksheet.write_formula(row2, col2+2,'=SUM(C4:C14)',A6_format)
		#worksheet.write(row2, col2+1,rd[1],A6_format)
		#worksheet.write(row2, col2+2,rd[2],A6_format)

		cell = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+1)
		cell1 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+2)

		worksheet.write_formula(row2,col2+3,'='+cell1+'/'+cell,A7_format)
		worksheet.write_formula(row2, col2+4,'=SUM(E4:E14)',A6_format)
		worksheet.write_formula(row2, col2+5,'=SUM(F4:F14)',A6_format)

		cell3 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+4)
		cell4 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+5)
		worksheet.write_formula(row2,col2+6,'='+cell4+'/'+cell3,A7_format)
		worksheet.write_formula(row2,col2+7,'='+'('+cell4+'+'+cell1+')'+'/'+'('+cell3+'+'+cell+')',A7_format)
	row2 += 1
	count +=1
worksheet.write(row2, col2,u'总计',A6_format)
worksheet.write_formula(row2, col2+1,'=SUM(B4:B27)',A6_format)
worksheet.write_formula(row2, col2+2,'=SUM(C4:C27)',A6_format)
#worksheet.write(row2, col2+1,rd[1],A6_format)
#worksheet.write(row2, col2+2,rd[2],A6_format)

cell = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+1)
cell1 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+2)

worksheet.write_formula(row2,col2+3,'='+cell1+'/'+cell,A7_format)
worksheet.write_formula(row2, col2+4,'=SUM(E4:E27)',A6_format)
worksheet.write_formula(row2, col2+5,'=SUM(F4:F27)',A6_format)

cell3 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+4)
cell4 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+5)
worksheet.write_formula(row2,col2+6,'='+cell4+'/'+cell3,A7_format)
worksheet.write_formula(row2,col2+7,'='+'('+cell4+'+'+cell1+')'+'/'+'('+cell3+'+'+cell+')',A7_format)

A30_format = workbook.add_format({'align':'left',
'valign':'vcenter',
'border':1,
'font_size':11,
'font_name':'宋体'})

beizhu = '备注：核未决总件数：'+str(sz_total)+'，清理'+str(sz_done)+'件'
worksheet.merge_range('A30:H30',beizhu,A30_format)

workbook.close()
