import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='tester', password='',
                       db='testdb', charset='utf8')


# Connection 닫기
conn.close()