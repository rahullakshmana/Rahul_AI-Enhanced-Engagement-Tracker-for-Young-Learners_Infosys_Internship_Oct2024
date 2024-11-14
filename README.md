# Rahul's AI-Enhanced Engagement Tracker for Young Learners  
**Infosys Internship | October 2024**

An innovative AI-powered toolkit designed to track and enhance engagement among young learners, leveraging advanced image and video processing techniques to make learning interactive and responsive.

---

## Table of Contents
- [Image Processing](#image-processing)
- [Video Processing](#video-processing)
- [Annotations](#annotations)
- [Face Recognition](#face-recognition)

---

## Image Processing

**Libraries/Frameworks Used**  
- **OpenCV**: Version 4.10.0.84 - for comprehensive image processing operations  
- **NumPy**: Provides efficient handling of large arrays for image manipulations  

**Developed Logics**  


**C) Image_Colour**: Allows dynamic adjustments of color attributes, enhancing image aesthetics or focusing on key areas.



**D) Image_Concatenation**: Merges multiple images seamlessly, useful for side-by-side comparisons or feature demonstrations.

- **Input:**

   ![image1](https://github.com/user-attachments/assets/cbe4f229-50ab-4eca-bb20-71411d0411a7)
![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_stack(vertical)output](https://github.com/user-attachments/assets/ce6192eb-5cdf-42c4-a792-cb5dd3ead590)
![img_stack(horizontal)output](https://github.com/user-attachments/assets/db9c7710-debd-40a5-9445-2ebba9c7c81b)


**E) Image_Contour**: Detects and highlights contours, aiding in object identification and boundary marking.

- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_contouroutput](https://github.com/user-attachments/assets/d5ebe2e5-d269-4365-be9a-25ffaf292ecc)



**F) Image_Crop**: Extracts specific regions of interest, ideal for focusing on particular details.

- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_crop](https://github.com/user-attachments/assets/79423a18-4dea-46d8-bf62-9b96cbe9e3f1)




**E) Image_Detection and Erosion**: Identifies targeted areas and applies erosion to refine detected edges.


**F) Image_Edge Detection**: Uses filters to detect edges, enhancing details and outlines.


**G) Image_Equalized**: Equalizes histograms to improve contrast and clarity in low-quality images.


**H) Image_HSV**: Converts RGB colors to HSV, useful for color-based filtering and analysis.


**I) Image_Morph**: Applies morphological transformations, helping in noise reduction and structure enhancement.


**J) Image_Resize**: Resizes images, ensuring they meet specified dimensions for uniformity.


**K) Image_RGB to Gray**: Converts colorful images to grayscale, focusing on shape and structure.


**A) Image_Noise Removal & Closing Gaps**:
   Cleans up images by removing noise and closing gaps to improve clarity.
   - **Input:**

     
     ![image2](https://github.com/user-attachments/assets/88280f51-1201-4248-b453-cf749dc2458c)

   - **Output:**
    
        
        ![morphological_transformation(opening)output](https://github.com/user-attachments/assets/2387b17c-5d70-4f03-9ece-42a7efa21760)
![morphological_transformation(closing)output](https://github.com/user-attachments/assets/5757aa47-da0b-42d9-8f4b-3ef64eda7268)

   


**B) Image_Template**: Searches for specific patterns or objects within an image using template matching.


- **Input:**

  
![image2](https://github.com/user-attachments/assets/88280f51-1201-4248-b453-cf749dc2458c)
![template](https://github.com/user-attachments/assets/347e77fc-9047-41bc-9e3b-f03770ef1761)


- **Output:**

  
![templateoutput](https://github.com/user-attachments/assets/1e8386c2-3648-4c80-b8ad-ec44b36e7c70)

  

**L) Image_Single Image**: Processes single image inputs, allowing targeted analysis.


**M) Image_Blur**: Adds blur effects, reducing noise and highlighting important regions.



---

## Video Processing

**Libraries/Frameworks Used**  
- **OpenCV**: Version 4.10.0.84 - supports real-time video capture and processing, essential for dynamic content  

**Developed Logics**  
**1) Video_MultiVideo**: Reads images from a folder and displays their dimensions, helpful for batch processing.
**2) Video_FPS**: Captures and displays real-time video, calculating Frames Per Second (FPS) to assess video performance.
**3) Video_Save**: Captures live video from a webcam and saves it to a file for future analysis.
**4) Video_Stack**: Horizontally stacks two video files, ideal for comparison or creating multi-angle views.
**5) Video_Stream**: Streams live video feed, enabling real-time viewing and interaction.

---

## Annotations

**Libraries/Frameworks Used**  
- **OpenCV**: Version 4.10.0.84  
- **LabelImg**: Version 1.8.6 - a tool for labeling objects within images, essential for supervised learning  

**Developed Logics**  
**A) Data_Segregate**: Organizes images and corresponding labels, aiding in data management and accessibility.
**B) Label**: Draws bounding boxes around objects based on annotations, helping with object detection tasks.
**C) Label_Manipulate**: Updates class numbers in label files, allowing flexibility in object class identification for training.

---

## Face Recognition

**Libraries/Frameworks Used**  
- **OpenCV**: Version 4.10.0.84  
- **LabelImg**: Version 1.8.6  
- **dlib**: Version 19.24.6 - for precise facial landmark detection, enhancing recognition accuracy  
- **face_recognition**: Version 1.3.0 - widely used for facial detection and recognition  
- **imutils**: Version 0.5.4 - provides additional utilities for efficient image manipulation  

**Developed Logics**  
**A) Face_Recognition**: Recognizes and identifies faces in real-time, facilitating attendance tracking and security applications.
**B) Attendance_Save**: Automatically logs attendance based on recognized faces, streamlining record-keeping.
**C) Test**: A dedicated testing module for face recognition, ensuring functionality and reliability.
**D) Tools**: A collection of auxiliary processing functions supporting face recognition tasks.
**E) Excel_SC**: Exports recognition data to Excel, enabling easy record management.
**F) Excel_SC_DT**: Exports data with date-time stamps, ensuring timestamped records for accurate tracking.
**G) Landmark**: Detects facial landmarks, refining the recognition process by mapping facial features.
**H) Atten_Score**: Calculates attendance scores, enabling performance evaluation based on engagement.
**I) Avg_Atten_Score**: Averages scores across sessions, providing insights into long-term engagement trends.

---

**Note**: Ensure all required libraries and frameworks are installed with the specified versions for seamless operation. 

---

Unlock new possibilities with this AI-powered toolkit, making learning more interactive, measurable, and impactful for young learners!
