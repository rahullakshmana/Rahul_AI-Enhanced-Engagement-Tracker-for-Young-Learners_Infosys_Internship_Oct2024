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

### Developed Logics


### Face Recognition Script

This script uses real-time video from a webcam to identify a specific person’s face by comparing it to a reference image.

### Overview

- **Setup**: Loads a target face from a reference image and opens the webcam.
- **Face Detection**: Continuously captures video frames, detects faces, and checks if any match the target face.
- **Labeling**: Shows "Recognized" if there’s a match; otherwise, displays "Not Recognized."
- **Exit**: Press 'q' to end the video stream and close the program.

Run the script to begin real-time face recognition with a confidence threshold for accuracy.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

  ![face_recog_output](https://github.com/user-attachments/assets/b421e775-9ba2-4fe4-8199-784db36514dd)



### Attendance_Save Script

This script captures real-time video to recognize a specific person’s face, logs their attendance, and saves it to an Excel file for streamlined record-keeping.

#### Overview

- **Setup**: Loads the target face data and initializes the webcam.
- **Face Recognition and Logging**: Detects faces in the video stream, compares them to the target face, and logs recognized faces with timestamps in a DataFrame.
- **Attendance Recording**: Every 5 recognitions, the attendance data is saved to an Excel file, and the counter resets.
- **Exit**: Press 'q' to end the video stream. Any remaining recognitions are saved to Excel before exit.

This setup provides an automated attendance system that recognizes faces in real-time and logs attendance details efficiently.

- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

  ![face_recog_output](https://github.com/user-attachments/assets/b421e775-9ba2-4fe4-8199-784db36514dd)
![attendance_save_excel](https://github.com/user-attachments/assets/787c8f1d-d6fb-4172-88ab-6130ea9a2617)



### Test Module

This module provides a dedicated testing environment for face recognition, ensuring accurate functionality and reliability. It identifies faces in real-time, tracks entries with time intervals, and saves logs periodically.

#### Overview

- **Setup**: Loads target face data, initializes the webcam, and sets recognition and time thresholds.
- **Face Detection and Logging**: Detects faces in the video feed, checks if the recognized person matches the target, and records recognized faces with timestamps.
- **Timed Logging**: Logs each recognition at specific intervals, avoiding duplicates within a short timeframe, and resets the timer for new entries after a set gap.
- **Periodic Save**: Automatically saves the recognition log to an Excel file every 30 seconds.
- **Exit**: Press 'q' to end the video stream and save any remaining log data to Excel.

This testing module provides an organized framework for real-time face recognition, enabling robust verification of recognition accuracy with time-based logging.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

  ![face_recog_output](https://github.com/user-attachments/assets/b421e775-9ba2-4fe4-8199-784db36514dd)



### Tools Module

The Tools module offers a suite of auxiliary functions to enhance and support face recognition tasks, focusing on optimizing processing speed, accuracy, and data logging.

#### Overview

- **Setup**: Loads target face data, initializes the webcam, and sets confidence and frame skip parameters for efficient processing.
- **Face Detection and Logging**: Detects faces in real-time, checks if the recognized person matches the known face, and logs their information with date and time.
- **Optimized Processing**: Processes every second frame to reduce computational load while maintaining recognition accuracy.
- **Batch Logging**: Once a target recognition count (e.g., 5) is met, attendance records are saved to an Excel file.
- **Exit and Final Save**: Press 'q' to exit, triggering a final save of any remaining data to an Excel file.

The Tools module provides essential utility functions that streamline the process of face recognition and logging, enhancing overall reliability and efficiency.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

  ![face_recog_output](https://github.com/user-attachments/assets/b421e775-9ba2-4fe4-8199-784db36514dd)
![tools_excel](https://github.com/user-attachments/assets/5d20c690-d3e6-4168-a835-45c7626f9485)



### Excel_SC Module

The Excel_SC module is designed to export recognized face data, along with timestamped screenshots, to an Excel file. This enables easy record management and retrieval, especially useful for attendance or security applications.

#### Overview

- **Directory Setup**: Creates a dedicated directory to save screenshots of recognized faces.
- **Face Recognition and Screenshot Capture**: Detects faces in real-time, verifies them against a known image, and saves screenshots when a match is identified.
- **Timed Logging**: Logs the recognized face with a screenshot every 2 minutes, with a 5-minute gap required before re-logging the same individual.
- **Data Export**: All recognition data, including timestamps and screenshot paths, is saved to an Excel file upon completion.
- **Exit and Final Save**: Press 'q' to exit, triggering a final save of the data, ensuring no logged information is missed.

The Excel_SC module offers a streamlined approach to recording, managing, and exporting recognition data, supporting face recognition tasks with organized record-keeping.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

  ![face_recog_output](https://github.com/user-attachments/assets/b421e775-9ba2-4fe4-8199-784db36514dd)



### Excel_SC_DT Module

The Excel_SC_DT module is an enhanced tool for exporting face recognition data with precise date-time stamps. It ensures accurate, timestamped records, aiding in reliable tracking for attendance, security, or monitoring applications.

#### Overview

- **Screenshot Directory**: Creates a dedicated folder for storing recognized face screenshots with date-time stamps for easy management.
- **Real-time Face Recognition with Timestamp Overlay**: Detects faces in real time, overlays the current date and time on the screenshot, and saves the image.
- **Timed Logging Intervals**: Logs recognized faces every 2 minutes with a mandatory 5-minute gap before re-logging the same person, providing a well-structured timeline of appearances.
- **Periodic Excel Export**: Exports recognition data, including date, time, and screenshot path, to an Excel file every 30 seconds, keeping data consistently updated.
- **Exit and Final Save**: Press 'q' to exit, which triggers a final save to ensure all data is securely stored in Excel.

The Excel_SC_DT module is ideal for applications requiring high accuracy in tracking, such as attendance systems or security monitoring, with easy access to data through organized Excel records and timestamped images.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

  ![excel_sc_dt_video_output](https://github.com/user-attachments/assets/11b9b401-209e-4eba-950c-03aa2b175395)

![excel_sc_dt_excel](https://github.com/user-attachments/assets/a05d4f8c-7289-448a-aa07-a0f30db938ed)


### Landmark Module

The Landmark module is designed to refine facial recognition accuracy by mapping and analyzing facial landmarks. This feature is particularly useful for monitoring attentiveness based on head pose and detecting distinct facial features.

#### Overview

- **Facial Landmark Detection**: Utilizes dlib’s landmark predictor to detect 68 facial landmarks (such as eyes, nose, mouth, and chin) on detected faces. Green dots mark these landmarks on the frame for visualization.
- **Head Pose Estimation**: Computes head pose based on specific facial landmarks (nose tip, chin, eye corners, and mouth corners) to estimate the yaw, pitch, and roll of the face. This is crucial in determining if the person is looking straight (attentive) or away (not attentive).
- **Attention Status Display**: Defines an "attentive" status based on head pose. If the yaw and pitch angles are within specific thresholds, the person is marked as attentive. An "Attentive" or "Not Attentive" label is displayed on the frame.
- **Periodic Screenshot Logging**: Captures screenshots when the face is recognized, logging information including name, date, time, screenshot path, and attentiveness status.
- **Timed Excel Exports**: Saves recognition data to an Excel file every 30 seconds, including date, time, and attentiveness, for consistent tracking and record-keeping.
- **Exit and Final Save**: Press 'q' to exit, triggering a final save of all recognition and attentiveness data in Excel.

This module is ideal for applications requiring attentiveness monitoring, such as online classes, security, or any setting where tracking head orientation and attention are important.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**


![Rahul_2024-11-08_21-44-43](https://github.com/user-attachments/assets/051e9382-90f6-4fa3-a7ff-d03d18bfcc24)
![landmark_excel](https://github.com/user-attachments/assets/f143c849-2af7-4534-81b4-3b831baabe28)


### Atten_Score Module

The Atten_Score module is designed to calculate an attentiveness score based on the engagement of a person in front of the camera. This score is derived from the head pose estimation (yaw and pitch) and enables performance evaluation based on the individual's engagement level.

#### Overview

- **Attentiveness Score Calculation**: 
  The attentiveness score is computed by analyzing the yaw and pitch of the head pose. The score is normalized between 0 and 1. A higher score indicates a more attentive person. The formula used is based on the yaw and pitch thresholds, where the score decreases as the head moves away from the frontal position.
  
- **Score Threshold**:
  If the calculated attentiveness score is above a predefined threshold (0.5), the individual is considered "Attentive." Otherwise, the person is marked as "Not Attentive."

- **Facial Landmark Detection**:
  The module detects 68 facial landmarks using dlib's landmark predictor, marking them on the frame. This helps in analyzing head pose, which is crucial for calculating the attentiveness score.

- **Real-Time Monitoring**:
  The system runs on a live video feed, detecting faces and calculating the attentiveness score. It logs this data along with screenshots of the individual and saves it to an Excel file.

- **Screenshot Logging**:
  Screenshots are saved whenever a face is recognized and the attentiveness score is computed. These images are saved in a specified directory.

- **Periodic Data Saving**:
  The recognition events (name, date, time, attentiveness, and attention score) are saved to an Excel file every 30 seconds. The file also contains details about the screenshot taken during each event.

- **Exit and Final Save**:
  Press the 'q' key to stop the program. When exiting, the system will save any remaining recognition data to an Excel file.


## Key Functions

1. **`get_head_pose(landmarks)`**: 
   - Calculates the head pose by finding the rotation and translation vectors from the facial landmarks.

2. **`calculate_attention_score(yaw, pitch)`**: 
   - Calculates the attentiveness score based on yaw and pitch head angles. The score ranges from 0 to 1, with higher values indicating greater attentiveness.


This module is ideal for applications where attentiveness tracking is necessary, such as in online classes, meetings, or security systems requiring performance evaluation based on engagement levels.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

![Rahul_2024-11-08_21-26-07](https://github.com/user-attachments/assets/d0e02776-1bbb-4427-bbd6-b50f477727ee)
![atten_score_excel](https://github.com/user-attachments/assets/98716a35-6a04-4ab0-b832-36abedb4c4f7)



# Avg_Atten_Score Program

The Avg_Atten_Score program uses face recognition and head pose estimation to calculate an individual's average attentiveness in real-time based on a live video feed. It tracks whether the person is attentive or not by analyzing their head's yaw and pitch, logging the data, and saving screenshots.

## Key Features

- **Face Recognition**: Recognizes a known individual using `face_recognition`.
- **Attentiveness Score**: Calculates a score based on head pose (yaw and pitch) and displays it in real-time.
- **Screenshot Logging**: Saves screenshots of the recognized individual when attentiveness is calculated.
- **Data Saving**: Logs recognition events and saves them to an Excel file every 30 seconds.
- **Exit and Average Score**: Press 'q' to exit, and the program will calculate and save the average attentiveness score.


## Usage

1. Place the reference image in the working directory.
2. Run the program to start the video stream and tracking.
3. The data is saved in an Excel file.

This program is ideal for monitoring attentiveness in online classes, meetings, or security systems.


- **Input:**


![rahul_crop1](https://github.com/user-attachments/assets/2e82eb2d-fba7-40f5-9b68-612a9c69f96b)


- **Output:**

![Rahul_2024-11-08_21-37-06](https://github.com/user-attachments/assets/3d4f4fcc-a003-47e2-add3-497cc7aa739c)
![avg_attendance_score_excel](https://github.com/user-attachments/assets/b6c9d3ee-ea25-46ae-82d6-316dbd10118d)


---

**Note**: Ensure all required libraries and frameworks are installed with the specified versions for seamless operation. 

---

Unlock new possibilities with this AI-power
ed toolkit, making learning more interactive, measurable, and impactful for young learners!
