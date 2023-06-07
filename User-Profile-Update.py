#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, os
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="emart")
cur = conn.cursor()

form = cgi.FieldStorage()
Id = form.getvalue("Id")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Profile Update</title>
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
    <style>
        .card{
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.7);
        padding: 16px;
        height:400px;
        width:400px;
        margin-top:100px;
        }    
    </style>

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
                 <li>
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
q = """select * from user where Id=%s""" % (Id)
cur.execute(q)
rec = cur.fetchall()

for i in rec:
    fn = "./Media/User-Profile/" + i[8]
    print("""
    <h1></h1>
    <h2></h2>
    <div class="col-md-5"></div>
    <div class="card col-md-7">
        <div class="col-md-4"></div>
        <a data-toggle="modal" data-target="#profileupdate"><img src="%s" height="110px" width="110px" style="border-radius:55px; margin-top:20px"></a>
        <h2 class="text-center" style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;margin-left:20px;">%s</h2>
        <br>
        <h4 class="text-center"> Employee Id : %s</h4>
        <h4 class="text-center"> Phone Number : %s</h4>

    """ % (fn, i[2], i[1], i[4]))

    print("""
                <br><br><center><a data-toggle="modal" data-target="#passwordupdate">change password</a></center>
        </div>
    """)

print("""
    <div class="modal fade" id="passwordupdate" role="dialog">
        <form class="modal-dialog animate" style="margin-top:150px;" method="post">
            <div class="modal-content animate">
                <div class="modal-header" style=" background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));">
                    <span onclick="document.getElementById('passwordupdate').style.display='none'" data-dismiss="modal"
                        class="close" title="Close Modal" style="padding: 5px">&times;</span>
                    <h4 class="modal-title text-center heading" style="color:white;" >
                        PASSWORD CHANGE</h4>
                </div>
                <!-- model -->
                <div class="modal-body" style="padding: 50px;">
                        <input class="form-control" type="password" placeholder="Old Password" name="pass"><br>
                        <input class="form-control" type="password" placeholder="New Password" name="new"><br>
                        <input class="form-control" type="password" placeholder="Confirm Password" name="cnew"><br>
                        <input class="form-control" style=" background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));color:white;" type="submit" class="but" name="sub" value="Submit"><br>
                </div>
            </div>
        </form>
    </div>
    <script>

    </script>

    """)

print("""

    <div class="modal fade" id="profileupdate" role="dialog">
        <form class="modal-dialog animate" style="margin-top:150px;" method="post" enctype="multipart/form-data"> 
            <div class="modal-content animate">
                <div class="modal-header" style=" background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));">
                    <span onclick="document.getElementById('profileupdate').style.display='none'" data-dismiss="modal"
                        class="close" title="Close Modal" style="padding: 5px">&times;</span>
                    <h4 class="modal-title text-center heading" style="color:white;" >
                        PROFILE UPDATE</h4>
                </div>
                <div class="modal-body" style="padding: 50px;">
                    <input class="form-control"  name="images" placeholder="New Profile" onfocus="(this.type='file')" onblur="(this.type='file')"><br><br>
                    <center><input type="submit" name="update" class="form-control" style=" background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));color:white;" value="Update"></center><br>
                </div>
            </div>
        </form>
    </div>

""")

Update = form.getvalue("update")
Submit = form.getvalue("sub")
Pass = form.getvalue("pass")
New = form.getvalue("new")
CNew = form.getvalue("cnew")
if Submit != None:
    if CNew == New:
        q1 = """update user set Password="%s" where Password='%s' """ % (New, Pass)
        cur.execute(q1)
        conn.commit()
        print("""
                <script>
                    alert("Password Changed")
                    location.href="./index.py"
                </script>
                """)
if Update != None:
    if len(form) != 0:
        Profile = form['images']
        if Profile.filename:
            fl = os.path.basename(Profile.filename)
            open("./Media/User-Profile/" + fl, "wb").write(Profile.file.read())
            q1 = """update user set Profile="%s" where Id='%s' """ % (fl, Id)
            cur.execute(q1)
            conn.commit()
            print("""
                <script>
                    alert("profile update success");
                    location.href="./User-Profile-Update.py?Id=%s";
                </script>
                </body>
                </html>""" % Id)
conn.close()




