#coding: utf-8
import pymysql
import xlsxwriter
from TelnetClient import TelnetClient

command = 'sh /app1/yn5301/sj/main/wj_hs/wj_1201.sh'
t =TelnetClient()
t.cmd_run(command)

workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet('sheet1')

worksheet.set_column('A:A',17)
worksheet.set_row(0,32)
a1format = workbook.add_format({
    'bold':     True,
    'font_size':18,  #字体大小
    'border':   1,
    'align':    'center',#水平居中
    'valign':   'vcenter',#垂直居中
    #'fg_color': '#D7E4BC',#颜色填充
})

worksheet.merge_range('A1:H1',u'截止12.5未决清理汇总',a1format)

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

sql = "select * from wj_hs where version = '1201'"# and inputtime = today -1"
print(sql)
#conn =pypyodbc.connect('DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=yndbsvr3;DATABASE=yn5301;UID=query;PWD=query333'\
#	,encoding='GBK',unicode_results=False)
conn =pymysql.connect('localhost','root','root','yunnanamiddb')
cr = conn.cursor()
#results = cr.execute(sql).fetchall()
cr.execute(sql)
results = cr.fetchall()
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
#print(results)
for rd in results:
    col2 = 0
        #print(rd)
	#print(rd[0].decode('gbk'))
	#worksheet.write(row2, col2,rd[0].decode('gbk').strip(),A4_format)
    if count < count_len -2 :
        worksheet.write(row2, col2,rd[0].strip(),A4_format)
        worksheet.write(row2, col2+1,rd[1],A4_format)
        worksheet.write(row2, col2+2,rd[2],A4_format)
        #print(str(row2)+'|'+str(col+1))
        cell = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+1)
        cell1 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+2)
        #print(str(row2)+'|'+str(col+2))
        #worksheet.write(row2, col2+3,rd[5],A4_format)
        worksheet.write_formula(row2,col2+3,'='+cell1+'/'+cell,A5_format)
        worksheet.write(row2, col2+4,rd[3],A4_format)
        worksheet.write(row2, col2+5,rd[4],A4_format)

        cell3 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+4)
        cell4 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+5)
        worksheet.write_formula(row2,col2+6,'='+cell4+'/'+cell3,A5_format)
        worksheet.write_formula(row2,col2+7,'='+'('+cell4+'+'+cell1+')'+'/'+'('+cell3+'+'+cell+')',A5_format)
    else:
        worksheet.write(row2, col2,rd[0].strip(),A6_format)
        worksheet.write(row2, col2+1,rd[1],A6_format)
        worksheet.write(row2, col2+2,rd[2],A6_format)
        #print(str(row2)+'|'+str(col+1))
        cell = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+1)
        cell1 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+2)
        #print(str(row2)+'|'+str(col+2))
        #worksheet.write(row2, col2+3,rd[5],A4_format)
        worksheet.write_formula(row2,col2+3,'='+cell1+'/'+cell,A7_format)
        worksheet.write(row2, col2+4,rd[3],A6_format)
        worksheet.write(row2, col2+5,rd[4],A6_format)

        cell3 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+4)
        cell4 = xlsxwriter.worksheet.xl_rowcol_to_cell_fast(row2, col2+5)
        worksheet.write_formula(row2,col2+6,'='+cell4+'/'+cell3,A7_format)
        worksheet.write_formula(row2,col2+7,'='+'('+cell4+'+'+cell1+')'+'/'+'('+cell3+'+'+cell+')',A7_format)

    #worksheet.write(row2, col2+6,rd[5],A4_format)

    row2 += 1
    count +=1
	#print(rd[0].decode('gbk').strip()+'|'+str(rd[1]))

#worksheet.write('A1',u'中文',bold)

workbook.close()
