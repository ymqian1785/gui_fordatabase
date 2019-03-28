import cx_Oracle
import sys
import csv
import time
import os

# conn= cx_Oracle.connect('TJOCR/TJOCR@127.0.0.1/orcl')
# conn= cx_Oracle.connect('airport/jcfj2017@10.92.172.110:1521/orcl')
# conn = cx_Oracle.connect('airport','jcfj2017','10.92.172.110:1521/orcl')
conn = cx_Oracle.connect('TJOCR','TJOCR','127.0.0.1/orcl')

cursor = conn.cursor()
# cursor.execute("select *, ROW_NUMBER() over(order by NAME) as rows from PSG_AJ_ZC where PASSENGERNO ='TSN2014_20181107173702351'")
# cursor.execute("select ROW_NUMBER() over(partition by NAME order by insDT) as rows, * from PSG_AJ_OCR where insDT='王真'")
# cursor.execute("select ROW_NUMBER() over(partition by NAME order by NAME) as rows, IDCARD from PSG_AJ_OCR where NAME='王真'")
# cursor.execute("select * from（select * from PSG_AJ_OCR order by NO desc）where rownum=1 AND PASSENGERNO ='TSN2014_20181107173702351'")
cursor.execute("select * from（select * from PSG_AJ_ZC order by ID desc）where INTIME>=to_date('2018-11-07 00:00:00','yyyy-mm-dd hh24:mi:ss')and INTIME<=to_date('2018-11-08 00:00:00','yyyy-mm-dd hh24:mi:ss'）")
# rownum=1 AND
cursor.execute("select * from（select * from PSG_AJ_ZC order by ID desc）where INTIME>=to_date('2018-11-07 00:00:00','yyyy-mm-dd hh24:mi:ss')and INTIME<=to_date('2018-11-08 00:00:00','yyyy-mm-dd hh24:mi:ss'）")
cursor.execute("select * from PSG_AJ_ZC where id=(select c.p from (select id,lag(id,1,0)  over (order by apply_date) as p from t_company_apply) c where c.id='ae2e829ecffd4715a5c163f829c2e0f5')")


one = cursor.fetchall()
print(one)
for rec in one:
    print (rec[0])
    print('输出成功')

# now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# fname="E:/"+now+r".csv"
# outputFile = open (fname,"w")
#
# output = csv.writer(outputFile, dialect='excel')
# cursor.execute("select * from PSG_AJ_OCR where PASSENGERNO ='TSN2014_20181107173702351'")
#
# cols=[]
# for col in cursor.description:
#     cols.append(col[0])
# output.writerow(cols)
#
# for row in cursor:
#     output.writerow(row)
#
# outputFile.close

cursor.close()
conn.close()





