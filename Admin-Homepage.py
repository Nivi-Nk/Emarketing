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
    
    <div class="col-md-3"></div>
    <div class="col-md-7">
        <h3 class="text-center">Welcome To Emart</h3>
    </div>
</body>
</html>
      """)

print("""
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }
    </script>
""")