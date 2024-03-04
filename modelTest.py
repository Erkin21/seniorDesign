import tflite_runtime.interpreter as tflite
import numpy as np

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path='path/to/model.tflite')
interpreter.allocate_tensors()

# Prepare input data (replace this with your input data)
input_data = np.array(...)  # shape should match the input shape of your model
input_tensor_index = interpreter.get_input_details()[0]['index']
interpreter.set_tensor(input_tensor_index, input_data)

# Run inference
interpreter.invoke()

# Get the output results
output_tensor_index = interpreter.get_output_details()[0]['index']
output_data = interpreter.get_tensor(output_tensor_index)

# Process the output data as needed
print("Inference Result:", output_data)
