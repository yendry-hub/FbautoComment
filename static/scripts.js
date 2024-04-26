function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("sidebar-show");
}

function showAddForm() {
  document.getElementById("addForm").style.display = "block";
  document.getElementById("tableContent").style.display = "none";
  document.getElementById("sidebar").classList.remove("sidebar-show");
}

function showTable() {
  document.getElementById("addForm").style.display = "none";
  document.getElementById("tableContent").style.display = "table";
  document.getElementById("sidebar").classList.remove("sidebar-show");
}

function editEntry(id) {
  window.location.href = '/edit/' + id;
}

function deleteEntry(id) {
  if (confirm("Are you sure you want to delete this entry?")) {
    window.location.href = '/delete/' + id;
  }
}

// Hide sidebar when clicking outside of it
document.addEventListener("click", function (event) {
  var sidebar = document.getElementById("sidebar");
  var toggleButton = document.querySelector(".sidebar-toggle");
  var isClickInsideSidebar = sidebar.contains(event.target);
  var isClickInsideToggleButton = toggleButton.contains(event.target);

  if (!isClickInsideSidebar && !isClickInsideToggleButton) {
    sidebar.classList.remove("sidebar-show");
  }
});

function disableButton() {
  // Disable the button
  document.getElementById("submitButton").disabled = true;

  // Optionally, you can submit the form here if needed
  // document.getElementById("myForm").submit();
}
