#!C:\Python27\python

import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re


print("Content-Type: text/html\n")

dato = {'user' : 'root',
        'password':'',
        'database':'biblioteca',
        'host':'127.0.0.1'}
db = mysql.connector.connect(** dato)

form = cgi.FieldStorage()
Vlibro = form.getfirst('bookName','empty')
cursor = db.cursor()
sql="select titulo,autor,editorial from recurso where titulo like '%s' or autor like '%s'" %(Vlibro,Vlibro)
cursor.execute(sql)
resultado = cursor.fetchall()

print("""
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Buscar libro</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="Shortcut Icon" type="image/x-icon" href="assets/icons/book.ico" />
    <script src="js/sweet-alert.min.js"></script>
    <link rel="stylesheet" href="css/sweet-alert.css">
    <link rel="stylesheet" href="css/material-design-iconic-font.min.css">
    <link rel="stylesheet" href="css/normalize.css">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/jquery.mCustomScrollbar.css">
    <link rel="stylesheet" href="css/style.css">
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="js/jquery-1.11.2.min.js"><\/script>')</script>
    <script src="js/modernizr.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.mCustomScrollbar.concat.min.js"></script>
    <script src="js/main.js"></script>
</head>
<body>
    <div class="navbar-lateral full-reset">
        <div class="visible-xs font-movile-menu mobile-menu-button"></div>
        <div class="full-reset container-menu-movile custom-scroll-containers">
            <div class="logo full-reset all-tittles">
                <i class="visible-xs zmdi zmdi-close pull-left mobile-menu-button" style="line-height: 55px; cursor: pointer; padding: 0 10px; margin-left: 7px;"></i> 
                sistema bibliotecario
            </div>
            <div class="full-reset" style="background-color:#2B3D51; padding: 10px 0; color:#fff;">
                <figure>
                    <img src="assets/img/logo.png" alt="Biblioteca" class="img-responsive center-box" style="width:55%;">
                </figure>
                <p class="text-center" style="padding-top: 15px;">Sistema Bibliotecario</p>
            </div>
            <div class="full-reset nav-lateral-list-menu">
                <ul class="list-unstyled">
                    <li><a href="home.py"><i class="zmdi zmdi-home zmdi-hc-fw"></i>&nbsp;&nbsp; Inicio</a></li>

                    <li>
                        <div class="dropdown-menu-button"><i class="zmdi zmdi-account-add zmdi-hc-fw"></i>&nbsp;&nbsp; Registro de usuarios <i class="zmdi zmdi-chevron-down pull-right zmdi-hc-fw"></i></div>
                        <ul class="list-unstyled">
                            <li><a href="admin.py"><i class="zmdi zmdi-face zmdi-hc-fw"></i>&nbsp;&nbsp; Nuevo administrador</a></li>
                            <li><a href="usuarios.py"><i class="zmdi zmdi-accounts zmdi-hc-fw"></i>&nbsp;&nbsp; Nuevo Usuario</a></li>
                        </ul>
                    </li>
                    <li>
                        <div class="dropdown-menu-button"><i class="zmdi zmdi-assignment-o zmdi-hc-fw"></i>&nbsp;&nbsp; Libros y catalogo <i class="zmdi zmdi-chevron-down pull-right zmdi-hc-fw"></i></div>
                        <ul class="list-unstyled">
                            <li><a href="book.py"><i class="zmdi zmdi-book zmdi-hc-fw"></i>&nbsp;&nbsp; Nuevo libro</a></li>
                            <li><a href="catalog.py"><i class="zmdi zmdi-bookmark-outline zmdi-hc-fw"></i>&nbsp;&nbsp; Catalogo</a></li>
                        </ul>
                    </li>
                    <li>
                        <div class="dropdown-menu-button"><i class="zmdi zmdi-alarm zmdi-hc-fw"></i>&nbsp;&nbsp; Prestamos y reservaciones <i class="zmdi zmdi-chevron-down pull-right zmdi-hc-fw"></i></div>
                        <ul class="list-unstyled">
                            <li><a href="loan.py"><i class="zmdi zmdi-calendar zmdi-hc-fw"></i>&nbsp;&nbsp; Todos los prestamos</a></li>
                            <li>
                                <a href="loanpending.py"><i class="zmdi zmdi-time-restore zmdi-hc-fw"></i>&nbsp;&nbsp; Devoluciones pendientes <span class="label label-danger pull-right label-mhover">7</span></a>
                            </li>
                            <li>
                                <a href="loanreservation.py"><i class="zmdi zmdi-timer zmdi-hc-fw"></i>&nbsp;&nbsp; Reservaciones <span class="label label-danger pull-right label-mhover">7</span></a>
                            </li>
                        </ul>
                    </li>
                    <li><a href="report.py"><i class="zmdi zmdi-trending-up zmdi-hc-fw"></i>&nbsp;&nbsp; Reportes y estadisticas</a></li>
                    <li><a href="advancesettings.py"><i class="zmdi zmdi-wrench zmdi-hc-fw"></i>&nbsp;&nbsp; Configuraciones avanzadas</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="content-page-container full-reset custom-scroll-containers">
        <nav class="navbar-user-top full-reset">
            <ul class="list-unstyled full-reset">
                <figure>
                   <img src="assets/img/user01.png" alt="user-picture" class="img-responsive img-circle center-box">
                </figure>
                <li style="color:#fff; cursor:default;">
                    <span class="all-tittles">Admin Name</span>
                </li>
                <li  class="tooltips-general exit-system-button" data-href="index.py" data-placement="bottom" title="Salir del sistema">
                    <i class="zmdi zmdi-power"></i>
                </li>

                <li  class="tooltips-general search-book-button"  data-href="searchbook.py" data-placement="bottom"  title="Buscar libro">
                    <i class="zmdi zmdi-search" name = "Blibro" ></i>
                </li>
                <li  class="tooltips-general btn-help" data-placement="bottom" title="Ayuda">
                    <i class="zmdi zmdi-help-outline zmdi-hc-fw"></i>
                </li>
                <li class="mobile-menu-button visible-xs" style="float: left !important;">
                    <i class="zmdi zmdi-menu"></i>
                </li>
            </ul>
        </nav>
        <div class="container">
            <div class="page-header">
              <h1 class="all-tittles">Sistema bibliotecario <small>Busqueda de libro</small></h1>
            </div>
        </div>

        <br><br><br>
        <h3 class="text-center all-tittles">resultados de la busqueda</h3> 
        """)
