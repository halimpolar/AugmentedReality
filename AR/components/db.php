<?php

    $servername = "localhost";
    $username = "root";
    $password = "password";
    $dbname = "AugmentedDB";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 

    $sql = "SELECT user_name, user_SID, user_role, user_marker FROM tbl_user";
    $result = $conn->query($sql);


   $json=json_encode($result);
   echo $json;
    
?> 