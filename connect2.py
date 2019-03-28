import cx_Oracle
import sys
import csv
import time
import os


conn = cx_Oracle.connect('TJOCR','TJOCR','127.0.0.1/orcl')

cursor = conn.cursor()
cursor.execute("select * from PSG_AJ_OCR where PASSENGERNO ='TSN2014_20181107173702351'")
# cursor.execute("select ROW_NUMBER() over(partition by NAME order by insDT) as rows, * from PSG_AJ_OCR where insDT='王真'")
# cursor.execute("select ROW_NUMBER() over(partition by NAME order by NAME) as rows, IDCARD from PSG_AJ_OCR where NAME='王真'")
# cursor.execute("select * from PSG_AJ_OCR e,PSG_AJ_ZC d where e.PASSENGERNO=d.PASSENGERNO AND rownum=1 and e.PASSENGERNO ='TSN2014_20181105072657715'")

one = cursor.fetchall()
print(one)

for rec in one:
    print (rec[0])
    print(type(rec[15]))
    print(type(rec[17]))
    print('输出成功')