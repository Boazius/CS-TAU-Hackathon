document.querySelectorAll('img').forEach(img => {
    // Create a canvas to draw the image
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    
    // Set canvas dimensions to match the image
    canvas.width = img.width;
    canvas.height = img.height;
    
    // Draw the image onto the canvas
    context.drawImage(img, 0, 0);
    
    // Convert the canvas to a Base64-encoded string
    const imageData = canvas.toDataURL('image/png');
    
    // Send the image data to the background script
    chrome.runtime.sendMessage({ type: 'PROCESS_IMAGE', imageData }, (response) => {
      if (response.containsElement) {
        const overlay = document.createElement('div');
        overlay.style.width = img.width + 'px';
        overlay.style.height = img.height + 'px';
        overlay.style.backgroundColor = 'black';
        overlay.style.color = 'white';
        overlay.style.position = 'absolute';
        overlay.style.top = img.offsetTop + 'px';
        overlay.style.left = img.offsetLeft + 'px';
        overlay.textContent = `Element: ${response.element}`;
        img.replaceWith(overlay);
      }
    });
  });
  