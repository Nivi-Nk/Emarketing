#!C:/Users/admin/AppData/Local/Programs/Python/Python310/Python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
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
      """)


import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="Localhost",user="root",password="",database="emart")
cur=conn.cursor()

q1="""select*from shopkeeper where Status='Approved' """
cur.execute(q1)
rec=cur.fetchall()


print("""
<div class="col-md-3"></div>
<div class="container col-md-8">

<div class="row">
<div class="container col-md-5">
<h2  style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;margin-left:20px;">Shop Keeper Details</h2>
</div>
<div class="col-md-2"></div>
<div class="container col-md-5">
<input type="text" onkeyup='tableSearch()' id="myInput" placeholder="search by name" style="margin-top:20px"  class="form-control">
</div>
</div>
<br>
<table class="table" id="pager">
<tr><th>S.No</th>
<th>Shopkeeper Id</th>
<th>Name</th>
<th>Phone Number</th>
<th>Email</th>
<th>Profile</th>
<th></th>
</tr>""")
sno=0
for i in rec:
    sno=sno+1
    fn="./Media/Shopkeeper-Profile/"+i[7]
    print("""
    <tr>
    <form method="post">
    <td><input type="text" value="%s" name="id" style="border:none;width:30px;"></td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td> 
    <td><img src="%s" height="100px" width="100px"style="border-radius:50px;"> </td>
    """%(sno,i[1],i[2],i[4],i[6],fn))
    print("""
       </form>
        """)
print("""
    </table>
    </div>
    </div class="col-md-1"></div>
    </div>
    """)


q2="""select*from shopkeeper where Status='Rejected' """
cur.execute(q2)
res=cur.fetchall()
print("""
<div class="col-md-3"></div>
<div class="container col-md-8">
<center>
    <h2  style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;">Rejected  Details</h2>

</center><br>
<table class="table">
<tr><th>S.No</th>
<th>Shopkeeper Id</th>
<th>Name</th>
<th>Phone Number</th>
<th>Email</th>
<th>Profile</th>
<th></th>
</tr>""")
sno=0
for i in res:
    sno=sno+1
    fn="./Media/Shopkeeper-Profile/"+i[7]
    print("""
    <tr>
    <form method="post">
    <td><input type="text" value="%s" name="id" style="border:none;width:30px;"></td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td> 
    <td><img src="%s" height="100px" width="100px"style="border-radius:50px;"> </td>
    </tr>
    """%(sno,i[1],i[2],i[4],i[6],fn))
    print("""
       </form>
        """)

# Search the values in table by name
print("""
<script>

         function tableSearch() {
            let input, filter, table, tr, td, txtValue;

            //Intialising Variables
            input = document.getElementById("myInput");
            filter = input.value.toUpperCase();
            table = document.getElementById("pager");
            tr = table.getElementsByTagName("tr");

            for (let i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[2];
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = "";
                    } else {
                        tr[i].style.display = "none";
                    }
                }
            }

        }

</script>
""")
print("""
    </table>
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
