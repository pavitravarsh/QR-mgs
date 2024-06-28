// static/scripts.js
$(document).ready(function () {
  $("#messageForm").submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    var magicalWord = $("#magicalWord").val();
    var message = $("#message").val();

    // Send data to backend via AJAX POST request
    $.ajax({
      type: "POST",
      url: "/api/save-message",
      contentType: "application/json",
      data: JSON.stringify({ magicalWord: magicalWord, message: message }),
      success: function (response) {
        alert("Message saved successfully!");
        // Optionally clear form fields or perform other actions
        $("#magicalWord").val("");
        $("#message").val("");
      },
      error: function (error) {
        console.error("Error saving message:", error);
        alert("Failed to save message.");
      },
    });
  });
});
