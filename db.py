__author__ = 'Administrator'
#db for python
import  MySQLdb
conn = MySQLdb.connect(
    host='61.130.144.194',
    user='qmrgame',
    passwd='Qmrgame925833',
    db='serverlist',
    port=5849,
    charset='utf8')
print conn
def mysql():
    cxn = conn.cursor()
    sql = '''select * from gameserverinfo'''
    cxn.execute(sql)
    r1 = cxn.fetchone()
    print r1
    cxn.close()
    conn.close()
if __name__ == '__main__':
    mysql()


