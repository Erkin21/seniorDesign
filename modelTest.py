# !pip install tflite-runtime
import numpy as np
import tflite_runtime.interpreter as tflite

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path='//content//kerasModelUpdated1.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Replace this by getting data from the excel sheet this value here is to just test to work it
input_data = np.array([[157.44, 65.67, 22.03, 59.69, 93.03, 0.78, 29.32, 29.96, 1.34, 0.95, 1.4, 62.11, 1, 0.56, 0.42]], dtype=np.float32)
print(input_data)

# Test the model with the input data
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run inference
interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
output_data = interpreter.get_tensor(output_details[0]['index'])
probability_alz = (output_data[0] * 100).item()  
print("Probability if they have Alzheimer's: {:.2f} %".format(probability_alz))
