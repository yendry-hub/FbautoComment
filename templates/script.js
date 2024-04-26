const sidebar = document.querySelector('.sidebar');
const content = document.querySelector('.content');
const sidebarToggleButton = document.querySelector('.sidebar-toggle'); // Add a toggle element

let isSidebarHidden = false; // Track sidebar state
let clickTimeout; // Timeout to handle rapid clicks

function showSection(sectionId) {
    const sections = document.querySelectorAll('.content-section');
    const links = document.querySelectorAll('.sidebar a');
    sections.forEach(section => section.classList.remove('active'));
    links.forEach(link => link.classList.remove('active'));
    document.getElementById(sectionId).classList.add('active');
    document.querySelector(`.sidebar a[href="#${sectionId}"]`).classList.add('active');
}

function toggleSidebarHide() {
    if (!isSidebarHidden) {
        isSidebarHidden = true;
        sidebar.classList.add('hidden');
        sidebar.style.opacity = 0;
    }
}

function toggleSidebarShow() {
    if (isSidebarHidden) {
        isSidebarHidden = false;
        sidebar.classList.remove('hidden');
        sidebar.style.opacity = 1;
    }
}

// Inside toggleSidebarHide and toggleSidebarShow functions (optional)
if (isSidebarHidden) {
    sidebar.style.opacity = 0; // Optional: Set opacity to 0 for a fade-out effect
  } else {
    sidebar.style.opacity = 1; // Optional: Restore opacity to 1
  }
  
// Event Listeners
content.addEventListener('click', toggleSidebarHide); // Click anywhere in content hides sidebar

if (sidebarToggleButton) { // If toggle element exists
  sidebarToggleButton.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default behavior for toggle button clicks
    if (isSidebarHidden) {
      toggleSidebarShow();
    } else {
      toggleSidebarHide();
    }
  });
}

function submitLink() {
    // Implement your link submission logic here
    const linkText = document.getElementById('link-text').value;
    console.log("Submitted Link:", linkText);
    // Clear the textbox after submission
    document.getElementById('link-text').value = '';
}

// Add event listener for form submission (placeholder)
const dataForm = document.getElementById('data-form');
if (dataForm) {
    dataForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Implement your form submission logic here
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const comment = document.getElementById('comment').value;
        console.log("Submitted Data:", { username, password, comment });
        // You can add logic to process the form data (e.g., send to server)
    });
}
