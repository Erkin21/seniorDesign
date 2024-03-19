import numpy as np
import tflite_runtime.interpreter as tflite

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path='kerasModelUpdated.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prepare input data (replace this with your actual input data)
input_data = np.array([[165.31, 68.01, 25.05, 56, 87.07, 20.13, 30.02, 32.69, 1.29, 0.91, 1.41, 59.5, 0.95, 0.51, 0.43, 2.49, 3.98, 2.31, 55.03, 43.08, 2.46, 7.59]], dtype=np.float32)

# Set input tensor
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run inference
interpreter.invoke()

# Get the output results
output_data = interpreter.get_tensor(output_details[0]['index'])

# Print the output result
print("Probability if they have Alz:", output_data[0][0] * 100, "%")
