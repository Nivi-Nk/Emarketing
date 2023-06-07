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
import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="emart")
cur = conn.cursor()
q1 = """select*from product_offer """
cur.execute(q1)
rec = cur.fetchall()
print("""<div class="col-md-3"></div>
<div class="container col-md-8" style="margin-top:30px">

<div class="row">
<div class="container col-md-5">
<h2  style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;margin-left:20px;">Exist Offers</h2>
</div>
<div class="col-md-2"></div>
<div class="container col-md-5">
<input type="text" onkeyup='tableSearch()' id="myInput" placeholder="search by name" style="margin-top:20px"  class="form-control">
</div>
</div>
<br>
<table class="table" id="pager">
<tr><th>S.No</th>
<th>Shop_Id</th>
<th>Product Name</th>
<th>Product Offer</th>
<th>Product Price</th>
<th></th>
</tr>""")
sno = 0
for i in rec:
    sno +=1
    print("""
    <tr>
    <form method="post">
    <td>%s</td>
    <td>%s</td>    
    <td>%s</td>
    <td><input type="text" value="%s" name="mail" style="border:none;width:150px;"></td>
    <td><input type="text" value="%s" name="username" style="border:none;width:150px;"></td>
    <td><input type="text" value="%s" name="id" style="border:none;width:30px; display:none;"></td>
    </tr>
    </form>
    """ % (sno, i[2], i[3], i[7], i[5], i[0]))

print("""
    </table>
    </div>
    </div>
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
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }
    </script>
""")

