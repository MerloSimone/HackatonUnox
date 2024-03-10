<?php
// Connect to the database (replace with your actual credentials)
$mysqli = new mysqli("89.40.142.15", "acme_user", "acme_user", "unox");


// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

// Fetch data from the database
$query = "SELECT LOWER(summary) AS summary, COUNT(*) AS messageCount FROM messages GROUP BY LOWER(summary)";
$result = $mysqli->query($query);


// Convert the result to an associative array
$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}

// Close the result set
$result->close();

// Close the database connection
$mysqli->close();

// Set the Content-Type header to application/json
header('Content-Type: application/json');

// Output the JSON response
echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

?>
