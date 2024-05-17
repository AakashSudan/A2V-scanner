<?php
$servername = "localhost";
$username = "admin";
$password = "123456";
$database = "users";

$conn = mysqli_connect($servername, $username, $password, $database);
if (!$conn){
    die("Sorry we failed to connect: ". mysqli_connect_error());
}
$Username="";
$password="";
$email="";
$login=false;
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    $Username = $_POST['Username'];
    $password = $_POST['password'];
    // echo "Your Email is $email and password is $password";
}
?>
