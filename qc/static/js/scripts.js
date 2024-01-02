function showSection(section) {
                
    // Find section text from server
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => {
        // Log text and display on page
        console.log(text);
        document.querySelector('#content').innerHTML = text;
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Add button functionality
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            showSection(this.dataset.section);
        };
    });
});