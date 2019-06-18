# Self-Driving-Car

The Self Driving Car is Made using the Udacity Self Driving Car Simulator which can be found at 
https://github.com/udacity/self-driving-car-sim

The project is based on Convolutional Neral Networks (CNN) and Behavioral Cloning. 
Training invloves driving the car manually, wherein images are captured by the 3 car cameras mounted at the front and corresponding steering angle is noted
The Training Images can be found in the IMG folder.
Steering Angles corresponding to the Training Images are stored in the driving_log.csv file.

These Training Images and Steering Angles are clubbed together, and a Convlutional Neural Network is trained to predict a Steering Angle given an input Image
The model used for Convolutional Neral Network is the NVIDIA model as suggested by NVIDIA.
Various Transformation and Data Augmentation Techniques are applied on the input images so as to make Training more efficient and achieve a Good Accuracy.

The performance of the Car after Training on the Trained Track can be found in the video below:-

https://drive.google.com/open?id=1_SaNTLfogPnO2WkxNdc8UOjpDUfzpsns

The performance of the Car after Training on the Unknown Test Track can be found in the video below:-

https://drive.google.com/open?id=11xYqZfAvQO2_DI-DI_ahaWpC0P1yA86t
