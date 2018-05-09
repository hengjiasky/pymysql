import pymysql
  
# 创建连接，当连接本地服务器时host='localhost'优于host='127.0.0.1'
con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='密码', db='库名'，charset='utf8')
# 创建游标
cursor = db.cursor()
  
# 使用execute方法执行SQL语句
effect_row = cursor.execute("select * from 表名")
# 提交，不然无法保存新建或者修改的数据 
con.commit() 

# 关闭游标 
cursor.close() 

# 关闭数据库连接 
con.close()
