#encoding=utf-8
import pymysql
def setSql(ip,user,pw):
    conn = pymysql.connect(ip, user, pw,charset='utf8')
    return conn
def getSql(db, sql,conn):
    with conn.cursor() as cursor:
        cursor.execute('USE {}'.format(db))
        cursor.execute(sql)
        result = cursor.fetchall()
        list_result = []
        for i in result:
            list_result.append('{}'.format(i[0]))
    return list_result
def getClients(db, sql, conn, ports_num):
    with conn.cursor() as cursor:
        cursor.execute('USE {}'.format(db))
        cursor.execute(sql)
        result = cursor.fetchall()
        list_result = []
        for i in result:
            list_result.append('端口：{},名字：{},email：{}'.format(ports_num[0],i[0],i[1]))
    return list_result
inport = input("Enter port,use ',' split: ")
ports = inport.split(',')
conn = setSql("sql.ggg.moe", "root", "3396959")
sql1 = "SELECT sid FROM user WHERE port in({})".format(inport)
sql2 = "SELECT userid FROM tblhosting WHERE id in({})"
sql3 = "SELECT firstname,email FROM tblclients WHERE id in({})"
list_result = getSql("shadowsocksoz",sql1,conn)
list_result = getSql("whmcs",sql2.format(','.join(list_result)),conn)
list_result = getClients("whmcs",sql3.format(','.join(list_result)),conn,ports)
for i in list_result:
    print(''.join(list_result[0]))



