import pymysql
  
con = pymysql.connect(host='localhost', port=3306, user='root', passwd='密码', db='库名')
cursor = con.cursor()
cursor.executemany("insert into hosts(name,name_id)values(%s,%s)", [("abc",1),("def",2)])
con.commit()
cursor.close()
con.close()
  
# 获取最新自增ID
new_id = cursor.lastrowid
