document.addEventListener("DOMContentLoaded", () => {
    console.log("LungCare AI Loaded");
});

function updateRisk(input) {
    const card = input.closest(".input-card");
    const range = card.querySelector(".range-input");
    const text = card.querySelector(".risk-text");

    let value = parseFloat(input.value);
    if (isNaN(value)) value = 0;

    range.value = value;

    if (value <= 0) {
        text.textContent = "🟢 No problem";
        text.style.color = "green";
    } 
    else if (value <= 1) {
        text.textContent = "🟡 Mid range";
        text.style.color = "goldenrod";
    } 
    else if (value <= 2) {
        text.textContent = "🟠 Problem is high";
        text.style.color = "orange";
    } 
    else {
        text.textContent = "🔴 Problem is too high";
        text.style.color = "red";
    }
}
