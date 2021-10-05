<?php
// database connection code
if(isset($_POST['txtName']))
{
$username = alth9061; 
$password = CSPBdb4fr33!;
$host = "db4free.net:3306"; 
// $host = "db4free.net"; 
// $host = "85.10.205.173:3306";
$dbname = db_connect_mt; 

$options = array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8'); 

try 
{ 
	$db = new PDO("mysql:host={$host};dbname={$dbname};charset=utf8", $username, $password, $options); 
} 
catch(PDOException $ex) 
{ 
	die("Failed to connect to the database: " . $ex->getMessage()); 
} 
// $con = mysqli_connect('localhost', 'root', '','db_connect');
// get the post records

$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtEmail'];
$txtPhone = $_POST['txtPhone'];
$txtMessage = $_POST['txtMessage'];

// database insert SQL code
$sql = "INSERT INTO `tbl_contact` (`Id`, `fldName`, `fldEmail`, `fldPhone`, `fldMessage`) VALUES ('0', '$txtName', '$txtEmail', '$txtPhone', '$txtMessage')";

// insert in database 
$rs = mysqli_query($con, $sql);
if($rs)
{
	echo "Contact Records Inserted";
}
}
else
{
	echo "Are you a genuine visitor?";
	
}
?>