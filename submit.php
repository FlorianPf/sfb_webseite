<?php 
// Error handling:
error_reporting(-1);
ini_set('display_errors', 'On');
set_error_handler("var_dump");

if(isset($_POST['submit'])){
    $to = "webmaster@schachfreunde-braunfels.de"; // this is your Email address
    $name = $_POST['name'];
    $dateofbirth = $_POST['dateofbirth'];
    $email = $_POST['email'];
    $from = $email;
    $phone = $_POST['phone'];
    $club = $_POST['club'];
    $dwz = $_POST['dwz'];
    $subject = "Anmeldung Stadtmeisterschaft";
    $message = "Name:\t\t\t" . $name . "\nGeburtsdatum:\t" . $dateofbirth . "\nE-Mail-Adresse:\t" . $email . "\nTelefonnummer:\t" . $phone . "\nVerein:\t\t\t" . $club . "\nDWZ:\t\t\t" . $dwz;

    $headers = "From:" . $from;
    mail($to,$subject,$message,$headers);
    // mail($from,$subject2,$message2,$headers2); // sends a copy of the message to the sender
    echo "Anmeldung erfolgreich!";
    // You can also use header('Location: thank_you.php'); to redirect to another page.
    // You cannot use header and echo together. It's one or the other.
    }
?>
