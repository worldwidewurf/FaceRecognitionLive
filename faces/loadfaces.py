import sys
import os
import numpy as np
import cv2
import face_recognition as fr

def loadpictures():
    # Load all the pictures that are in the images folder and return them in a list
    # The list contains tuples of the form (name, image)
    # The name is the name of the file
    # the image is a fr face ancoding
    
    
    face_encodings = []
    images_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    raw_images = os.listdir(images_folder)
    for image in raw_images:
        try:
            imagepath = os.path.join(images_folder, image)
            saved_picture = fr.load_image_file(imagepath)
            saved_picture_face_array = fr.face_encodings(saved_picture)
            face_encodings.append((image.split(".")[0], saved_picture_face_array[0]))
        except:
            """this might not be needed in the future because i intend to take the pictures in the program making sure 
               that there is a face in the picture before saving it
            """
            print("Could not load image: " + image+
                  " might be because there is no face in the image or the image is too small")
    return face_encodings
    
