from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime


#import text- speech function
from win32com.client import Dispatch

#function to speak
def speak(str1):
    speak_engine = Dispatch('SAPI.SpVOice')
    speak_engine.rate = -2
    speak_engine.Speak(str1)


#speak('Attendance Taken')




#open the default camera to capture image
video = cv2.VideoCapture(0)


facedetect = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')


#Load pretrained face recognition data from pickle file
with open('Data/names.pkl','rb') as w:
    LABELS = pickle.load(w)

with open('Data/faces_data.pkl','rb') as f:
    FACES = pickle.load(f)    
    
    
    
#print shape of matrix
print('Shape of face matrix ',FACES.shape)    



knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(FACES,LABELS)

COL_NAMES = ['NAME','TIME']


while True:
    ret, frame = video.read()
    
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    faces = facedetect.detectMultiScale(grey,1.3,5)
    
    for(x,y,w,h) in faces:
        
        crop_img = frame[y:y+h,x:x+w,:]
        
        resized_img = cv2.resize(crop_img,(50,50)).flatten().reshape(1,-1)
        
        #predict the identity of face using the trained KNN clasifier
        output = knn.predict(resized_img)


        #get curretn timestamp
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        
        
        exist = os.path.isfile("Attendance_" + date + ".csv")
        
        
        
        #draw rectange and text on frame for visualization
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        
        #create am attendance record with predicted identity and timestamp
        attendance = [str(output[0]),str(timestamp)]
        
    cv2.imshow("FRame",frame)
    
    
    #wait for a key ti press
    k = cv2.waitKey(1)
    
    if k == ord('o'):
        speak('Attendance Taken..')
        time.sleep(5)
        
        if exist:
            #if file exists, append attendace
            with open("Attendance_" + date + ".csv","+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
                csvfile.close()
                
        else:
            #If file does'nt exist, create it and write column names and attendance
            with open("Attendance_"+date + ".csv",'+a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
            csvfile.close()
            
    if k == ord('q'):
         break
        
        
video.release() 
cv2.destroyAllWindows()                        