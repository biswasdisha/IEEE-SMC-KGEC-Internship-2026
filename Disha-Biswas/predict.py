import os
from typing import Tuple

import numpy as np
from tensorflow.keras.models import load_model

from utils.preprocess import preprocess_image

MODEL_PATH = os.path.join(os.path.dirname(__file__), "ResNet50_Final_Model.keras")

try:
    MODEL = load_model(MODEL_PATH, compile=False)
except Exception as exc:  # pragma: no cover - runtime safety
    MODEL = None
    MODEL_ERROR = str(exc)
else:
    MODEL_ERROR = None


def predict_image(image_path: str) -> Tuple[str, float]:
    """Predict whether an X-ray image is NORMAL or PNEUMONIA."""
    if MODEL is None:
        raise RuntimeError(
            f"Model could not be loaded: {MODEL_ERROR or 'Unknown error'}"
        )

    image_array = preprocess_image(image_path)
    prediction = MODEL.predict(image_array, verbose=0)

    prediction_array = np.asarray(prediction).reshape(-1)
    if prediction_array.size == 1:
        score = float(prediction_array[0])
        label = "PNEUMONIA" if score >= 0.5 else "NORMAL"
        confidence = abs(score) * 100
    else:
        predicted_index = int(np.argmax(prediction_array))
        score = float(prediction_array[predicted_index])
        label = "PNEUMONIA" if predicted_index == 1 else "NORMAL"
        confidence = score * 100

    confidence = max(0.0, min(100.0, confidence))
    return label, round(confidence, 2)
