chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'PROCESS_IMAGE') {
      fetch('http://localhost:5000/process_image', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ imageData: message.imageData })
      })
      .then(response => response.json())
      .then(data => {
        sendResponse(data);
      })
      .catch(error => {
        console.error('Error:', error);
        sendResponse({ error: 'Failed to process image' });
      });
  
      return true;  // Will respond asynchronously.
    }
  });
  