import pymysql
 
con = pymysql.connect(host='loacalhost', port=3306, user='root', passwd='密码', db='库名')
cursor = con.cursor()
cursor.execute("select * from 表名")
 
# 获取剩余结果的第一行数据
row_1 = cursor.fetchone()

# 获取剩余结果前n行数据
row_2 = cursor.fetchmany(n)
 
# 获取剩余结果所有数据
row_3 = cursor.fetchall()
 
con.commit()
cursor.close()
con.close()
