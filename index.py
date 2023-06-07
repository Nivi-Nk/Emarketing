#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb,os

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="emart")
cur = conn.cursor()

q = "select max(Id) from user"
cur.execute(q)

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

UserId = "23USR" + z + str(n + 1)

q5 = "select max(Id) from shopkeeper"
cur.execute(q5)

r1 = cur.fetchone()
if r1[0] != None:
    n1 = r1[0]
else:
    n1 = 0

z1 = ""
if n1 <= 9:
    z1 = "000"
elif n1 >= 10 and n1 <= 99:
    z1 = "00"
elif n1 >= 100 and n1 <= 999:
    z1 = "0"

Shop_Id = "23SHP" + z1 + str(n1 + 1)

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Home Page</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/x-icon" href="./Media/Images/logoonly.png">
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        body {
        # background-color: pink;
       
            margin: 0px;
        }

        /* nav style*/
        .navbar {
            background-color: rgb(240, 99, 155);
            height: 90px;
        }

        .navbar-nav {
                        background-color: rgb(240, 99, 155);
        }

        .centernav {
            margin-top: 20px;
        }

        .dropmenu {
            font-size: 18px;
        }

        .dropdown-menu li a:hover {
            background-color: rgb(66, 27, 27) !important;
            color: white !important;
        }

        h4 {
            margin-top: 3px;
            color: black;
        }


        /* modal style */
        .heading {
            font-size: 20px;
            font-family: Georgia, 'Times New Roman', Times, serif;
            color: white;
            margin-top: 10px;
        }

        /* The Close Button (x) */
        .close {
            color: white;
            font-size: 35px;
            font-weight: bold;
        }

        .close:hover,
        .close:focus {
            color: red;
            cursor: pointer;
        }

        /*input-container style */

        .input-container {
            display: -ms-flexbox;
            display: flex;
            width: 100%;
            margin-bottom: 15px;

        }

        .icon {
            padding: 10px;
            background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));
            color: white;
        }

        .input-field {
            width: 100%;
            padding: 5px;
            outline: none;
        }

        .input-field:focus {
            border: 2px solid rgb(104, 177, 250);
        }

        /* Set a style for the submit button */

        .btn {
            background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));
            color: white;
            padding: 10px;
            border: none;
            cursor: pointer;
            width: 100%;
            opacity: 0.9;
        }

        .btn:hover {
            opacity: 1;
        }

        span.psw {
            float: right;
        }

        .cancelbtn {

            background-color: red;
            color: rgb(249, 243, 243);
        }


        /* Add Zoom Animation */
        .animate {
            -webkit-animation: animatezoom 0.6s;
            animation: animatezoom 0.6s
        }


        @-webkit-keyframes animatezoom {
            from {
                -webkit-transform: scale(0)
            }

            to {
                -webkit-transform: scale(1)
            }
        }

        @keyframes animatezoom {
            from {
                transform: scale(0)
            }

            to {
                transform: scale(1)
            }
        }

        .footer {
            padding: 0;
            overflow: hidden;
            width: 100%;
            height: auto;
            background: rgb(70, 67, 67);
            color: white;
        }

        .footer-title {
            position: relative;
            color: #fff;
            font-size: 20px;
            font-weight: 600;
        }

        .footer-links a {
            padding: 10px 0;
            color: #fff;
            display: block;
            line-height: 10px;
            transition: color 0.5s ease-in-out;
            text-decoration: none;
        }

        .footer-links a:hover {
            color: #ff304d;
        }

        .link a {
            display: inline-block;
            padding-left: 10px;
        }

        /* footer  */
    </style>
    <script>
        var username, password;
        function login()
         {
            username = document.forms["loginform"]["uname"];
            password = document.forms["loginform"]["password"];
            if (username.value == "") {
                alert("Please Enter Name");
                username.focus()
                return false;
            }
            if (password.value == "") {
                alert("Please Enter Password");
                password.focus()
                return false;
            }
            if (username.value == "Admin" && password.value == "admin@123") {
                alert("Login Success");
                return true;
            }
            else {
                alert("User name not found");
                return false;
            }
        }
    </script>
