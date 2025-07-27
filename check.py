from tensorflow.keras.models import load_model

# Load your model
model = load_model("VEGETABLE_IMAGE_CLASSIFIER.h5")

# Show the model summary
model.summary()
