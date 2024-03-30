import { streamGemini } from './gemini-api.js';

let form = document.querySelector('form');
let promptInput = document.querySelector('input[name="prompt"]');
let output = document.querySelector('.output');

form.onsubmit = async (ev) => {
  ev.preventDefault();
  output.textContent = 'Generating...';

  try {
    // Load the image as a base64 string
    let imageUrl = form.elements.namedItem('chosen-image').value;
    let imageBase64 = await fetch(imageUrl)
      .then(r => r.arrayBuffer())
      .then(a => base64js.fromByteArray(new Uint8Array(a)));

    // Assemble the prompt by combining the text with the chosen image
    let contents = [
      {
        role: 'user',
        parts: [
          { inline_data: { mime_type: 'image/jpeg', data: imageBase64, } },
          { text: promptInput.value }
        ]
      }
    ];

    // Call the gemini-pro-vision model, and get a stream of results
    let stream = streamGemini({
      model: 'gemini-pro-vision',
      contents,
    });

    // Read from the stream and interpret the output as markdown
    let buffer = [];
    let md = new markdownit();
    for await (let chunk of stream) {
      buffer.push(chunk);
      output.innerHTML = md.render(buffer.join(''));
    }
  } catch (e) {
    output.innerHTML += '<hr>' + e;
  }
};
if ('webkitSpeechRecognition' in window) {
  var recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;

  var microphone = document.getElementById('microphone');
  var transcript = document.getElementById('transcript');

  microphone.addEventListener('click', function() {
    recognition.start();
  });

  recognition.onresult = function(event) {
    for (var i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        transcript.value += event.results[i][0].transcript;
      }
    }
  };

  recognition.onerror = function(event) {
    console.log('Error occurred in recognition: ' + event.error);
  }
} else {
  console.log('SpeechRecognition interface not available');
}
// Check if the browser supports the SpeechRecognition interface
if ('webkitSpeechRecognition' in window) {
  var recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;

  var microphone = document.getElementById('microphone');
  var stopButton = document.getElementById('stop');
  var transcript = document.getElementById('transcript');

  microphone.addEventListener('click', function() {
    recognition.start();
  });

  stopButton.addEventListener('click', function() {
    recognition.stop();
  });

  recognition.onresult = function(event) {
    for (var i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        transcript.value += event.results[i][0].transcript;
      }
    }
  };

  recognition.onerror = function(event) {
    console.log('Error occurred in recognition: ' + event.error);
  }
} else {
  console.log('SpeechRecognition interface not available');
}