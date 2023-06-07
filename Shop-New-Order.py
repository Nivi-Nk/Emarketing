#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()

Id = form.getvalue("Id")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Shop Keeper Homepage</title>
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
        <div class="brand"><img src="./Media/Images/emart-logo.jpg" height="67px" width="300px" alt=""></div>
        <hr>
        <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>
        <div class="menu-list">
            <ul id="menu-content" class="menu-content collapse out">
                """)
print("""           
                 <li class="active">
                    <a href="./Shop-Keeper-Homepage.py?Id=%s">
                        <i class="fa fa-home fa-lg"></i> Home
                    </a>
                 </li>
                  """ % Id)
print(""" 
                 <li>
                    <a href="./Shop-Keeper-Profile-Update.py?Id=%s"><i class="fa fa-user fa-lg"></i> Personal Info </a>
                </li>
                 """ % Id)
print("""

                <li data-toggle="collapse" data-target="#income" class="collapsed">
                    <a href="#"><i class="fa fa-rupee fa-lg"></i> Order Details <i class="fa fa-chevron-down"></i></a>
                </li>
                <ul class="sub-menu collapse" id="income">
                    <li><a href="./Shop-New-Order.py?Id=%s"><i class="fa fa-chevron-right"></i> New Order</a></li>             
""" % Id)
print("""             
                    <li><a href="./Shop-Exist-Order.py?Id=%s"><i class="fa fa-chevron-right"></i>  Exist Order</a></li>
                </ul>

""" % Id)
print("""             

                <li data-toggle="collapse" data-target="#service" class="collapsed">
                    <a href="#"><i class="fa fa-bell fa-lg"></i> Offer <i class="fa fa-chevron-down"></i></a>
                </li>
                <ul class="sub-menu collapse" id="service">
                    <li><a href="./Shop-New-Offer.py?Id=%s"><i class="fa fa-chevron-right"></i> New</a></li>
           """ % Id)

print("""
                    <li><a href="./Shop-Exist-Offer.py?Id=%s"><i class="fa fa-chevron-right"></i> Previous</a></li>
                </ul>
                """ % Id)

print("""
                <li>
                    <a href="./index.py">
                        <i class="fa fa-backward fa-lg"></i> Logout
                    </a>
                </li>
            </ul>
        </div>
    </div>
</body>

</html>
""")

conn = pymysql.connect(host="Localhost", user="root", password="", database="emart")
cur = conn.cursor()


print("""
<div class='col-md-4'></div>
<div class="container col-md-6" style="margin-top:100px">
<table class="table">
<tr><th>S.No</th>
<th>User_Id</th>
<th>Product Name</th>
<th>Product Quantity</th>
<th>Product Price</th>
<th>Order Date</th>
<th></th>
</tr>""")
q2 = """select * from order_details where Status='New'  """
cur.execute(q2)
res = cur.fetchall()
sno = 0
for i in res:
    sno +=1
    print("""
    <tr>
    <form method="post">
    <td>%s</td>
    <td><input type="text" value="%s" name="userid" style="border:none;width:150px;"></td>
    <td><input type="text" value="%s" name="prdname" style="border:none;width:150px;"></td>
    <td><input type="text" value="%s" name="prdprice" style="border:none;width:50px;"></td>
    <td><input type="text" value="%s" name="prdquantity" style="border:none;width:50px;"></td>
    <td><input type="text" value="%s" name="id" style="border:none;width:30px; display:none;"></td>

    """ % (sno,i[1],i[4],i[6], i[5], i[0]))
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

import smtplib

Uid=form.getvalue("userid")
Approve = form.getvalue("approve")
Reject = form.getvalue("reject")
IdValue = form.getvalue("id")
# mq = """select * from user where UserId=%s """ % (Uid)
# cur.execute(mq)
# conn.commit()
# ml = cur.fetchall()
# for i in ml:
#     Gmail = i[5]
#     Name = i[2]
if Approve != None:
    # if (mq):
    #     fromadd = 'mail.testing.127.nk@gmail.com'
    #     password = 'feroznwbapelpcqv'
    #     toadd = Gmail
    #     subject = ' Purchase Details '
    #     body = 'Dear {}, \n\t\t Your order is accepted. '.format(Name)
    #     msg = """Subject:{} \n\n {}""".format(subject, body)
    #     server = smtplib.SMTP('smtp.gmail.com:587')
    #     server.ehlo()
    #     server.starttls()
    #     server.login(fromadd, password)
    #     server.sendmail(fromadd, toadd, msg)
    #     server.quit()
    q = """update order_details set Status='Shipped' where Id='%s'""" % (IdValue)
    cur.execute(q)
    conn.commit()
    print("""
            <script>
               location.href="Shop-New-Order.py?Id=%s";
            </script>
            """%Id)
if Reject != None:
    q = """update order_details set Status='Canceled' where Id='%s'""" % (IdValue)
    cur.execute(q)
    conn.commit()
    print("""
                <script>
                   location.href="Shop-New-Order.py?Id=%s";
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