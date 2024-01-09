
document.addEventListener('DOMContentLoaded', function() {
    // Add click event listeners to buttons
    document.querySelectorAll('button[data-section]').forEach(button => {
        button.onclick = function() {
            const sectionId = this.dataset.section;
            fetchContent(sectionId);
        };
    });
});

function fetchContent(sectionId) {
    // Fetch content for the given sectionId
    fetch(`/section/${sectionId}/`)
        .then(response => response.text())
        .then(text => {
            // Update the content div with the fetched text
            document.getElementById('content').innerHTML = text;
        })
        .catch(error => {
            console.error('Error fetching content:', error);
        });
}