print("""<div class="container-fluid">""")
if(len(resultado)==0):
    print("""<h2 class="text-center"><i class="zmdi zmdi-mood-bad zmdi-hc-5x"></i><br><br>Lo sentimos, no hemos encontrado ningun libro con el nombre <strong>ingresado</strong> en el sistema</h2>""")
else:
    cont=1
    cont1=0 
    for i in resultado:
        print("""
                <div class="media media-hover">
                    <div class="media-left media-middle">
                        <a href="#!" class="tooltips-general" data-toggle="tooltip" data-placement="right" title="Mas informacion del libro">
                        <img class="media-object" src="assets/img/book.png" alt="Libro" width="48" height="48">
                        </a>
                    </div>
                    <div class="media-body">
                    <h4 class="media-heading">""")
        print(cont) 
        cont = cont+1
        print("""       - Titulo :""")
        print(resultado[cont1][0])
        print(""" </h4>             
                        <div class="pull-left">
                            <strong>""")
        print("""Autor :""")
        print(resultado[cont1][1])
        print("""<br>
                            <strong>Editorial :""")
        print(resultado[cont1][2])
        print("""<br>
                        </div>
                        <p class="text-center pull-right">
                        <a href="reservar.py" class="btn btn-info btn-xs" style="margin-right: 10px;"><i class="zmdi zmdi-info-outline"></i> &nbsp;&nbsp; Solicitar Recerva</a>
                        <a href="prestamo.py" class="btn btn-info btn-xs" style="margin-right: 10px;"><i class="zmdi zmdi-info-outline"></i> &nbsp;&nbsp; Solicitar Prestamo</a>
                        </p>
                    </div>
                </div>""")
        cont1 = cont1+1

print("""
            </div>
            <div class="modal fade" tabindex="-1" role="dialog" id="ModalHelp">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        <h4 class="modal-title text-center all-tittles">ayuda del sistema</h4>
                    </div>
                    <div class="modal-body">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore dignissimos qui molestias ipsum officiis unde aliquid consequatur, accusamus delectus asperiores sunt. Quibusdam veniam ipsa accusamus error. Animi mollitia corporis iusto.
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="zmdi zmdi-thumb-up"></i> &nbsp; De acuerdo</button>
                    </div>
                </div>
            </div>
            </div>
           
        </div>
    </body>
    </html>
    """)
