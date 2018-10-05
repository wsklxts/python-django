import pymysql

def con():
    return  pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='ll',
                           charset='utf8')

def change(sql,arg):
    conn = con()
    cursor = conn.cursor()
    try:
        cursor.execute(sql,arg)
        conn.commit()  # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
    except Exception as e:
        return False
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return True
def manyChange(sql,arg):
    conn = con()
    cursor = conn.cursor()
    try:
        cursor.executemany(sql,arg)
        conn.commit()  # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
    except Exception as e:
        return False
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return True

def view(sql, arg):
    conn = con()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, arg)
    result = cursor.fetchall()
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result