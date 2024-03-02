import numpy as np
import tensorflow as tf

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="/home/seniorDesign/Desktop/machineLearning/tfModel/model.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prepare input data (adjust according to your model's input requirements)
input_data = np.array([6, 165.31, 68.01, 56, 87.07, 20.13, 30.02, 32.69, 1.29, 0.91, 1.41, 59.5, 0.95, 0.51, 0.43, 2.49, 3.98, 2.31, 55.03, 43.08, 2.46, 7.59], dtype=np.float32)
input_data = input_data.reshape(input_details[0]['shape'])

# Set input tensor
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run inference
interpreter.invoke()

# Get output tensor
output_data = interpreter.get_tensor(output_details[0]['index'])

print("Inference result:", output_data)