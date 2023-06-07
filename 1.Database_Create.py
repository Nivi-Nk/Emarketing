#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgitb

cgitb.enable()
conn=pymysql.connect(host="Localhost",user="root",password="")
cur=conn.cursor()

q="""create database emart"""
cur.execute(q)
conn.commit()
print("""
<script>
alert("Create Successfully");
</script>
""")


conn.close()