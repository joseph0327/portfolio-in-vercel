document.addEventListener("DOMContentLoaded", () => {
    const dropdown = document.querySelector(".dropdown-container");
    const toggle = dropdown.querySelector(".dropdown-toggle");
  
    // Toggle the dropdown menu on click
    toggle.addEventListener("click", (event) => {
      event.preventDefault(); // Prevent the default link behavior
      dropdown.classList.toggle("active");
    });
  
    // Close the dropdown menu if clicked outside
    document.addEventListener("click", (event) => {
      if (!dropdown.contains(event.target)) {
        dropdown.classList.remove("active");
      }
    });
  });


  //---------------------------------
