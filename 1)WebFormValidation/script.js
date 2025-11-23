function submitForm(event) {
    event.preventDefault(); // Prevent the form from reloading the page

    // Get values entered by the user
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let dob = document.getElementById("dob").value;
    let pw = document.getElementById("pw").value;

    // Check all fields and if it is all empty
    if (!name || !email || !dob || !pw) {
        alert("Please fill in all fields.");
        return;
    }

    // Email check (must contain @ and .)
    if (!email.includes("@") || !email.includes(".")) {
        alert("Enter a valid email.");
        return;
    }

    // Password check
    if (pw.length < 8) { //Checking if length is 
        alert("Password must be at least 8 characters.");
        return;
    }

    // Check password contains at least one letter and one number using regex
    let hasLetter = /[a-zA-Z]/.test(pw);
    let hasNumber = /\d/.test(pw);

    if (!hasLetter || !hasNumber) {
        alert("Password must contain at least one letter and one number.");
        return;
    }

    // Hide the form
    document.getElementById("formDiv").style.display = "none";

    // Show the user-entered information    
    let infoDiv = document.getElementById("infoDiv");
    infoDiv.innerHTML = `<h2>Your Entered Information</h2>
                         <b>Name:</b> ${name}<br>
                         <b>Email:</b> ${email}<br>
                         <b>Date of Birth:</b> ${dob}<br>`;
    infoDiv.style.display = "block"; // Make it visible
}