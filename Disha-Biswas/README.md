# Chest X-ray Pneumonia Detection

## Project Overview
This Flask web application uses a trained TensorFlow/Keras deep learning model to classify chest X-ray images as either NORMAL or PNEUMONIA. The project is designed as a professional B.Tech final year project demo with a modern medical-themed interface.

## Features
- Upload chest X-ray images in JPG, JPEG, or PNG format
- Preview uploaded images before prediction
- Run inference using a trained ResNet50-based Keras model
- Display prediction label and confidence score
- Responsive Bootstrap 5 user interface
- About page with project background and technology details

## Folder Structure
```text
Pneumonia_Detection/
│── app.py
│── predict.py
│── requirements.txt
│── README.md
│── ResNet50_Final_Model.keras
├── static/
│   ├── css/
│   ├── uploads/
│   └── images/
├── templates/
│   ├── index.html
│   ├── result.html
│   └── about.html
└── utils/
    └── preprocess.py
```

## Installation
1. Create and activate a virtual environment (recommended).
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
```bash
python app.py
```
Then open your browser at:
```text
http://127.0.0.1:5000/
```

## Screenshots
- Placeholder: Add screenshots of the home page, result page, and about page here.

## Future Improvements
- Add explainable AI visualizations for model attention
- Integrate a database for storing predictions
- Add user authentication for multi-user access
- Support more medical imaging classes
