<%--
  Created by IntelliJ IDEA.
  User: mac
  Date: 04/03/2017
  Time: 15:10
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<!DOCTYPE html>
<html lang="fr">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ESTC -Inscription LP </title>

    <!-- CSS -->
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="assets/css/form-elements.css">
    <link rel="stylesheet" href="assets/css/style.css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Favicon and touch icons -->
    <link rel="shortcut icon" href="assets/ico/favicon.png">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="assets/ico/apple-touch-icon-57-precomposed.png">

</head>

<body>

<!-- Top menu -->


<!-- Top content -->
<div class="top-content">
    <div class="container">

        <div class="row">
            <div class="col-sm-8 col-sm-offset-2 text">
                <h2><strong>École Superieure de Technologie de Casablanca</strong></h2>
                <div class="description">
                    <p>
                    </p>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2 form-box">
                <form role="form" action="Candidat" method="post" class="f1">

                    <h3>Inscription Licence Professionnelle</h3>
                    </br>
                    <div class="f1-steps">
                        <div class="f1-progress">
                            <div class="f1-progress-line" data-now-value="10" data-number-of-steps="3" style="width: 10%;"></div>
                        </div>
                        <div class="f1-step active">
                            <div class="f1-step-icon"><i class="fa fa-user"></i></div>
                            <p>Informations basiques</p>
                        </div>
                        <div class="f1-step">
                            <div class="f1-step-icon"><i class="fa fa-user"></i></div>
                            <p>contacts et adresse</p>
                        </div>
                        <div class="f1-step">
                            <div class="f1-step-icon"><i class="fa fa-mortar-board"></i></div>
                            <p>Bac</p>
                        </div>
                        <div class="f1-step">
                            <div class="f1-step-icon"><i class="fa fa-mortar-board"></i></div>
                            <p>Bac+2</p>
                        </div>
                        <div class="f1-step">
                            <div class="f1-step-icon"><i class="fa fa-mortar-board"></i></div>
                            <p>Licence Pro</p>
                        </div>
                    </div>

                    <fieldset>
                        <h4>saisiez vos informations:</h4>
                        <div class="form-group">
                            <input type="text" name="nom" placeholder="nom..." class="f1-first-name form-control" id="f1-first-name">
                        </div>
                        <div class="form-group">
                            <input type="text" name="prenom"  placeholder="prenom..." class="f1-last-name form-control" id="f1-last-name">
                        </div>
                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-cne" name="cne" placeholder="cne étudiant">
                        </div>

                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-cin" name="cin" placeholder="cin national ">
                        </div>
                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-nationalite" name="nationalite" placeholder="nationalité">
                        </div>
                        <div class="form-group">
                            <input type="date"  class="f1-last-name form-control" id="f1-date_nasc" name="date_nasc" placeholder="date de naissance">
                        </div>
                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-lieu" name="lieu" placeholder="lieu de naissance">
                        </div>
                        <div class="f1-buttons">
                            <button type="button" class="btn btn-next">Next</button>
                        </div>
                    </fieldset>

                    <fieldset>
                        <h4>saisissez vos informations de contacts:</h4>
                        <div class="form-group">
                            <input type="text"  name="adresse" placeholder="adresse..." class="f1-first-name form-control" id="f1-first-adresse">
                        </div>
                        <div class="form-group">
                            <input type="text"  name="ville" placeholder="ville..." class="f1-last-name form-control" id="f1-ville">
                        </div>

                        <div class="form-group">
                            <input type="tel"  class="f1-last-name form-control" id="f1-telfixe" name="telfixe" placeholder="telephone fixe">
                        </div>
                        <div class="form-group">
                            <input type="tel"  class="f1-last-name form-control" id="f1-telmobile" name="telmobile" placeholder="telephone mobile">
                        </div>
                        <div class="form-group">
                            <input type="email"  class="f1-last-name form-control" id="f1-email" name="email" placeholder="Email">
                        </div>
                        <div class="f1-buttons">
                            <button type="button" class="btn btn-previous">Previous</button>
                            <button type="button" class="btn btn-next">Next</button>
                        </div>
                    </fieldset>
                    <fieldset>
                        <h4>saisissez vos informations du baccalauréat:</h4>
                        <div class="form-group">
                            <input type="text"  name="diplomebac" placeholder="type du diplome..." class="f1-first-name form-control" id="f1-diplomebac">
                        </div>
                        <div class="form-group">
                            <input type="date"  name="datebac" placeholder="date d'obtention..." class="f1-last-name form-control" id="f1-datebac">
                        </div>
                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-notebac" name="notebac" placeholder="moyenne baccalauréat">
                        </div>
                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-mentionbac" name="mentionbac" placeholder="mention baccalauréat">
                        </div>
                        <div class="f1-buttons">
                            <button type="button" class="btn btn-previous">Previous</button>
                            <button type="button" class="btn btn-next">Next</button>
                        </div>
                    </fieldset>



                    <fieldset>
                        <h4>saisissez vos informations du bac+2:</h4>
                        <div class="form-group">
                            <input type="text" name="diplomebac2" placeholder="type diplomebac +2..." class="f1-email form-control" id="f1-diplomebac2">
                        </div>
                        <div class="form-group">
                            <input type="date" name="datebac2" placeholder="date d'obtention du diplome bac+2..." class="f1-password form-control" id="f1-datebac2">
                        </div>

                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-filierebac2" name="filierebac21" placeholder="filiere bac+2">
                        </div>

                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-notes1" name="notes1" placeholder="note semestre 1">
                        </div>

                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-annotes1" name="annotes1" placeholder="année de validation semestre 1">
                        </div>


                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-notes2" name="notes2" placeholder="note semestre 2">
                        </div>

                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-annotes2" name="annotes2" placeholder="année de validation semestre 2">
                        </div>


                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-notes3" name="notes3" placeholder="note semestre 3">
                        </div>

                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-annotes3" name="annotes3" placeholder="année de validation semestre 3">
                        </div>


                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-notes4" name="notes4" placeholder="note semestre 4">
                        </div>

                        <div class="form-group">
                            <input type="text"  class="f1-last-name form-control" id="f1-annotes4" name="annotes4" placeholder="année de validation semestre 4">
                        </div>

                        <div class="f1-buttons">
                            <button type="button" class="btn btn-previous">Previous</button>
                            <button type="button" class="btn btn-next">Next</button>
                        </div>
                    </fieldset>

                    <fieldset>
                        <h4>choisissez votre option pour la licence:</h4>
                        <div class="form-group">
                            <label class="sr-only" for="f1-filierelp">Filiere LP</label>
                            <input type="text" name="filierelp" placeholder="filiere LP..." class="f1-facebook form-control" id="f1-filierelp">
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
<script src="assets/js/jquery-1.11.1.min.js"></script>
<script src="assets/bootstrap/js/bootstrap.min.js"></script>
<script src="assets/js/jquery.backstretch.min.js"></script>
<script src="assets/js/retina-1.1.0.min.js"></script>
<script src="assets/js/scripts.js"></script>

<!--[if lt IE 10]>
<script src="assets/js/placeholder.js"></script>
<![endif]-->

</body>

</html>