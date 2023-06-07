#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Admin Page</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="./Media/Images/logoonly.png">
    <link rel="stylesheet" href="./style.css">
    
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
   
</head>

<body>
    <div class="nav-side-menu">
        <div class="brand"><img src="./Media/Images/emart-logo.jpg" height="67px" width="300px" alt="">
        </div>
        <hr>
        <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>
        <div class="menu-list">

            <ul id="menu-content" class="menu-content collapse out">
                 <li class="active">
                    <a href="./Admin-Homepage.py">
                        <i class="fa fa-home fa-lg"></i> Home
                    </a>
                 </li> 

            <!--    <li data-toggle="collapse" data-target="#one" class="collapsed">
                    <a href="#"><i class="fa fa-group fa-lg"></i> Shopkeeper Details <i class="fa fa-chevron-down"></i></a>
                </li>
                <ul class="sub-menu collapse" id="one">
                    <li><a href="./Adm-New-Shopkeeper.py"><i class="fa fa-chevron-right"></i>  New Shopkeeper </a></li>
                    <li><a href="./Adm-Exist-Shop-Keeper.py"><i class="fa fa-chevron-right"></i>  Existing Shopkeeper</a></li>
                </ul>
                
                <li data-toggle="collapse" data-target="#two" class="collapsed">
                    <a href="#"><i class="fa fa-group fa-lg"></i> Shopkeeper Details <i class="fa fa-chevron-down"></i></a>
                </li>
                <ul class="sub-menu collapse" id="two">
                    <li><a href="./Adm-New-Shopkeeper.py"><i class="fa fa-chevron-right"></i>  New Shopkeeper </a></li>
                    <li><a href="./Adm-Exist-Shop-Keeper.py"><i class="fa fa-chevron-right"></i>  Existing Shopkeeper</a></li>
                </ul>
                -->
                
                <li data-toggle="collapse" data-target="#shp" class="collapsed">
                    <a href="#"><i class="fa fa-group fa-lg"></i> Shopkeeper Details <i class="fa fa-chevron-down"></i></a>
                </li>
                <ul class="sub-menu collapse" id="shp">
                    <li><a href="./Adm-New-Shopkeeper.py"><i class="fa fa-chevron-right"></i>  New Shopkeeper </a></li>
                    <li><a href="./Adm-Exist-Shop-Keeper.py"><i class="fa fa-chevron-right"></i>  Existing Shopkeeper</a></li>
                </ul>

               
                <li>
                    <a href="./Adm-View-Offers.py"><i class="fa fa-bullhorn fa-lg"></i> View Offers<span></span></a>
                </li>

                <li>
                    <a href="./Adm-Pass-Request.py"><i class="fa fa-bell fa-lg"></i> Password Request <span></span></a>
                </li>
                <li>
                    <a href="./index.py">
                        <i class="fa fa-backward fa-lg"></i> Logout
                    </a>
                </li>

            </ul>
        </div>
    </div>

    <div class="col-md-4"></div>
    <div class="col-md-7" style="margin-top:100px">
    """)

import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="Localhost",user="root",password="",database="emart")
cur=conn.cursor()

q1="""select*from password_recover where Status='New' """
cur.execute(q1)
rec=cur.fetchall()


print("""
<div class="container col-md-6">
<table class="table">
<tr><th>S.No</th>
<th>Shop_Id</th>
<th>Name</th>
<th>Email</th>
<th></th>
</tr>""")
sno=0
for i in rec:
    sno=+1
    print("""
    <tr>
    <form method="post">
    <td>%s</td>
    <td><input type="text" value="%s" name="shid" style="border:none;width:150px;"></td>    
    <td><input type="text" value="%s" name="name" style="border:none;width:150px;"></td>
    <td><input type="text" value="%s" name="mail" style="border:none;width:150px;"></td>
    <td><input type="text" value="%s" name="username" style="border:none;width:30px; display:none;"></td>
    <td><input type="text" value="%s" name="password" style="border:none;width:30px; display:none;"></td>
    <td><input type="text" value="%s" name="id" style="border:none;width:30px; display:none;"></td>
    
    """%(sno,i[1],i[2],i[3],i[4],i[5],i[0]))
    print("""
            <td>
                <input type="submit"  value="Approve" name="approve" class="edit">
            </td>
            <td>
                <input type="submit"  value="Reject" name="reject" class="save">     
            </td>
            </tr>
        </form>
            """)
import  smtplib
form = cgi.FieldStorage()
Name=form.getvalue("name")
User=form.getvalue("username")
Pass=form.getvalue("password")
Approve = form.getvalue("approve")
Reject = form.getvalue("reject")
IdValue = form.getvalue("id")
Gmail=form.getvalue("mail")
if Approve != None:
    fromadd = 'mail.testing.127.nk@gmail.com'
    password = 'feroznwbapelpcqv'
    toadd = Gmail
    subject = ' Password Recover '
    body = 'Dear {}, \n\t\t   Admin has approved your request. \n\t Username : {} \n\t Password : {} '.format(Name,User,Pass)
    msg = """Subject:{} \n\n {}""".format(subject, body)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromadd, password)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    q = """update password_recover set Status='Approved' where Id='%s'""" % (IdValue)
    cur.execute(q)
    conn.commit()
    print("""
            <script>
               alert(" updated successfully");
               location.href="Adm-Pass-Request.py";
            </script>
            """)
if Reject != None:
    q = """update password_recover set Status='Rejected' where Id='%s'""" % (IdValue)
    cur.execute(q)
    conn.commit()
    print("""
                <script>
                   alert(" updated successfully");
                   location.href="Adm-Pass-Request.py";
                </script>
                """)

print("""
    </table>
    </div>
    </body>
    </html>""")
conn.close()
print("""
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }
    </script>
""")