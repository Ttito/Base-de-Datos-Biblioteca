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
Vnombre = form.getfirst('NombreCompleto','empty')
VNusuario = form.getfirst('NombreUsuario','empty')
Vemail = form.getfirst('Email1','empty')
Vcontrasena = form.getfirst('Contrasena1','empty')
VcontrasenaC = form.getfirst('Contrasena2','empty')

if(Vcontrasena!='empty' and Vcontrasena == VcontrasenaC):
    insertar = db.cursor()
    insertar.execute("insert into administrador values(null,'%s','%s','%s','%s')" % (Vnombre,VNusuario,Vemail,Vcontrasena))
    db.commit()
    insertar.close()

print("""

<html>
<head>
    <title>Administradores</title>
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
                            <li><a href="usuarios.py"><i class="zmdi zmdi-accounts zmdi-hc-fw"></i>&nbsp;&nbsp; Nuevo usuario</a></li>
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
                    <li><a href="report.py"><i class="zmdi zmdi-trending-up zmdi-hc-fw"></i>&nbsp;&nbsp; Reportes y estadasticas</a></li>
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
                <li  class="tooltips-general search-book-button" data-href="searchbook.py" data-placement="bottom" title="Buscar libro">
                    <i class="zmdi zmdi-search"></i>
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
              <h1 class="all-tittles">Sistema bibliotecario <small>Administracion Usuarios</small></h1>
            </div>
        </div>
        <div class="container-fluid">
            <ul class="nav nav-tabs nav-justified"  style="font-size: 17px;">
                <li role="presentation"  class="active"><a href="admin.py">Administradores</a></li>
                <li role="presentation"><a href="usuarios.py">Usuarios</a></li>        
            </ul>
        </div>
        <div class="container-fluid"  style="margin: 50px 0;">
            <div class="row">
                <div class="col-xs-12 col-sm-4 col-md-3">
                    <img src="assets/img/user01.png" alt="user" class="img-responsive center-box" style="max-width: 110px;">
                </div>
                <div class="col-xs-12 col-sm-8 col-md-8 text-justify lead">
                    Bienvenido a la seccion para registrar nuevos administradores del sistema, debes de llenar todos los campos del siguiente formulario para registrar un administrador
                </div>
            </div>
        </div>
        <div class="container-fluid">
            <div class="row">
                <div class="col-xs-12 lead">
                    <ol class="breadcrumb">
                      <li class="active">Nuevo administrador</li>
                      <li><a href="listadmin.py">Listado de administradores</a></li>
                    </ol>
                </div>
            </div>
        </div>
        <div class="container-fluid">
            <div class="container-flat-form">
                <div class="title-flat-form title-flat-blue">Registrar un nuevo administrador</div>
                <form autocomplete="off">
                    <div class="row">
                       <div class="col-xs-12 col-sm-8 col-sm-offset-2">
                            <div class="group-material">
                                <input type="text"  name = "NombreCompleto"  class="material-control tooltips-general" placeholder="Nombre completo" required="" maxlength="70"  data-toggle="tooltip" data-placement="top" title="Escribe el nombre del administrador">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Nombre completo</label>
                            </div>
                           <div class="group-material">
                                <input type="text" name = "NombreUsuario" class="material-control tooltips-general input-check-user" placeholder="Nombre de usuario" required="" maxlength="20" data-toggle="tooltip" data-placement="top" title="Escribe un nombre de usuario sin espacios, que servira para iniciar sesion">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Nombre de usuario</label>
                           </div>
                            <div class="group-material">
                                <input type="email" name = "Email1" class="material-control tooltips-general" placeholder="E-mail"  maxlength="50" data-toggle="tooltip" data-placement="top" title="Escribe el Email del administrador">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Email</label>
                            </div>
                            <div class="group-material">
                                <input type="password" name = "Contrasena1" class="material-control tooltips-general" placeholder="Contrasena" required="" maxlength="200" data-toggle="tooltip" data-placement="top" title="Escribe una contrasena">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Contrasena</label>
                            </div>
                           <div class="group-material">
                                <input type="password" name = "Contrasena2" class="material-control tooltips-general" placeholder="Repite la contrasena" required="" maxlength="200" data-toggle="tooltip" data-placement="top" title="Repite la contrasena">
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Repetir contrasena</label>
                           </div>
                            <p class="text-center">
                                <button type="reset" class="btn btn-info" style="margin-right: 20px;"><i class="zmdi zmdi-roller"></i> &nbsp;&nbsp; Limpiar</button>
                                <button type="submit" class="btn btn-primary"><i class="zmdi zmdi-floppy"></i> &nbsp;&nbsp; Guardar</button>
                            </p> 
                       </div>
                   </div>
                </form>
            </div>
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
        <footer class="footer full-reset">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-xs-12 col-sm-6">
                        <h4 class="all-tittles">Acerca de</h4>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam quam dicta et, ipsum quo. Est saepe deserunt, adipisci eos id cum, ducimus rem, dolores enim laudantium eum repudiandae temporibus sapiente.
                        </p>
                    </div>
                    <div class="col-xs-12 col-sm-6">
                        <h4 class="all-tittles">Desarrollador</h4>
                        <ul class="list-unstyled">
                            <li><i class="zmdi zmdi-check zmdi-hc-fw"></i>&nbsp; Grupo BD <i class="zmdi zmdi-facebook zmdi-hc-fw footer-social"></i><i class="zmdi zmdi-twitter zmdi-hc-fw footer-social"></i></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="footer-copyright full-reset all-tittles"> 2017 Grupo BD</div>
        </footer>
    </div>
</body>
</html>
        
""")