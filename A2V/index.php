<?php
session_start();
// if(isset($_SESSION['loggedin'])|| $_SESSION['loggedin']!=true){
//   header("location: Login.php");
//   exit;
// }


?>


<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="description" content=" Intro section with dropdown navigation - Frontend Mentor">
  <meta name="keywords" content=" Intro section with dropdown navigation,Frontend Mentor ">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" sizes="32x32" href="./images/favicon-32x32.png">
  <title>A2V Scanner - <?php $_SESSION['Username']?></title>
  <link rel="stylesheet" type="text/css" href="styles.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <header class="header">
    <h1>
      <a href="/">
        <img class="logo" src="./images/LOGO1.png" alt="Snap icon" />
      </a>
    </h1>
    <img class="hamburger" src="./images//icon-menu.svg" alt="" aria-hidden="true" />
    <nav class="menu">
      <ul class="nav-menu">
        <li class="features-btn">
          <button>Features
            <img src="./images/icon-arrow-down.svg" alt="" aria-hidden="true" /></button>
          <ul class="hidden-features">
            <li>
              <!-- <img src="./images/icon-todo.svg" alt="" aria-hidden="true" width="15" height="15" /> -->
              <a href="/">Automated Discovery</a></li>
                <li>
                  <!-- <img src="./images/icon-calendar.svg" alt="" aria-hidden="true" width="15" height="15" />  -->
                  <a href="scanner.php">Vunnerability Detection</a></li>
            <li>
              <!-- <img src="./images/icon-reminders.svg" alt="" aria-hidden="true" width="15" height="15" />  -->
              <a href="/">Risc Assessment</a></li>
            <li>
              <!-- <img src="./images/icon-planning.svg" alt="" aria-hidden="true" width="15" height="15" /> -->
                <a href="/">Reporting</a></li>
          </ul>
        </li>
        <li class="company-btn">
          <button>Company
            <img src="./images/icon-arrow-down.svg" alt="" aria-hidden="true" />
          </button>
          <ul class="hidden-company">
            <li><a href="/">History</a></li>
            <li><a href="ourTeam.php">Our Team</a></li>
            <li><a href="/">Blog</a></li>
          </ul>
        </li>
        <li><a href="/">Careers</a></li>
        <li><a href="/">About</a></li>
      </ul>
      <ul class="nav-buttons nav-menu">

      WELCOME TO OUR WEBSITE
        <li><a href="Login.php"><button>LOGOUT</button></a></li>

        <!-- <li><button>Register</button></li> -->
      </ul>
    </nav>
  </header>
  <main>
    <img class="hero" src="./images/image-hero-mobile.png" alt="Man with laptop" />
    <section class="remote">
      <section class="remote-information">
        <h2>Secure Your Website</h2>
        <p>Through the scanner’s eye, no bug can hide,
          A silent guardian, in bytes we confide.</p>
          <form action="scanner.html" method="get">
            <!-- <button class="btn" type="submit">Go to HTML Page</button> -->
            <button type="submit" class="submit ">Start Scanning</button>
          </form>
        <!-- <a href="">Scan Your Website</a> -->
      </section>
      <!-- <section class="partners">
        <img src="./images/client-databiz.svg" alt="Databiz logo">
        <img src="./images/client-audiophile.svg" alt="Audiophile logo">
        <img src="./images//client-meet.svg" alt="Meet logo">
        <img src="./images//client-maker.svg" alt="Maker logo">
      </section> -->
    </section>
  </main>
  <script src="app.js"></script>
</body>

</html>