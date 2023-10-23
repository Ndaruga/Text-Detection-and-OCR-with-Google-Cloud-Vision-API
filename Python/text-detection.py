from typing import Sequence
from google.cloud import vision
from PIL import Image
import io
import re


def analyze_image_from_uri(image_uri: str, feature_types: Sequence) -> vision.AnnotateImageResponse:
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(image_uri, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    # image.source.image_uri = image_uri
    features = [vision.Feature(type_=feature_type) for feature_type in feature_types]
    request = vision.AnnotateImageRequest(image=image, features=features)

    response = client.annotate_image(request=request)

    return response


# def print_text(response: vision.AnnotateImageResponse):
#     print("=" * 80)
        
#     for annotation in response.text_annotations:
#         vertices = [f"({v.x},{v.y})" for v in annotation.bounding_poly.vertices]
#         print(
#             f"{repr(annotation.description):42}",
#             ",".join(vertices),
#             sep=" | ",
#         )


image_uri = "Python/Test-images/IMG_20221106_111206.jpg"
# img = Image.open(image_uri)
# img.show()
features = [vision.Feature.Type.TEXT_DETECTION]

response = analyze_image_from_uri(image_uri, features)
# print("*" * 80)
print(response.text_annotations[0].description)
# print_text(response)