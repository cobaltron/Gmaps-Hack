from selenium import webdriver
import sys
import os
import time
import cv2
import numpy as np

args=sys.argv[1:]
lat=args[0]
long=args[1]

driver = webdriver.Chrome(executable_path='C:/Users/Rajarshi Lahiri/Desktop/Gmap Hack/chromedriver.exe')
url="https://www.google.com/maps/@"+lat+","+long+',13z/data=!5m1!1e1'
#print(url)
driver.get(url)
driver.fullscreen_window()
time.sleep(1)
driver.save_screenshot('Map'+'.png')
driver.quit()

img=cv2.imread("Map.png")
h = img.shape[0]
w = img.shape[1]
t1=t2=t3=t4=0
# loop over the image, pixel by pixel
for i in range(h):
  for j in range(w):
    k = img[i,j]
    if(np.array_equal(k,np.array([104,214,99]))):
        t1=t1+1
    if(np.array_equal(k,np.array([77,151,255]))):
        t2=t2+1
    if(np.array_equal(k,np.array([50,60,242]))):
        t3=t3+1
    if(np.array_equal(k,np.array([31,31,129]))):
        t4=t4+1

response=['Less Traffic','Medium Traffic','Heavy Traffic',"Extremely Heavy Traffic"]
traffic=np.array([t1,t2,t3,t4])
print(response[np.argmax(traffic)])

