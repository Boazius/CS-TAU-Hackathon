// Function to process image and send to background script
const processImage = (img, isVideoPoster = false, videoElement = null) => {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');
  canvas.width = img.width;
  canvas.height = img.height;
  context.drawImage(img, 0, 0);
  const imageData = canvas.toDataURL('image/png');
  chrome.runtime.sendMessage({ type: 'PROCESS_IMAGE', imageData }, (response) => {
      if (response.detected) {
         const text = `Contains: Horse`;
        if (isVideoPoster) {
          createSvgWithText(videoElement,text);
        } else {
          createSvgWithText(img,text);
        }
      } else {
          if (isVideoPoster) {
              videoElement.style.display = ''; // Show the video if no unwanted object is detected
          } else {
              img.style.display = ''; // Show the image if no unwanted object is detected
          }
      }
  });
};

function createSvgWithText(element, text) {
  // Create the SVG namespace
  const xmlns = "http://www.w3.org/2000/svg";
  
  // Create SVG element
  const svg = document.createElementNS(xmlns, "svg");
  const height = element.height;
  const width = element.width;
  svg.setAttribute("width", width);
  svg.setAttribute("height", height);
  svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
  
  // Create a black rectangle for the background
  const rect = document.createElementNS(xmlns, "rect");
  rect.setAttribute("width", "100%");
  rect.setAttribute("height", "100%");
  rect.setAttribute("fill", "black");
  svg.appendChild(rect);
  
  // Create text element
  const textElement = document.createElementNS(xmlns, "text");
  textElement.setAttribute("x", "50%");
  textElement.setAttribute("y", "50%");
  textElement.setAttribute("text-anchor", "middle");
  textElement.setAttribute("dominant-baseline", "middle");
  textElement.setAttribute("fill", "white");
  textElement.setAttribute("font-size", "24"); // Adjust font size as needed
  
  // Set the text content
  textElement.textContent = text;
  
  // Append text to SVG
  svg.appendChild(textElement);
  
  // Serialize SVG to string
  const serializer = new XMLSerializer();
  const svgString = serializer.serializeToString(svg);
  const parent = element.parentElement;
  parent.innerHTML = svgString;
}


// Process all images
document.querySelectorAll('img').forEach(img => {
  img.style.display = 'none'; // Hide the image initially
  img.crossOrigin = 'Anonymous';

  const handleImageLoad = () => processImage(img);
  img.onload = handleImageLoad;

  // Check if the image is already loaded
  if (img.complete) {
      handleImageLoad();
  }
});

// Process all videos
document.querySelectorAll('video').forEach(video => {
  video.style.display = 'none'; // Hide the video initially

  const img = new Image();
  img.src = video.poster;
  img.crossOrigin = 'Anonymous';

  const handlePosterLoad = () => processImage(img, true, video);
  img.onload = handlePosterLoad;

  // Handle the case where the image might already be loaded when the event is added
  if (img.complete) {
      handlePosterLoad();
  }
});