</head>

<body>
    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container-fluid centernav">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#"><img src="./Media/Images/emart-logo.jpg" alt="" height="70px" width="350px"
                        style="margin-top:-28px ;margin-left: 5px; position: fixed;"></a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
            
                <ul class="nav navbar-nav navbar-right navcolor">
                    <!-- <li><a href="#"> Sign Up<span class="glyphicon glyphicon-user" style="padding-left:10px"></span></a>
                    </li> -->
                    <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">
                            <h4> Register <span class="caret"></span></h4>
                        </a>
                        <ul class="dropdown-menu" style="margin-top: 10px;">
                            <li>
                                <a data-toggle="modal" class="dropmenu" data-target="#userreg">User</a>
                            </li>
                            <li>
                                <a data-toggle="modal" class="dropmenu" data-target="#shopreg">Shop Keeper</a>
                            </li>
                        </ul>
                    </li>
                    <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">
                            <h4> Login <span class="caret"></span></h4>
                        </a>
                        <ul class="dropdown-menu" style="margin-top: 10px;">
                            <li>
                                <a data-toggle="modal" class="dropmenu" data-target="#adminlogin">Admin</a>
                            </li>
                            <li>
                                <a data-toggle="modal" class="dropmenu" data-target="#shopkeeperlogin">Shop Keeper</a>
                            </li>
                            <li>
                                <a data-toggle="modal" class="dropmenu" data-target="#userlogin"> User</a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
""")
sq="""select * from product_offer"""
cur.execute(sq)
view=cur.fetchall()

print("""
    <style>
        .card{
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.7);
        padding: 16px;
        height:350px;
        width:300px;
        float:left;
        margin-left:50px;
        margin-top:100px
        }    
    </style>
    
       <h1></h1>
       <h2></h2>
       <div class="container">
""")
for i in view:
    fn = "./Media/Product/" + i[4]
    print("""
       <div class="card">
           <div class="col-md-4"></div>
           <img src="%s" height="110px" width="110px" style="border-radius:55px; margin-top:20px">
           <h2 class="text-center" style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;">%s</h2>
           <br>
           <h4 class="text-center"> Price : %s</h4>
           <h4 class="text-center"> Offer : %s</h4>

       """ % (fn, i[3], i[5], i[7]))

    print("""
            <center><a class="btn-primary btn-md form-control" data-toggle="modal" data-target="#userreg">Buy Now</a></center>
           </div>
       """)
print("""</div>""")
print("""
    <!-- admin login -->

    <div class="modal fade" id="adminlogin" role="dialog">
        <form class="modal-dialog animate" style="margin-top:150px;" method="post" action="./Admin-Homepage.py" name="loginform"
            onsubmit="return login()">

            <!-- Modal content-->   
            <div class="modal-content animate">
                <div class="modal-header" style="background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));">
                    <span onclick="document.getElementById('adminlogin').style.display='none'" data-dismiss="modal"
                        class="close" title="Close Modal" style="padding: 5px">&times;</span>
                    <h4 class="modal-title text-center heading">
                        ADMIN LOGIN</h4>
                </div>
                <!-- model -->
                <div class="modal-body" style="padding: 50px;">
                    <div class="input-container">
                        <i class="fa fa-user icon"></i>
                        <input class="input-field" type="text" placeholder="Enter Username" name="uname">
                    </div>
                    <br>
                    <div class="input-container">
                        <i class="fa fa-key icon"></i>
                        <input class="input-field" type="password" placeholder="Password" name="password">
                    </div><br>
                    <center><button type="submit" class="btn btn-primary" onclick="adminfun()">Login</button></center>
                </div>
            </div>
        </form>
    </div>
    <!-- admin login -->

