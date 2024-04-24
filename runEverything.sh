#!/bin/bash

# Navigate to first project
cd Desktop/project

# Activate First script
python main.py

# Activate Second script in Pico
thonny --run mpuClass.py

# Delay it so that you can unplug it or unplug it OR run main in Pico
sleep 10
#thonny --run main.py

# Activate Third script
python mpuToExcel.py

sleep 5

# Navigate to machine learning folder.
cd Desktop/machineLearning

# activate the virtual environment
source tfline1-env/bin/activate

python modelTest.py
