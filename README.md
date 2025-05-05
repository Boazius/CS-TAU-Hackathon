# CS-TAU-Hackathon

## *CS-TAU-Hackathon* is a Chrome extension developed during the Tel Aviv University Computer Science Hackathon. The extension aims to prevent the display of unwanted images, such as graphic or pornographic content, on websites, including social media platforms. It uses a Flask backend for content processing and a front-end interface for user interaction. A PowerPoint presentation was created and actively presented during the hackathon to demonstrate the project.

## Table of Contents

- Project Overview
- Features
- Installation
- Usage
- Contributors
- Personal Contributions
- License

## Project Overview

This project was developed during the CS-TAU Hackathon on July 25-26, 2024. The core idea is a Chrome extension that filters out unwanted images (e.g., graphic or pornographic content) from websites, including social media platforms. The extension integrates a Flask-based backend for image processing and content validation, with a front-end interface for user interaction. A PowerPoint presentation was prepared and presented to showcase the project's functionality and impact.

## Features

- **Image Filtering**: Blocks unwanted images (graphic or pornographic content) on websites, including social media.
- **Chrome Extension**: Runs as a browser extension for seamless integration with web browsing.
- **Multimedia Support**: Processes images and videos, with validation for formats and sizes.
- **Video Poster Check**: Validates video posters to ensure compatibility.
- **Flask Backend**: Provides API endpoints for content processing and filtering.
- **Responsive Design**: Front-end interface adapts to various screen sizes.

## Installation

To set up the project locally and test the Chrome extension, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Boazius/CS-TAU-Hackathon.git
   cd CS-TAU-Hackathon
   ```

2. **Install Backend Dependencies**: Ensure you have Python 3.8+ installed. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**: Start the Flask server:

   ```bash
   python app.py
   ```

4. **Load the Chrome Extension**:

   - Open Chrome and navigate to `chrome://extensions/`.
   - Enable "Developer mode" in the top-right corner.
   - Click "Load unpacked" and select the project directory containing the extension files (e.g., `manifest.json`).
   - Ensure the Flask server is running for the extension to communicate with the backend.

## Usage

1. **Install the Extension**: Follow the installation steps to load the Chrome extension.
2. **Browse Websites**: Visit any website, including social media platforms, and the extension will automatically filter out unwanted images.
3. **Troubleshooting**:
   - Ensure the Flask server is running (`http://localhost:5000`).
   - Some images may fail to load due to format or size issues, as noted in commit `e284e617`.
   - Check the browser console or server logs for debugging.

## Contributors

- **Boaz Yakubov** (Boazyakubov@gmail.com)
- **Avner Fivelovich** (avner1209@gmail.com)
- **Yair Hen Zavita** (yairhenz@mail.tau.ac.il)

## Personal Contributions

### Boaz Yakubov

- **Backend Development**: Designed and implemented the Flask backend, including API endpoints for image processing and content filtering (Commits `7b8de58e`, `d031f8be`, `67767ba3`, `db3aa7ba`).
- **Performance Optimization**: Separated initialization and function calls for successive operations, reducing processing time to 0.4 seconds (Commit `d031f8be`).
- **Initial Setup**: Established the initial project structure and README (Commits `adc1eb3d`, `f22cd5e0`).
- **Core Logic**: Developed the core Python logic for image filtering and content validation (Commit `7b8de58e`).

### Avner Fivelovich

- **Chrome Extension Development**: Built the Chrome extension, including the front-end interface and content filtering logic (Commits `8b4576fe`, `364bb8fc`, `d86672cc`).
- **Content Formatting**: Updated the extension to handle formatted responses and added video poster validation (Commit `d86672cc`).
- **Bug Fixes**: Addressed rendering issues during page loading and improved image compatibility (Commit `e284e617`).
- **Presentation Support**: Contributed to the preparation of the PowerPoint presentation for the hackathon demo (Commits `c950267a`, `1694151c`).

### Yair Hen Zavita

- **Presentation Development**: Created and finalized the PowerPoint presentation for the hackathon, ensuring clear communication of the project's goals and functionality (Commits `c950267a`, `1694151c`).
- **Active Presentation**: Actively presented the project during the hackathon, effectively showcasing the Chrome extension's features and impact to judges and attendees.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
