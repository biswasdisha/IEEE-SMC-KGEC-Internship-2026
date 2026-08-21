import os
import uuid
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from predict import predict_image

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
app.secret_key = "pneumonia-detection-project-secret"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        flash("Please upload a chest X-ray image first.", "danger")
        return redirect(url_for("home"))

    file = request.files["image"]
    if file.filename == "":
        flash("No image selected. Please choose a file.", "danger")
        return redirect(url_for("home"))

    if not allowed_file(file.filename):
        flash("Unsupported file type. Please upload a JPG, JPEG, or PNG image.", "danger")
        return redirect(url_for("home"))

    filename = secure_filename(file.filename)
    stem = Path(filename).stem
    ext = Path(filename).suffix.lower()
    unique_name = f"{stem}_{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)

    try:
        file.save(file_path)
        prediction, confidence = predict_image(file_path)
    except Exception as exc:  # pragma: no cover - runtime safety
        flash(f"Prediction failed: {exc}", "danger")
        return redirect(url_for("home"))

    image_url = url_for("static", filename=f"uploads/{unique_name}")
    return render_template(
        "result.html",
        image_url=image_url,
        prediction=prediction,
        confidence=confidence,
    )


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.errorhandler(413)
def file_too_large(_error):
    flash("The uploaded image is too large. Please use a file smaller than 16MB.", "danger")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
