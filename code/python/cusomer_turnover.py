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
        count_sqli = "select dim_staff.staff_key, staff_first_name, format(sum(rental_amount),2) total from dim_staff inner join fact_rental on dim_staff.staff_key = fact_rental.staff_key group by staff_key order by sum(rental_amount) desc"
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
print(a)
datax = a[:,1]
datay = a[:,2]
datay1 = [float(datay[0].replace(',','')),float(datay[1].replace(',',''))]
plt.bar(datax, datay1)
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False
plt.title('各个职员的营业额')
plt.show()