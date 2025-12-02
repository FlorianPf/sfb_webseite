<?php 
// Error handling:
error_reporting(-1);
ini_set('display_errors', 'On');
set_error_handler("var_dump");

if(isset($_POST['submit'])){
    $to1 = "webmaster@schachfreunde-braunfels.de";
    // $to2 = "vorstand@schachfreunde-braunfels.de";

    // Falls die Weiterleitung bei turnierleiter@schachfreunde-braunfels.de steht, können die folgenden beiden Zeilen geändert werden:.
    // $to3 = "turnierleiter@schachfreunde-braunfels.de";
    // $to3 = "adiehl1@gmx.net";

    $name = $_POST['name'];
    $dateofbirth = $_POST['dateofbirth'];
    $email = $_POST['email'];
    $from = $email;
    $phone = $_POST['phone'];
    $club = $_POST['club'];
    $dwz = $_POST['dwz'];
    $captcha = $_POST['captcha'];
    if(str_contains(strtolower($captcha), 'gukesh')) {
        $subject = "Anmeldung Stadtmeisterschaft";
        $message = "Name:\t\t\t" . $name . "\nGeburtsdatum:\t" . $dateofbirth . "\nE-Mail-Adresse:\t" . $email . "\nTelefonnummer:\t" . $phone . "\nVerein:\t\t\t" . $club . "\nDWZ:\t\t\t" . $dwz;

        $headers = "From:" . $from;
        mail($to1,$subject,$message,$headers);
        mail($to2,$subject,$message,$headers);
        mail($to3,$subject,$message,$headers);

        $fileName = "teilnehmerliste.csv";
        $data = $name . ", " . $dateofbirth . ", " . $email . ", " . $phone . ", " . $club . ", " . $dwz . "\n";
        file_put_contents($fileName, $data, FILE_APPEND);

        echo "Anmeldung erfolgreich!";
    } else {
        echo "Anmeldung fehlgeschlagen, Spam-Schutz nicht korrekt ausgefüllt!";
    }
}
?>
