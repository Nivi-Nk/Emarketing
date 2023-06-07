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
    <title>User Homepage</title>
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
                    <a href="./User-Homepage.py?Id=%s">
                        <i class="fa fa-home fa-lg"></i> Home
                    </a>
                 </li>
                  """ % Id)
print(""" 
                 <li class=""><a href="./User-Profile-Update.py?Id=%s"><i class="fa fa-user fa-lg"></i> Personal Info</a></li>
                """%Id)
print(""" 
                 <li class=""><a href="./User-Buy-Product.py?Id=%s"><i class="fa fa-shopping-cart fa-lg"></i> Buy Product</a></li>
                """ % Id)

print("""
                    <li><a href="./User-Offer-Details.py?Id=%s"><i class="fa fa-bell "></i> Offers</a></li>
                """ % Id)
print("""             

                <li data-toggle="collapse" data-target="#buy" class="collapsed">
                    <a href="#"><i class="fa fa-shopping-cart fa-lg"></i> Purchase Details <i class="fa fa-chevron-down"></i></a>
                </li>
                <ul class="sub-menu collapse" id="buy">
                    <li><a href="./User-Delivery-Status.py?Id=%s"><i class="fa fa-chevron-right"></i> Delivery Status </a></li>
           """ % Id)
print("""
                    <li><a href="./User-Buy-History.py?Id=%s"><i class="fa fa-chevron-right"></i> View Buy History</a></li>
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

q = """select * from user where Id=%s""" % (Id)

cur.execute(q)
rec = cur.fetchall()

for i in rec:
    print("""
    <div class="col-md-5"></div>
    <div class="col-md-7">
    <h1>Welcome %s </h1>
    </div>
    """ % (i[2]))
conn.close()


print("""
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }
    </script>
""")