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
        count_sqli = "select dim_film.film_key, film_title, format(sum(rental_amount),2) total from dim_film inner join fact_rental on dim_film.film_key = fact_rental.film_key group by film_key order by sum(rental_amount) desc"
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
datax = a[:5,1]
datay1 = a[:5,2]
datay = [float(datay1[0]),float(datay1[1]),float(datay1[2]),float(datay1[3]),float(datay1[4]),]
print(datay)
plt.bar(datax,datay)
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False
plt.title('创收排名前五的电影营收额')
for a,b in zip(datax,datay):   #柱子上的数字显示
 plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=7);
plt.show()