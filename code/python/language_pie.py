
import matplotlib.pyplot as plt
import numpy as np
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='011004',
    db='sakila_dwh',
    charset='utf8',
       # autocommit=True,    # 如果插入数据， 和conn.commit()功能一致。
)

cursor = conn.cursor()
# sql = "SELECT film_language,count(*) AS COUNT FROM sakila_dwh GROUP BY film_language ORDER BY COUNT DESC"

try:
    try:
        count_sqli = "SELECT film_language,count(*) AS COUNT FROM dim_film GROUP BY film_language ORDER BY COUNT DESC"
        cursor.execute(count_sqli)

    except Exception as e:
        print("连接数据表失败:", e)
    else:
        print("连接数据表成功;")
        info = cursor.fetchall()

except:
    print("!!!!!!!!!!!!!!!!!!!!")
conn.close()
a = np.array(info)
datax = a[:6,0]
datay = a[:6,1]
print(datax)
print(datay)
plt.figure(figsize=(9,9))
plt.pie(datay,labels=datax,autopct='%1.1f%%')
plt.title('film_language')

plt.show()


