#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")


import pymysql
import cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()

Id = form.getvalue("Id")
conn = pymysql.connect(host="Localhost", user="root", password="", database="emart")
cur = conn.cursor()

q1 = "select max(Id) from product_offer"
cur.execute(q1)

r = cur.fetchone()
if r[0] != None:
    n = r[0]
else:
    n = 0

z = ""
if n <= 9:
    z = "000"
elif n >= 10 and n <= 99:
    z = "00"
elif n >= 100 and n <= 999:
    z = "0"

PrdId = "22PRD" + z + str(n + 1)

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

print("""
   <div class="col-md-5"></div>
   <div class="col-md-7" style="margin-top:100px">
    <h2  style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;margin-left:60px">Add New Product</h2><br>
   """)
print("""
            <form action="" class="container col-md-6"  name="profile" method="post" enctype="multipart/form-data">
            <input class="form-control" type="text" name="pid" value="%s" required><br>
            """ % PrdId)
print("""
            <input class="form-control" autofocus type="text" name="prdname" placeholder="Product Name" maxlength="20" required><br>
            <input class="form-control" type="text" name="prdprice" placeholder="Product Price" maxlength="10" required><br>
            <input class="form-control" type="text" name="prdq" placeholder="Product Quantity" maxlength="10"><br>
            <input class="form-control" type="text" name="prdoff" placeholder="Product Offer" maxlength="100"><br>
            """)
print("""
            <input class="form-control" name="str" placeholder="Prd_start" onfocus="(this.type='date')" onblur="(this.type='text')"><br>
            <input class="form-control" name="end" placeholder="Prd_end" onfocus="(this.type='date')" onblur="(this.type='text')"><br>
            <input class="form-control" name="prdimage" placeholder="Product_img" onfocus="(this.type='file')" onblur="(this.type='file')"><br>
            <input class="form-control btn btn-info" type="Submit" name="submit" value="ADD"><br><br><br>
        </form>
""")
import  smtplib,os
q2 = "select * from shopkeeper where Id='%s'" %(Id)
cur.execute(q2)
rec = cur.fetchall()
for i in rec:
    Shop_Id=i[1]
Submit = form.getvalue("submit")
if Submit!=None:
    if len(form) != 0:
        Prd_Name = form.getvalue("prdname")
        Prd_Price = form.getvalue("prdprice")
        Prd_Quantity = form.getvalue("prdq")
        Offer=form.getvalue("prdoff")
        Prd_Str = form.getvalue("str")
        Prd_End = form.getvalue("end")
        Status = "Active"
        pprofile = form['prdimage']
        #
        # fromadd = 'mail.testing.127.nk@gmail.com'
        # password = 'feroznwbapelpcqv'
        # toadd = Gmail
        # subject = ' Shop Registration '
        # body = 'Dear {}, \n\t\t   Admin has approved your request.'.format(Name)
        # msg = """Subject:{} \n\n {}""".format(subject, body)
        # server = smtplib.SMTP('smtp.gmail.com:587')
        # server.ehlo()
        # server.starttls()
        # server.login(fromadd, password)
        # server.sendmail(fromadd, toadd, msg)
        # server.quit()

        if pprofile.filename:
            fn = os.path.basename(pprofile.filename)
            open("./Media/Product/" + fn, "wb").write(pprofile.file.read())
            q = """insert into product_offer(Prod_Id,Shop_Id,Prod_Name,Product_Image,Product_Amount,Product_Quantity,Product_Offer,Off_start,Off_end,Status)
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (PrdId,Shop_Id,Prd_Name,fn,Prd_Price,Prd_Quantity,Offer,Prd_Str,Prd_End,Status)
            cur.execute(q)
            conn.commit()
            print("""
                    <script>
                    alert(" Info Addedd Successfully");
                    location.href="Shop-New-Offer.py?Id=%s";
                    </script>
                 """%Id)

conn.close()

print("""
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }
    </script>
""")

