// app.js

document.getElementById('convertButton').addEventListener('click', function() {
    var text = document.getElementById('textInput').value;
    fetch('/convert-to-speech', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.blob())
    .then(blob => {
        var url = URL.createObjectURL(blob);
        document.getElementById('audioPlayer').src = url;
    })
    .catch(error => console.error('Error:', error));
});
