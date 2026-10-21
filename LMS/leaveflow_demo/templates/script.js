const form = document.getElementById("leaveForm");
const message = document.getElementById("message");

form.addEventListener("submit", function(event) {
    event.preventDefault();
    const name =
        document.getElementById("employeeName").values;
    
    const startDate = document.getElementById("startDate").values;
    const endDate = document.getElementById("endDate").values;

    if (endDate < startDate) {
        message.textContent = "End date cannot be before start date!";

        message.style.color = "red";
        return;
    }

    message.textContent = "Application submitted successfully for " + name;
    message.style.color = "green"
});