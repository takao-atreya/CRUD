const form = document.getElementById("leaveForm");
const message = document.getElementById("message");

form.addEventListener("submit", function(event) {
    event.preventDefault();
    const name =
        document.getElementById("employeeName").value;
    
    const empID = document.getElementById("employeeID").value;

    console.log("Submit event triggered!");
    console.log("Employee ID:", empID);
    console.log("Employee ID length:", empID.trim().length);
   
    if(empID.trim().length === 5) {
        message.textContent = "Invalid ID!"
        message.style.color = "red";

        return;
    }
    
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;

    if (endDate < startDate) {
        message.textContent = "End date cannot be before start date!";

        message.style.color = "red";
        return;
    }

    message.textContent = "Application submitted successfully for " + name;
    message.style.color = "green"
});
