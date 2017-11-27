<?php
    $servername = "localhost";
    $username = "root";
    $password = "passwordbaru";
    $dbname = "AugmentedDB";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 

    $sql = "SELECT user_name, user_SID, user_role, user_marker FROM tbl_user";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            echo "<br> Name: ". $row["user_name"]. " - SID: ". $row["user_SID"]. " " . $row["user_role"] . "<br>";
        }
    } else {
        echo "0 results";
    }

    $conn->close();
?> 