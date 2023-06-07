#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import  cgitb

cgitb.enable()
conn=pymysql.connect(host="Localhost",user="root",password="",database="abc")
cur=conn.cursor()

q="""create table shopkeeper(Id int(10)Auto_increment primary key,Shop_Id varchar(30),Name varchar(20),Phone bigint(20),Address varchar(50),Gender varchar(20),Email varchar(30),Id_proof varchar(40),Profile varchar(30),Shop_Type varchar(20), Shop_Image varchar(30),Shop_Address varchar(30),Shop_City varchar(30),Username varchar(20),Password varchar(30),Status varchar(20))"""
cur.execute(q)
conn.commit()


print("""
<script>
alert("Create Successfully");
</script>
""")
conn.close()