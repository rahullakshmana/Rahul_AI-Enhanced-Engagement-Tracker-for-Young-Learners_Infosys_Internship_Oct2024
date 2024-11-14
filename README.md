# Rahul_AI-Enhanced-Engagement-Tracker-for-Young-Learners  
**Infosys Internship | October 2024**

A comprehensive AI-based toolkit for tracking and enhancing engagement among young learners using image and video processing techniques.

---

## Table of Contents
1. [Image Processing](#image-processing)
2. [Video Processing](#video-processing)
3. [Annotations](#annotations)
4. [Face Recognition](#face-recognition)

---

## 1. Image Processing

**Libraries/Frameworks Used**:
- **OpenCV**: Version 4.10.0.84 - for image processing tasks
- **NumPy**: For efficient array handling

**Developed Logics**:
- **Image_Noise Removal & Closing Gaps**: Removes noise and fills gaps in images.
- **Image_Template**: Performs template matching on images.
- **Image_Colour**: Adjusts color attributes in images.
- **Image_Concatenation**: Merges multiple images into one.
- **Image_Contour**: Detects and highlights image contours.
- **Image_Crop**: Extracts regions of interest from images.
- **Image_Detection and Erosion**: Identifies and erodes detected areas.
- **Image_Edge Detection**: Applies edge detection filters.
- **Image_Equalized**: Equalizes histograms to improve contrast.
- **Image_HSV**: Converts image colors to HSV format.
- **Image_Morph**: Executes morphological transformations.
- **Image_Resize**: Resizes images to specific dimensions.
- **Image_RGB to Gray**: Converts RGB images to grayscale.
- **Image_Single Image**: Processes single image inputs.
- **Image_Blur**: Applies blur filters to reduce noise.

---

## 2. Video Processing

**Libraries/Frameworks Used**:
- **OpenCV**: Version 4.10.0.84 - for video handling and real-time capture

**Developed Logics**:
- **Video_MultiVideo**: Reads and displays images from a folder, showing dimensions.
- **Video_FPS**: Captures and displays real-time video with FPS calculation.
- **Video_Save**: Captures and saves live video to a file.
- **Video_Stack**: Stacks two video files horizontally after resizing.
- **Video_Stream**: Streams live video from the webcam.

---

## 3. Annotations

**Libraries/Frameworks Used**:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6 - for labeling objects in images

**Developed Logics**:
- **Data_Segregate**: Organizes images and labels into directories.
- **Label**: Draws bounding boxes on images based on annotations.
- **Label_Manipulate**: Updates class numbers in label files for object detection.

---

## 4. Face Recognition

**Libraries/Frameworks Used**:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6 - for facial landmark recognition
- **face_recognition**: Version 1.3.0 - for facial detection and recognition
- **imutils**: Version 0.5.4 - for image manipulation utilities

**Developed Logics**:
- **Face_Recognition**: Detects and recognizes faces.
- **Attendance_Save**: Saves attendance records of recognized faces.
- **Test**: Module for testing face recognition functionality.
- **Tools**: Utility functions for processing.
- **Excel_SC**: Exports data to Excel sheets.
- **Excel_SC_DT**: Exports data with date-time information.
- **Landmark**: Detects facial landmarks for enhanced recognition.
- **Atten_Score**: Calculates attendance scores.
- **Avg_Atten_Score**: Averages attendance scores across sessions.
