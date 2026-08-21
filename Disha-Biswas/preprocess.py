from PIL import Image
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input


IMAGE_SIZE = (224, 224)


def preprocess_image(image_path: str) -> np.ndarray:
    """Load, resize, and normalize an image for ResNet50 inference."""
    image = Image.open(image_path).convert("RGB")
    image = image.resize(IMAGE_SIZE)
    image_array = np.array(image, dtype=np.float32)
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array