""")
print("""
   
    <!-- Shopkeeper login -->

    <div class="modal fade" id="shopkeeperlogin" role="dialog">
        <form class="modal-dialog animate" style="margin-top:150px;" name="" method="post" enctype=""multipart/form-dta>
            <!-- Modal content-->
            <div class="modal-content animate">
                <div class="modal-header" style="background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));">
                    <span onclick="document.getElementById('emplogin').style.display='none'" data-dismiss="modal"
                        class="close" title="Close Modal" style="padding: 5px">&times;</span>
                    <h4 class="modal-title text-center heading">
                        SHOPKEEPER LOGIN</h4>
                </div>
                <!-- model -->
                <div class="modal-body" style="padding: 50px;">
                    <div class="input-container">
                        <i class="fa fa-user icon"></i>
                        <input class="input-field" type="text" placeholder="Enter Username" id="uname" name="sname">
                    </div>
                    <br>
                    <div class="input-container">
                        <i class="fa fa-key icon"></i>
                        <input class="input-field" type="password" placeholder="Password" id="password" name="spass">
                    </div>
                    <center><input type="submit" name="ssubmit" class="btn btn-primary" value="Login"></center>

                    <span class="psw">Forget <a href="./Forget-Password.py">password?</a></span><br>
                </div>
            </div>
        </form>
    </div>
    """)

print("""

    <!-- User login -->

    <div class="modal fade" id="userlogin" role="dialog">
        <form class="modal-dialog animate" style="margin-top:150px;"  method="post" enctype=""multipart/form-dta>
            <!-- Modal content-->
            <div class="modal-content animate">
                <div class="modal-header" style="background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));">
                    <span onclick="document.getElementById('emplogin').style.display='none'" data-dismiss="modal"
                        class="close" title="Close Modal" style="padding: 5px">&times;</span>
                    <h4 class="modal-title text-center heading">
                        USER LOGIN</h4>
                </div>
                <!-- model -->
                <div class="modal-body" style="padding: 50px;">
                    <div class="input-container">
                        <i class="fa fa-user icon"></i>
                        <input class="input-field" type="text" placeholder="Enter Username" id="uname" name="uname">
                    </div>
                    <br>
                    <div class="input-container">
                        <i class="fa fa-key icon"></i>
                        <input class="input-field" type="password" placeholder="Password" id="password" name="upass">
                    </div>
                    <center><input type="submit" name="usubmit" class="btn btn-primary" value="Login"></center>

                  <!--  <span class="psw">Forget <a href="./Forget-Password.py">password?</a></span><br> -->
                </div>
            </div>
        </form>
    </div>
    """)

print("""
    <!-- User Registration -->
    <div class="modal fade" id="userreg" role="dialog">
        <form class="modal-dialog animate" name="profile" method="post" enctype="multipart/form-data">
            <!-- Modal content-->   
            <div class="modal-content animate">
                <div class="modal-header" style="background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));">
                    <span data-dismiss="modal"
                        class="close" title="Close Modal" style="padding: 5px">&times;</span>
                    <h4 class="modal-title text-center heading">
                        USER REGISTRATION</h4>
                </div>
                <!-- model -->
                <div class="modal-body" style="padding: 50px;">
        <div class="col-md-4"></div>
            """)
print("""
            <input class="form-control" type="text" value="%s" required><br>
            """ % UserId)
print("""
            <input class="form-control" autofocus type="text" name="name" placeholder="Enter your Name" maxlength="20" required><br>
            <input class="form-control" type="text" name="ph" placeholder="Phone Number" maxlength="10" required><br>
            <input class="form-control" type="text" name="address" placeholder="Address" maxlength="100"><br>
            <input class="form-control" type="text" name="email" placeholder="Email" maxlength="25" required><br>
            <label>Gender</label>
            <input type="radio" checked name="gender" Value="Male">Male
            <input type="radio" name="gender" Value="Female">Female
            <br><br>
            <input class="form-control" name="dob" placeholder="D.O.B" onfocus="(this.type='date')" onblur="(this.type='text')"><br>
            <input class="form-control" type="text" name="username" placeholder="User Name"><br>
            <input class="form-control" type="text" name="password" placeholder="Password"><br>
            <input class="form-control" name="image" placeholder="Upload Profile Picture" onfocus="(this.type='file')" onblur="(this.type='file')">
            <br>
            <input class="form-control btn btn-info" type="Submit" name="reg" value="REGISTER"><br><br><br>
             <span class="psw">Already have an account ? <a data-dismiss="modal" data-toggle="modal"  data-target="#userlogin">Login</a></span><br>
                </form>
                </div>
            </div>
        </form>
    </div>
