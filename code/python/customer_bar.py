import matplotlib.pyplot as plt
import numpy as np
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='011004',
    db='sakila_dwh',
    charset='utf8',
)

cursor = conn.cursor()


try:
    try:
        count_sqli = "SELECT customer_country,count(*) AS COUNT FROM dim_customer GROUP BY customer_country ORDER BY COUNT DESC LIMIT 10"
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
datax = a[:, 0]
datay = a[:, 1]
print(datax)
print(datay)
plt.bar(datax, datay)
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False
plt.title('各个国家的客户数（排名前十）')
plt.show()
