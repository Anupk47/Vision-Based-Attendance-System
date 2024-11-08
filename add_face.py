import cv2
import pickle 
import os
import numpy as np
from datetime import datetime



#open default cameras
video = cv2.VideoCapture(0)

#using pretrained HaarCascade Model 
facedetect = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')


face_data = []
i = 0

names = input('Enter your Name')

#capture frames until we say decide to stop
while True:
    ret, frame = video.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(grey,1.3,5)
    
    #iterate over detected faces
    for (x, y, w, h) in faces:
        #crops the face reigion from the frame
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))



        if len(face_data) <= 5 and i % 5 == 0:
            face_data.append(resized_img)
        
        i = i + 1
        
        #display count of captured faces on the frame
        cv2.putText(frame,str(len(face_data)), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(50,50,255),1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)    
    
    cv2.imshow("Frame",frame)
    
    k = cv2.waitKey(1)
    if k == ord('q') or len(face_data) == 5: #
        break
    
    
    
#release the video capture object and close all windows     
video.release()
cv2.destroyAllWindows()     



#converting the list of face images to a numpy array and reshape it
face_data = np.asarray(face_data)
face_data = face_data.reshape(5,-1)

#print(face_data) 



#now putting all the data inside the pickle file


# Check if 'names.pkl' is present in the 'Data/' directory
if 'names.pkl' not in os.listdir('Data/'):
    # If not present, create a list with the entered name repeated 5 times
    names = [names] * 5
    #save list to names.pkl
    with open('Data/names.pkl','wb') as f:
        pickle.dump(names,f)
    
else:
     # If 'names.pkl' is present, load the existing list
    with open('Data/names.pkl' ,'rb') as f:
        names = pickle.load(f)
    
    # Append the entered name 5 times to the existing list    
    names = names + [names] * 5
    #save and update the list to names.pkl
    with open('Data/names.pkl','wb') as f:
        pickle.dump(names,f)



#similarly check if faces_data.pkl is present in the Data/ 

#if not               
if 'faces_data.pkl' not in os.listdir('Data/'):
    #save numpy array face_data to face_data.pkl
    with open('Data/faces_data.pkl','wb') as f:
        pickle.dump(face_data,f)
    
else:
     # If 'faces_data.pkl' is present, load the existing array
    with open('Data/faces_data.pkl' ,'rb') as f:
        faces = pickle.load(f)
    
    # Append the new array 'faces_data' to the existing array  
    faces = np.append(faces,face_data, axis=0)
     # Save the updated array to 'faces_data.pkl'
    with open('Data/faces_data.pkl','wb') as f:
        pickle.dump(faces,f)