""")

print("""
    <!-- Shop Keeper Registration -->
    <div class="modal fade" id="shopreg" role="dialog">
        <form class="modal-dialog animate" name="profile" method="post" enctype="multipart/form-data">
            <!-- Modal content-->   
            <div class="modal-content animate">
                <div class="modal-header" style="background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(177, 145, 151), rgb(232, 113, 113));">
                    <span data-dismiss="modal"
                        class="close" title="Close Modal" style="padding: 5px">&times;</span>
                    <h4 class="modal-title text-center heading">
                        SHOPKEEPER REGISTRATION</h4>
                </div>
                <!-- model -->
                <div class="modal-body" style="padding: 50px;">
        <div class="col-md-4"></div>
            """)
print("""
            <input class="form-control" type="text" value="%s" required><br>
            """ % Shop_Id)
print("""
            <input class="form-control" autofocus type="text" name="shname" placeholder="Enter your Name" maxlength="20" required><br>
            <input class="form-control" type="text" name="shage" placeholder="Age" required><br>            
            <input class="form-control" type="text" name="shph" placeholder="Phone Number" maxlength="10" required><br>
            <input class="form-control" type="text" name="shaddress" placeholder="Address" maxlength="100"><br>
            <input class="form-control" type="text" name="shemail" placeholder="Email" maxlength="25" required><br>
            <label>Gender </label>
            <input type="radio" checked name="shgender" Value="Male"> Male
            <input type="radio" name="shgender" Value="Female"> Female
            <br><br>
            <input class="form-control" type="text" name="shopname" placeholder="Shop Name" maxlength="25" required><br>
            
            <select class="form-control" id="" name=Shtype">
                <option disabled selected>Shop Type</option>
                <option value=>Textile</option>
                <option>Electronics</option>
                <option>Stationary</option>
                </select><br>
            <input class="form-control" type="text" name="shopaddress" placeholder="Shop Address"><br>
            <input class="form-control" type="text" name="shcity" placeholder="Shop City"><br>
            <input class="form-control" name="shimage" placeholder="User Profile Picture" onfocus="(this.type='file')" onblur="(this.type='file')">
            <br>
            <input class="form-control" name="shproof" placeholder="Idproof Picture" onfocus="(this.type='file')" onblur="(this.type='file')">
            <br>
            <input class="form-control" name="shopimage" placeholder="Shop Picture" onfocus="(this.type='file')" onblur="(this.type='file')">
            <br>
             <input class="form-control" type="text" name="shusername" placeholder="User Name"><br>
            <input class="form-control" type="text" name="shpassword" placeholder="Password"><br>
            <input class="form-control btn btn-info" type="Submit" name="shopreg" value="REGISTER"><br><br><br>
            <span class="psw">Already have an account ? <a data-dismiss="modal" data-toggle="modal"  data-target="#shopkeeperlogin">Login</a></span><br>      
        </form>
                </div>
            </div>
    </div>
</body>

