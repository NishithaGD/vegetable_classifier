VEGETABLE IMAGE CLASSIFIER USING CUSTOM ANN

Project Title:
Vegetable Image Classifier using a Custom Artificial Neural Network (ANN)

Description:
This project is designed to classify images of vegetables into their respective categories using a custom-built ANN model. The ANN uses fully connected layers to process flattened image inputs and outputs class predictions.

Dataset:
The dataset used for this project was downloaded from Kaggle. It contains categorized images of various vegetables organized into training and testing folders.

Model Information:
- Model Type: Artificial Neural Network (ANN)
- Framework: TensorFlow / Keras
- Input: Flattened image vectors (e.g., 64x64x3 = 12288 features)
- Output: Vegetable class label using Softmax activation
- Loss Function: Categorical Crossentropy
- Optimizer: Adam
- Metrics: Accuracy

Project Structure:
vegetable_classifier_ann/
├── dataset/
│   ├── train/
│   │   ├── tomato/
│   │   ├── carrot/
│   │   └── ... (other classes)
│   └── test/
│       ├── tomato/
│       ├── carrot/
│       └── ...
├── model/
│   └── vegetable_ann_model.h5        # Saved model file
├── main.py                           # Script for training and evaluation
├── predict.py                        # Script for loading model and making predictions
├── requirements.txt                  # List of Python dependencies
└── README.txt                        # Project documentation

How to Run:
1. Install required dependencies:
   pip install -r requirements.txt

2. Train the model:
   python main.py

3. Predict an image:
   python predict.py --img_path path_to_image.jpg

Notes:
- Ensure all images are resized to 64x64 pixels before training or prediction.
- Image pixel values should be normalized (e.g., scaled between 0 and 1).
- This ANN model is simple and may not perform well on complex datasets. For higher accuracy, a CNN model is recommended.

Author:
Nishitha GD
