<div class="form-group">
                                    <div class="alert alert-danger" role="alert">

                                        <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                                        <span class="sr-only">Saisissez une date valide.</span>
                                        Saisissez une date valide.

                                    </div>
                                </div>









<%--
  Created by IntelliJ IDEA.
  User: mac
  Date: 25/02/2017
  Time: 15:55
  To change this template use File | Settings | File Templates.
--%>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>BootZard - Bootstrap Wizard Template</title>

    <!-- CSS -->
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
    <link rel="stylesheet" href="./assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="./assets/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="./assets/css/form-elements.css">
    <link rel="stylesheet" href="./assets/css/style.css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Favicon and touch icons -->
    <link rel="shortcut icon" href="assets/ico/favicon.png">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="./assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="./assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="./assets/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="./assets/ico/apple-touch-icon-57-precomposed.png">

</head>

<body>

<!-- Top menu -->
<nav class="navbar navbar-inverse navbar-no-bg" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#top-navbar-1">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="index.html">BootZard - Bootstrap Wizard Template</a>
        </div>
        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="top-navbar-1">
            <ul class="nav navbar-nav navbar-right">
                <li>
							<span class="li-text">
								Put some text or
							</span>
                    <a href="#"><strong>links</strong></a>
                    <span class="li-text">
								here, or some icons:
							</span>
                    <span class="li-social">
								<a href="https://www.facebook.com/pages/Azmindcom/196582707093191" target="_blank"><i class="fa fa-facebook"></i></a>
								<a href="https://twitter.com/anli_zaimi" target="_blank"><i class="fa fa-twitter"></i></a>
								<a href="https://plus.google.com/+AnliZaimi_azmind" target="_blank"><i class="fa fa-google-plus"></i></a>
								<a href="https://github.com/AZMIND" target="_blank"><i class="fa fa-github"></i></a>
							</span>
                </li>
            </ul>
        </div>
    </div>
</nav>

<!-- Top content -->
<div class="top-content">
    <div class="container">

        <div class="row">
            <div class="col-sm-8 col-sm-offset-2 text">
                <h1>Free <strong>Bootstrap</strong> Wizard</h1>
                <div class="description">
                    <p>
                        This is a free responsive Bootstrap form wizard.
                        Download it on <a href="http://azmind.com"><strong>AZMIND</strong></a>, customize and use it as you like!
                    </p>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2 col-lg-6 col-lg-offset-3 form-box">
                <form role="form" action="" method="post" class="f1">

                    <h3>Register To Our App</h3>
                    <p>Fill in the form to get instant access</p>
                    <div class="f1-steps">
                        <div class="f1-progress">
                            <div class="f1-progress-line" data-now-value="16.66" data-number-of-steps="3" style="width: 16.66%;"></div>
                        </div>
                        <div class="f1-step active">
                            <div class="f1-step-icon"><i class="fa fa-user"></i></div>
                            <p>about</p>
                        </div>
                        <div class="f1-step">
                            <div class="f1-step-icon"><i class="fa fa-key"></i></div>
                            <p>account</p>
                        </div>
                        <div class="f1-step">
                            <div class="f1-step-icon"><i class="fa fa-twitter"></i></div>
                            <p>social</p>
                        </div>
                    </div>

                    <fieldset>
                        <h4>Tell us who you are:</h4>
                        <div class="form-group">
                            <label class="sr-only" for="f1-first-name">First name</label>
                            <input type="text" name="f1-first-name" placeholder="First name..." class="f1-first-name form-control" id="f1-first-name">
                        </div>
                        <div class="form-group">
                            <label class="sr-only" for="f1-last-name">Last name</label>
                            <input type="text" name="f1-last-name" placeholder="Last name..." class="f1-last-name form-control" id="f1-last-name">
                        </div>
                        <div class="form-group">
                            <label class="sr-only" for="f1-about-yourself">About yourself</label>
                            <textarea name="f1-about-yourself" placeholder="About yourself..."
                                      class="f1-about-yourself form-control" id="f1-about-yourself"></textarea>
                        </div>
                        <div class="f1-buttons">
                            <button type="button" class="btn btn-next">Next</button>
                        </div>
                    </fieldset>

                    <fieldset>
                        <h4>Set up your account:</h4>
                        <div class="form-group">
                            <label class="sr-only" for="f1-email">Email</label>
                            <input type="text" name="f1-email" placeholder="Email..." class="f1-email form-control" id="f1-email">
                        </div>
                        <div class="form-group">
                            <label class="sr-only" for="f1-password">Password</label>
                            <input type="password" name="f1-password" placeholder="Password..." class="f1-password form-control" id="f1-password">
                        </div>
                        <div class="form-group">
                            <label class="sr-only" for="f1-repeat-password">Repeat password</label>
                            <input type="password" name="f1-repeat-password" placeholder="Repeat password..."
                                   class="f1-repeat-password form-control" id="f1-repeat-password">
                        </div>
                        <div class="f1-buttons">
                            <button type="button" class="btn btn-previous">Previous</button>
                            <button type="button" class="btn btn-next">Next</button>
                        </div>
                    </fieldset>

                    <fieldset>
                        <h4>Social media profiles:</h4>
                        <div class="form-group">
                            <label class="sr-only" for="f1-facebook">Facebook</label>
                            <input type="text" name="f1-facebook" placeholder="Facebook..." class="f1-facebook form-control" id="f1-facebook">
                        </div>
                        <div class="form-group">
                            <label class="sr-only" for="f1-twitter">Twitter</label>
                            <input type="text" name="f1-twitter" placeholder="Twitter..." class="f1-twitter form-control" id="f1-twitter">
                        </div>
                        <div class="form-group">
                            <label class="sr-only" for="f1-google-plus">Google plus</label>
                            <input type="text" name="f1-google-plus" placeholder="Google plus..." class="f1-google-plus form-control" id="f1-google-plus">
                        </div>
                        <div class="f1-buttons">
                            <button type="button" class="btn btn-previous">Previous</button>
                            <button type="submit" class="btn btn-submit">Submit</button>
                        </div>
                    </fieldset>

                </form>
            </div>
        </div>

    </div>
