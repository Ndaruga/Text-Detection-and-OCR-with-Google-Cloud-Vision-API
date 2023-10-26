# Text detection with OCR using Vision API


This project demonstrates how to use the Google Cloud Vision API to extract text from images using Python. You can find the code and instructions for running the project in this repository.

## Features
- Detect text from local images.
- Extract and print the detected text descriptions.
- (Optional) Analyze images from URLs (not implemented in this repository version).

## Technologies
- Python or Java
- Google Cloud Vision API


## Requirements
- Python 3.x
- Google Cloud account with billing enabled
- API key for Google Cloud Vision API (see "Setup" section)

Setup
1. Install Python libraries:
2. Enable the Google Cloud Vision API:
- Go to the Google Cloud Console (https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Enable the Google Cloud Vision API for your project.
- Create an API key and save it securely.

3. (Optional) Set environment variable:
- Export the API key as an environment variable named
- `GOOGLE_APPLICATION_CREDENTIALS`. This can be done in your terminal or by setting a system environment variable.

4. Download pre-trained model (optional):
- This project does not require any additional model downloads.


## Usage
1. Local image detection:
- Place your image files in the Python/Test-images folder.
- Run the test-image.py script:

    ```
    python test-image.py
    ```

2. (Optional) URL-based detection:
- Modify the analyze_image_from_uri function in text_detection.py to accept a URL as input.
- Configure the function with your desired image URL and feature types.
- Uncomment the relevant code to print the extracted text.


## Contributing
I welcome contributions to this project! Please clone the repository and create a new branch. Once you have a contiution create a PR

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Additional Notes
For more information on the Google Cloud Vision API, please refer to the official documentation: https://cloud.google.com/vision/docs/
