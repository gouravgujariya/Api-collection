import requests


def enhance_image(api_url, image_path, sharpness=1.0, color=1.0, noise_reduction=False):
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        # Prepare additional parameters
        data = {
            'sharpness': sharpness,
            'color': color,
            'noise_reduction': noise_reduction
        }

        response = requests.post(api_url, files=files, data=data)

        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print("Error:", response.json())


if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/enhance-image/"  # Replace with your API URL
    image_path = "C:\\Users\\ergou\\PycharmProjects\\pythonProject\\image_enhancement\\1533.jpg"  # Replace with the path to your image file

    # Set enhancement parameters
    sharpness = 1.5  # Example value
    color = 1.2  # Example value
    noise_reduction = True  # Example flag

    enhance_image(api_url, image_path, sharpness, color, noise_reduction)
