import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='oracle', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()

## 6.3.4~5 책으로 확인.