</html>
    """)

form = cgi.FieldStorage()
Uname = form.getvalue("uname")
UPassword = form.getvalue("upass")
Usubmit = form.getvalue("usubmit")
Sname=form.getvalue("sname")
Spassword=form.getvalue("spass")
Submit=form.getvalue("ssubmit")
if Usubmit != None:
    q1 = """select Id from user where Username="%s" and Password="%s" """ % (Uname, UPassword)
    cur.execute(q1)
    res = cur.fetchone()
    conn.commit()
    if res != None:
        print("""
        <script>
            alert("Login success");
            location.href="User-Homepage.py?Id=%s";
        </script>""" % res[0])
    else:
        print("""
        <script>
        alert("Enter Valid Data");
        </script>""")
if Submit!=None:
    q2 = """select Id from shopkeeper where Username="%s" and Password="%s" and Status="Approved" """ % (Sname, Spassword)
    cur.execute(q2)
    res1 = cur.fetchone()
    conn.commit()

    vq = """select Id from shopkeeper where Username="%s" and Password="%s" and Status="New" """ % (
    Sname, Spassword)
    cur.execute(vq)
    vres = cur.fetchone()
    conn.commit()

    rq = """select Id from shopkeeper where Username="%s" and Password="%s" and Status="Rejected" """ % (
    Sname, Spassword)
    cur.execute(rq)
    rres = cur.fetchone()
    conn.commit()

    if res1 != None:
        print("""
            <script>
                alert("Login success");
                location.href="Shop-Keeper-Homepage.py?Id=%s";
            </script>""" % res1[0])
    elif vres!=None:
        print("""
                    <script>
                        alert("Your Registration On Processing");
                    </script>""")
    elif rres != None:
        print("""
                    <script>
                        alert("Your Request has been rejected");
                    </script>""")
    else:
        print("""
            <script>
            alert("Enter Valid Data");
            </script>""")

Reg = form.getvalue("reg")
if Reg!=None:
        Name = form.getvalue("name")
        Address = form.getvalue("address")
        Phone = form.getvalue("ph")
        Mail = form.getvalue("email")
        Gender = form.getvalue("gender")
        DOB = form.getvalue("dob")
        UserName = form.getvalue("username")
        Password = form.getvalue("password")
        Status = "New"
        pprofile = form['image']
        if pprofile.filename:
            fn = os.path.basename(pprofile.filename)
            open("./Media/User-Profile/" + fn, "wb").write(pprofile.file.read())
            q3 = """insert into user(UserId,Name,Address,Ph_No,Email,Gender,DOB,Profile,Username,Password) 
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (UserId, Name, Address, Phone, Mail, Gender, DOB, fn, UserName, Password)
            cur.execute(q3)
            conn.commit()
            print("""
                        <script>
                            alert(" Info Addedd Successfully")
                            location.href="index.py";
                        </script>
                       """)


ShopReg = form.getvalue("shopreg")
if ShopReg!=None:
        Name = form.getvalue("shname")
        Age=form.getvalue("shage")
        Address = form.getvalue("shaddress")
        Phone = form.getvalue("shph")
        Mail = form.getvalue("shemail")
        Gender = form.getvalue("shgender")
        SAddress=form.getvalue("shopaddress")
        SCity=form.getvalue("shcity")
        UserName = form.getvalue("shusername")
        Password = form.getvalue("shpassword")
        Shtype=form.getvalue("Shtype")
        Status = "New"
        pprofile = form['shimage']
        shprofile = form['shproof']
        shpic=form['shopimage']
        if shprofile.filename:
            fn = os.path.basename(pprofile.filename)
            prf = os.path.basename(shprofile.filename)
            shoppic = os.path.basename(shpic.filename)
            open("./Media/Shopkeeper-Profile/" + fn, "wb").write(pprofile.file.read())
            open("./Media/Shopkeeper-Profile/" + prf, "wb").write(shprofile.file.read())
            open("./Media/Shopkeeper-Profile/" + prf, "wb").write(shpic.file.read())

            q3 = """insert into shopkeeper(Shop_Id,Name,Phone,Address,Email,Gender,Id_Proof,Profile,Shop_Type,Shop_Image,Shop_Address,Shop_City,Username,Password,Status) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (Shop_Id, Name, Phone, Address, Mail, Gender, fn,prf,Shtype,shoppic,SAddress,SCity, UserName, Password,Status)
            cur.execute(q3)
            conn.commit()
            print("""
                        <script>
                            alert(" Info Addedd Successfully")
                            location.href="index.py";
                        </script>
                       """)

print("""
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }
    </script>
""")

conn.close()

