Python操作MySQL数据库——pymysql
=
1、安装pymysql
-
```Python
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
```

·注意：存在中文的时候，连接需要添加charset='utf8'，否则中文显示乱码。·

2、获取查询数据
-
```Python
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
```
3、获取新创建数据自增ID
-
```python
import pymysql
  
con = pymysql.connect(host='localhost', port=3306, user='root', passwd='密码', db='库名')
cursor = con.cursor()
cursor.executemany("insert into hosts(name,name_id)values(%s,%s)", [("abc",1),("def",2)])
con.commit()
cursor.close()
con.close()
  
# 获取最新自增ID
new_id = cursor.lastrowid
```
