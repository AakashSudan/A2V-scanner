<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "users";

$conn = mysqli_connect($servername, $username, $password, $database);
if (!$conn){
    die("Sorry we failed to connect: ". mysqli_connect_error());
}
$Username="admin";
$password="admin";
$email="";
$login=false;
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    $Username = $_POST['Username'];
    $password = $_POST['password'];
    // echo "Your Email is $email and password is $password";
}




$sql = "Select * from users where username = '$Username' AND password = '$password'";
$result = mysqli_query($conn,$sql);
$num = mysqli_num_rows($result);
// echo "$num";
if ($num == 1){
    $login == true;
    // session_start();
    // $_SESSION['loggedin'] = true;
    // $_SESSION['Username'] = $username;
    header("location: index.php");
}
else{
    $showError = "Invalid Credentials";
    // echo "<h1>INVALID CREDENTIALS</h1>";
}





// $num = mys
// $result = mysqli_query($conn, $sql);


?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SignIn&SignUp</title>
    <link rel="stylesheet" type="text/css" href="./style.css" />
    <script
      src="https://kit.fontawesome.com/64d58efce2.js"
      crossorigin="anonymous"
    ></script>
  
  </head>
  <body>
    <div class="container">
      <div class="forms-container">
        <div class="signin-signup">
          <form action="\A2V Scanner\Login.php" method="post" class="sign-in-form">
            <h2 class="title">Sign In</h2>
            <div class="input-field">
              <i class="fas fa-user"></i>
              <input type="text" placeholder="Username" id="Username" name="Username"/>
            </div>
            <div class="input-field">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Password" id="password" name="password"/>
            </div>
            <input type="submit" value="Login" class="btn solid" />

            <p class="social-text">Or Sign in with social platforms</p>
            <div class="social-media">
              <a href="#" class="social-icon">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#" class="social-icon">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#" class="social-icon">
                <i class="fab fa-google"></i>
              </a>
              <a href="#" class="social-icon">
                <i class="fab fa-linkedin-in"></i>
              </a>
            </div>
            
          </form>
        </div>
      </div>
      <div class="panels-container">
        <div class="panel left-panel">
            <div class="content">
                <h3>New here?</h3>
                <p>Create your Account.</p>
                <a href="http://localhost/A2V%20Scanner/SignUp.php"><button class="btn transparent" id="sign-up-btn">Sign Up</button></a>
            </div>
            <img src="./img/log.svg" class="image" alt="">
        </div>

        <div class="panel right-panel">
            <div class="content">
                <h3>One of us?</h3>
                <p></p>
                <button class="btn transparent" id="sign-in-btn">Sign In</button>
            </div>
            <img src="./img/register.svg" class="image" alt="">
        </div>
      </div>
    </div>
 
    <script src="./app.js"></script>
  </body>
</html>