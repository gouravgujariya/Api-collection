
```markdown
# Image Enhancement API

This project implements an Image Enhancement API using FastAPI and OpenCV. The API provides various image enhancement functionalities, including sharpening, color enhancement, and noise reduction.

## Features

- Upload an image to the API.
- Enhance image quality with the following options:
  - **Sharpening**: Increase the sharpness of the image.
  - **Color Enhancement**: Adjust the color saturation of the image.
  - **Noise Reduction**: Remove noise from the image.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- OpenCV
- Pillow
- Requests (for the client)

You can install the required libraries using pip:

```bash
pip install fastapi uvicorn opencv-python pillow requests
```

## API Endpoints

### Enhance Image

**POST** `/enhance-image/`

#### Request

- **Form Data**:
  - `file`: The image file to enhance (required).
  - `sharpness`: A float value for sharpening (default: 1.0).
  - `color`: A float value for color enhancement (default: 1.0).
  - `noise_reduction`: A boolean value to apply noise reduction (default: False).

#### Response

- **200 OK**: Returns the enhanced image as a JSON response containing the enhanced image URL or base64-encoded image.
- **400 Bad Request**: Returns an error message if the input is invalid.

### Example Request

You can use the provided client script to interact with the API.

```python
import requests

def enhance_image(api_url, image_path, sharpness=1.0, color=1.0, noise_reduction=False):
    # Function implementation...

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/enhance-image/"  # Replace with your API URL
    image_path = "path/to/your/image.jpg"  # Replace with the path to your image file

    # Set enhancement parameters
    sharpness = 1.5  # Example value
    color = 1.2      # Example value
    noise_reduction = True  # Example flag

    enhance_image(api_url, image_path, sharpness, color, noise_reduction)
```

## Running the API

1. Save the main API code to a file, for example, `main.py`.
2. Run the FastAPI server with the following command:

   ```bash
   uvicorn main:app --reload
   ```

3. Access the API documentation at `http://127.0.0.1:8000/docs` to view available endpoints and test the API.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

- [gourav](https://github.com/gouravgujariya)
```

### Instructions for Use
- **Replace Placeholder Text**: Be sure to replace `[Your Name](https://github.com/yourusername)` with your actual name and GitHub link.
- **Add Additional Details**: Feel free to add any additional sections or details that you think may be relevant, such as troubleshooting steps, FAQs, or more detailed usage examples.
- **Saving the File**: Save this content in a file named `README.md` in the root directory of your project.

This README provides a comprehensive overview of your project, making it easier for users to understand its functionality and how to get started. Let me know if you need any changes or additional sections!
