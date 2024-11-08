# Vision Based Attendance System
 This project is a face recognition-based attendance system that captures and stores face data using OpenCV and employs a K-Nearest Neighbors (KNN) classifier for face identification. This system allows users to   add their faces, save them locally, and mark attendance based on recognized faces.


## Features
* Face Capture: Captures face data using a webcam.
* Face Recognition: Recognizes registered faces using a KNN classifier.
* Attendance Logging: Marks attendance in a CSV file with a timestamp.
* Audio Feedback: Provides an audio response using text-to-speech when attendance is marked.

## Concepts and Technologies Used
* OpenCV: Used for face detection and image processing.
* CascadeClassifier: Detects faces using a pre-trained Haar Cascade classifier.
* K-Nearest Neighbors (KNN): Used for face recognition by classifying faces based on previously saved face data.
* Pickle: Saves and loads face data and labels to/from files.
* CSV: Stores attendance records in a CSV file.
* Text-to-Speech: Provides audio feedback using win32com.client.

## Prerequisites
### must have this installed
* Open CV, Numpy, Sckit-learn, pickle, pywin32
* Download the Haar Cascade and place haarcascade_frontalface_default.xml file into the Data folder You can download it from [Github Repo](https://github.com/opencv/opencv/tree/master/data/haarcascades/)

## How To Run
* Run add_faces.py to capture face data and save locally and enter your name when prompted. The system will capture 5 images of your face and store them in the faces_data.pkl and the name in names.pkl file in the Data folder
* Run test.py to start the atttendance system
* when system recognizes a face, it marks attendance with name and timestamp in csv file name Attendance_<date>.csv
* press o key to confirm attendance, which provides and audio response
* press q to quit the program

## Algorithm: K-Nearest Neighbors (KNN)
The K-Nearest Neighbour algorithm is a simple, supervised machine learning algorithm that classifies new data points based on the majority label of nearest data points in the feature space 
* Trainging: During Training, the system stores labeled face data. Each Face is a 1-D array of pixel values, and the correspoding label is a person's name
* Prediction: When a new face is detected, the KNN Algorithm calculates the distance between this face and stored faces. Based on the 5 nearest neighbours, the algorithm assigns the most common name among these neighbours as the predicted name.

## Why KNN??
* KNN is chosen for this projesct due to it's simplicity and effectiveness for face recognition with a small dataset. it works well with for classification task where the data is relatively low dimensional, as it compares the input data to stored samples
  
## ScreenShots


* Running add_faces.py and then it will prompt "enter you name" to enter new person in database
* ![Running add_faces.py](https://github.com/user-attachments/assets/f51545d4-e785-4e5f-8dc0-bb8fd9b16683)
* Enterd The name
* ![capture](https://github.com/user-attachments/assets/7823ff10-adea-4d14-a4d5-45a54194011b)
* Camera Captures 5 images of person
* ![attendance](https://github.com/user-attachments/assets/010ff963-9200-462d-8895-edb40cf26e3f)
* Running Test.py to now record attendance press 'O' to record attendance you will hear Attendance Taken voice
* It also recognizes the person present in database

* ![sheet](https://github.com/user-attachments/assets/5d9cb378-8a32-44f8-8c50-f34078b5d498)
* Attendance stored in Csv file