</div>

<!-- Javascript -->
<script src="./assets/js/jquery-1.11.1.min.js"></script>
<script src="./assets/bootstrap/js/bootstrap.min.js"></script>
<script src="./assets/js/jquery.backstretch.min.js"></script>
<script src="./assets/js/retina-1.1.0.min.js"></script>
<script src="./assets/js/scripts.js"></script>

<!--[if lt IE 10]>
<script src="./assets/js/placeholder.js"></script>
<![endif]-->

</body>

</html>









<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<link rel="stylesheet" type="text/css" href="./css/bootstrap.css">

<style>
    .jumbotron {
        width: 600px;
        text-align: center;
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
    }
    .table {
        margin-top: 20px;
    }
    .form-control {
        margin-bottom: 5px;
    }
</style>

<html>
<head>
    <title>Inscription LP Est casablanca</title>
</head>
<body>

<div class="jumbotron">
    <h3>École Superieure de Technologie de Casablanca</h3>
    <h3>Inscription Licence Professionnelle</h3>
    <h4>Filiere ${filiere}</h4>

    <form action="Etudiant" method="post">
        <input class="form-control" type="text" value="${nom}" placeholder="Nom"/>
        <input class="form-control" type="text" value="${prenom}" placeholder="Prenom"/>
        <input class="form-control" type="text" value="${genre}" placeholder="Genre"/>
        <input class="form-control" type="text" value="${cne}" placeholder="Cne"/>
        <input class="form-control" type="text" value="${etudiant.cin}" placeholder="Cin"/>
        <fieldset>
            <legend>Informations de Contact</legend>
            <input class="form-control" type="text" value="${etudiant.telephone}" placeholder="Telephone"/>
            <input class="form-control" type="text" value="${etudiant.email}" placeholder="Email"/>
            <input class="form-control" type="text" value="${etudiant.adresse}" placeholder="Adresse"/>
        </fieldset>

        <fieldset>
            <legend>Études precedents</legend>
            <div class="col-sm-6">
                <input class="form-control" type="text" value="${etudiant.type_bac}" placeholder="Type du baccalauréat"/>
            </div>
            <div class="col-sm-6">
                <input class="form-control mx-sm-3" type="text" value="${etudiant.type_diplome}" placeholder="type du diplome universitaire"/>
            </div>

            <div class="col-sm-6">
                <input class="form-control" type="text" value="${etudiant.note_s1}" placeholder="Note S1"/>
            </div>
            <div class="col-sm-6">
                <input class="form-control" type="text" value="${etudiant.note_s2}" placeholder="Note S2"/>
            </div>
            <div class="col-sm-6">
                <input class="form-control" type="text" value="${etudiant.note_s3}" placeholder="Note S3"/>
            </div>

            <div class="col-sm-6">
                <input class="form-control" type="text" value="${etudiant.note_s4}" placeholder="Note S4"/>
            </div>

        </fieldset>
        </br>

        <input type="submit" class="btn btn-primary btn-block" value="s'inscrice">

    </form>

</div>

</body>
</html>
