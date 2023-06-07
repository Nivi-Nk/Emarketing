#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")
print("""


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forget Password</title>
    <link rel="icon" type="image/x-icon" href="./Media/Images/logo.png">
    
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <!------ Include the above in your HEAD tag ---------->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
    <style>
        .form-gap {
            padding-top: 130px;
        }

        /* The Close Button (x) */
        .close {
            color: rgb(246, 8, 8);
            font-size: 35px;
            font-weight: bold;
        }

        .close:hover,
        .close:focus {
            color: white;
            background-color: red;
            cursor: pointer;
        }
    </style>
</head>

<body style="background-image: linear-gradient(to right, rgb(232, 126, 126), rgb(187, 140, 151), rgb(232, 113, 113));">


    <div class="form-gap"></div>
    <div class="container">
        <div class="row">
            <div class="col-md-4 col-md-offset-4">
                <div class="panel panel-default">
                    <div class="panel-body">
                        <a href="./index.py"><span class="close" title="Close"
                                style="padding: 5px">&times;</span></a>
                        <div class="text-center">
                            <h3><i class="fa fa-lock fa-4x"></i></h3>
                            <h2 class="text-center">Forgot Password?</h2>
                            <p>You can ask your password here.</p>
                            <div class="panel-body">

                                <form id="register-form" role="form" autocomplete="off" class="form" method="post">

                                    <div class="form-group">
                                        <div class="input-group">
                                            <span class="input-group-addon"><i
                                                    class="glyphicon glyphicon-user color-blue"></i></span>
                                            <input id="email" name="shid" placeholder="Shop Id"
                                                class="form-control" type="text">
                                        </div>
                                    </div>
                                     <div class="form-group">
                                        <div class="input-group">
                                            <span class="input-group-addon"><i
                                                    class="glyphicon glyphicon-envelope color-blue"></i></span>
                                            <input id="email" name="shemail" placeholder="Email address"
                                                class="form-control" type="email">
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <input name="submit" class="btn btn-lg btn-primary btn-block"
                                            value="Send My Password" type="submit">
                                    </div>

                                </form>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>

</html>
""")

import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="emart")
cur = conn.cursor()

form = cgi.FieldStorage()
Email = form.getvalue("shemail")
Shop_Id = form.getvalue("shid")
psubmit = form.getvalue("submit")

if psubmit != None:
    q = """select Id from shopkeeper where Email="%s" and Shop_Id="%s" """ % (Email, Shop_Id)
    cur.execute(q)
    Idvalue = cur.fetchone()
    conn.commit()
    q1 = """select * from shopkeeper where Id=%s""" % (Idvalue)
    cur.execute(q1)
    rec = cur.fetchall()
    for i in rec:
        Shopid = i[1]
        Name = i[2]
        Email = i[6]
        UserName = i[13]
        Password = i[14]
        Status = "New"
        q2 = """insert into password_recover(Shop_Id,Name,Email,Username,Password,Status) 
                values('%s','%s','%s','%s','%s','%s')""" % (Shopid, Name, Email, UserName, Password, Status)
        cur.execute(q2)
        conn.commit()
        print("""
                    <html>
                    <script>
                    alert(" Request Submitted");
                     location.href="index.py";
                        
                    </script>
                    </html>""")
conn.close()
