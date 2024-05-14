<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="description" content=" Intro section with dropdown navigation - Frontend Mentor">
  <meta name="keywords" content=" Intro section with dropdown navigation,Frontend Mentor ">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" sizes="32x32" href="./images/favicon-32x32.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jersey+10+Charted&family=Teko:wght@300..700&display=swap"
    rel="stylesheet">
  <title>Our Team</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
  <link rel="stylesheet" type="text/css" href="ourTeam.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

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
              <a href="/">Automated Discovery</a>
            </li>
            <li>
              <!-- <img src="./images/icon-calendar.svg" alt="" aria-hidden="true" width="15" height="15" />  -->
              <a href="scanner.html">Vunnerability Detection</a>
            </li>
            <li>
              <!-- <img src="./images/icon-reminders.svg" alt="" aria-hidden="true" width="15" height="15" />  -->
              <a href="/">Risc Assessment</a>
            </li>
            <li>
              <!-- <img src="./images/icon-planning.svg" alt="" aria-hidden="true" width="15" height="15" /> -->
              <a href="/">Reporting</a>
            </li>
          </ul>
        </li>
        <li class="company-btn">
          <button>Company
            <img src="./images/icon-arrow-down.svg" alt="" aria-hidden="true" />
          </button>
          <ul class="hidden-company">
            <li><a href="/">History</a></li>
            <li><a href="ourTeam.html">Our Team</a></li>
            <li><a href="/">Blog</a></li>
          </ul>
        </li>
        <li><a href="/">Careers</a></li>
        <li><a href="/">About</a></li>
      </ul>
      <ul class="nav-buttons nav-menu">
        <li><a href="Login.php"><button>LOGOUT</button></a></li>
        <!-- <li><button>Register</button></li> -->
      </ul>
    </nav>
  </header>
  <main>
    <img class="hero" src="./images/image-hero-mobile.png" alt="Man with laptop" />
    <section class="remote">
      <section class="remote-information">
        <div class="scan">
            <div class="input-group input-group-lg">
                <!-- <span class="input-group-text" id="inputGroup-sizing-lg">Large</span> -->
                <input type="text" class="scanInput form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
            </div>
            <button type="button" class="btn mt-3 btn-primary btn-sm">Sql Injection</button>
            <button type="button" class="btn mt-3 btn-primary btn-sm">Scan Now</button>
        </div>

      </section>
    </section>
  </main>
  <script src="app.js"></script>
</body>

</html>