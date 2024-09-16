import pymysql

# 建立数据库连接
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit = True
)

try:
    # 获取服务器信息
    print(conn.get_server_info())
    duixiang = conn.cursor()   #创建游标对象
    conn.select_db("zje")   #选择数据库
    duixiang.execute("select id,name,age from student;")
    result = duixiang.fetchall()

    for row in result:
        dict = {}
        dict["id"] = row[0]
        dict["name"] = row[1]
        dict["age"] = row[2]
        print(dict)

finally:
    # 关闭数据库连接
    conn.close()