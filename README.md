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


**A) Image_Concatenation**: Merges multiple images seamlessly, useful for side-by-side comparisons or feature demonstrations.

- **Input:**

   ![image1](https://github.com/user-attachments/assets/cbe4f229-50ab-4eca-bb20-71411d0411a7)
![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_stack(vertical)output](https://github.com/user-attachments/assets/ce6192eb-5cdf-42c4-a792-cb5dd3ead590)
![img_stack(horizontal)output](https://github.com/user-attachments/assets/db9c7710-debd-40a5-9445-2ebba9c7c81b)


**B) Image_Contour**: Detects and highlights contours, aiding in object identification and boundary marking.

- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_contouroutput](https://github.com/user-attachments/assets/d5ebe2e5-d269-4365-be9a-25ffaf292ecc)



**C) Image_Crop**: Extracts specific regions of interest, ideal for focusing on particular details.

- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_crop](https://github.com/user-attachments/assets/79423a18-4dea-46d8-bf62-9b96cbe9e3f1)




**D) Image_Detection and Erosion**: Identifies targeted areas and applies erosion to refine detected edges.

- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

 ![dilo_ero(eroded)output](https://github.com/user-attachments/assets/3547979e-849e-434b-8ab5-375f6f3fe693)
![dilo_ero(dilated)output](https://github.com/user-attachments/assets/574d0959-cdf4-409e-9ed3-7ed987426b38)




**E) Image_Edge Detection**: Uses filters to detect edges, enhancing details and outlines.

- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

![img_edgeoutput](https://github.com/user-attachments/assets/591b31ed-12da-41d3-8735-e71183dc581c)



**F) Image_Equalized**: Equalizes histograms to improve contrast and clarity in low-quality images.


- **Input:**

![image1](https://github.com/user-attachments/assets/c7955530-f5f0-4387-8867-745da904dc96)



- **Output:**

 ![histogram_equlizationoutput](https://github.com/user-attachments/assets/2bc95cca-0983-4e73-b174-4f886e1d4f34)





**G) Image_HSV**: Converts RGB colors to HSV, useful for color-based filtering and analysis.


- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_hsvoutput](https://github.com/user-attachments/assets/223c9397-c028-4823-a674-caf84b8a8367)





**H) Image_Morph**: Applies morphological transformations, helping in noise reduction and structure enhancement.

- **Input:**

     
     ![image2](https://github.com/user-attachments/assets/88280f51-1201-4248-b453-cf749dc2458c)

   - **Output:**
    
        
        ![morphological_transformation(opening)output](https://github.com/user-attachments/assets/2387b17c-5d70-4f03-9ece-42a7efa21760)
![morphological_transformation(closing)output](https://github.com/user-attachments/assets/5757aa47-da0b-42d9-8f4b-3ef64eda7268)

**I) Image_Resize**: Resizes images, ensuring they meet specified dimensions for uniformity.


- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_resizeoutput](https://github.com/user-attachments/assets/9a866714-ebaa-4c6c-bf4e-345a57513825)




**J) Image_RGB to Gray**: Converts colorful images to grayscale, focusing on shape and structure.


- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![bgr2grayoutput](https://github.com/user-attachments/assets/d2b3714e-9bbd-4d3c-b415-ea7a8565af44)


   
**K) image_rotate**:
This rotates an image by 90 degrees around its center.

- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_rotateoutput](https://github.com/user-attachments/assets/e55b0fad-6440-4814-8a78-2124afa5dbf1)



**L) Image_Template**: Searches for specific patterns or objects within an image using template matching.


- **Input:**

  
![image2](https://github.com/user-attachments/assets/88280f51-1201-4248-b453-cf749dc2458c)
![template](https://github.com/user-attachments/assets/347e77fc-9047-41bc-9e3b-f03770ef1761)


- **Output:**

  
![templateoutput](https://github.com/user-attachments/assets/1e8386c2-3648-4c80-b8ad-ec44b36e7c70)


**M) Image_Blur**: Adds blur effects, reducing noise and highlighting important regions.


- **Input:**

![image2](https://github.com/user-attachments/assets/fb33de56-5500-4138-be8b-ca0ccc18bf4b)


- **Output:**

  ![img_bluroutput](https://github.com/user-attachments/assets/ace8528d-723a-4289-86bf-51d9c996b74e)


**N) Image_Noise Removal & Closing Gaps**:
   Cleans up images by removing noise and closing gaps to improve clarity.


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

- **Input:**

![input-annotations](https://github.com/user-attachments/assets/2bc763d5-1c9b-4925-934a-992e0e6e3c49)



- **Output:**

  ![output-annotations](https://github.com/user-attachments/assets/709af433-b1c5-43f3-aa83-c844a92808f8)


**B) Label**: Draws bounding boxes around objects based on annotations, helping with object detection tasks.


- **Output:**

  ![output(gun)-annotations](https://github.com/user-attachments/assets/d44ad5d5-b881-4b6e-9682-4e92ece91bae)




**C) Label_Manipulate**: Updates class numbers in label files, allowing flexibility in object class identification for training.

- **Output:**

  ![output(gun C)-annotations](https://github.com/user-attachments/assets/caeb1fa5-f23e-49b5-819f-862a73b2167d)




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

- **Input:**

![rahul_crop](https://github.com/user-attachments/assets/bde431b6-fb9e-4a5f-8641-a7c8d8e827db)



- **Output:**

  ![face_recog_output](https://github.com/user-attachments/assets/b421e775-9ba2-4fe4-8199-784db36514dd)



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
