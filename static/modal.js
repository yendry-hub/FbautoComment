var currentIndex = 2; // Start from the second row (index 1) since the first row is headers

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  // Get the data from the first row of the table
  //var rowData = document.querySelector("#tableContent tr:nth-child(2)").children;
  // Get the data from the current row of the table
  var rowData = document.querySelector("#tableContent tr:nth-child(" + currentIndex + ")").children;

  // Populate the inputs in the modal with the data
  document.getElementById("modalId").value = rowData[0].textContent;
  document.getElementById("modalName").value = rowData[1].textContent;
  document.getElementById("modalPhone").value = rowData[2].textContent;
  document.getElementById("modalPassword").value = rowData[3].textContent;
  document.getElementById("modalComment").value = rowData[4].textContent;
  
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Define a variable to keep track of the current index
var currentIndex = 1;

// Function to submit the next row
function submitNextRow() {
  // Get the data from the next row of the table
  var nextRowData = document.querySelector("#tableContent tr:nth-child(" + currentIndex + ")").children;

  // Populate the inputs in the modal with the data
  document.getElementById("modalName").value = nextRowData[1].textContent;
  document.getElementById("modalPhone").value = nextRowData[2].textContent;
  document.getElementById("modalPassword").value = nextRowData[3].textContent;
  document.getElementById("modalComment").value = nextRowData[4].textContent;

  // Submit the form asynchronously using AJAX
  var formData = new FormData(document.getElementById("modalForm"));
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/open_website");
  xhr.send(formData);

  // Move to the next row
  currentIndex++;

  // Check if there are more rows to process
  if (currentIndex <= document.querySelectorAll("#tableContent tr").length) {
    // Continue to submit the form for the next row after 1 second
    setTimeout(submitNextRow, 1000);
  } else {
    // If there are no more rows, close the modal
    document.getElementById("myModal").style.display = "none";
  }
}

// Attach event listener to the form submission
document.getElementById("modalForm").onsubmit = function (event) {
  event.preventDefault(); // Prevent the form from submitting traditionally

  // Submit the form for the current row
  submitNextRow();
};
