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
- **Image_Noise Removal & Closing Gaps**: Cleans up images by removing noise and closing gaps to improve clarity.
- **Image_Template**: Searches for specific patterns or objects within an image using template matching.
- **Image_Colour**: Allows dynamic adjustments of color attributes, enhancing image aesthetics or focusing on key areas.
- **Image_Concatenation**: Merges multiple images seamlessly, useful for side-by-side comparisons or feature demonstrations.
- **Image_Contour**: Detects and highlights contours, aiding in object identification and boundary marking.
- **Image_Crop**: Extracts specific regions of interest, ideal for focusing on particular details.
- **Image_Detection and Erosion**: Identifies targeted areas and applies erosion to refine detected edges.
- **Image_Edge Detection**: Uses filters to detect edges, enhancing details and outlines.
- **Image_Equalized**: Equalizes histograms to improve contrast and clarity in low-quality images.
- **Image_HSV**: Converts RGB colors to HSV, useful for color-based filtering and analysis.
- **Image_Morph**: Applies morphological transformations, helping in noise reduction and structure enhancement.
- **Image_Resize**: Resizes images, ensuring they meet specified dimensions for uniformity.
- **Image_RGB to Gray**: Converts colorful images to grayscale, focusing on shape and structure.
- **Image_Single Image**: Processes single image inputs, allowing targeted analysis.
- **Image_Blur**: Adds blur effects, reducing noise and highlighting important regions.

---

## Video Processing

**Libraries/Frameworks Used**  
- **OpenCV**: Version 4.10.0.84 - supports real-time video capture and processing, essential for dynamic content  

**Developed Logics**  
- **Video_MultiVideo**: Reads images from a folder and displays their dimensions, helpful for batch processing.
- **Video_FPS**: Captures and displays real-time video, calculating Frames Per Second (FPS) to assess video performance.
- **Video_Save**: Captures live video from a webcam and saves it to a file for future analysis.
- **Video_Stack**: Horizontally stacks two video files, ideal for comparison or creating multi-angle views.
- **Video_Stream**: Streams live video feed, enabling real-time viewing and interaction.

---

## Annotations

**Libraries/Frameworks Used**  
- **OpenCV**: Version 4.10.0.84  
- **LabelImg**: Version 1.8.6 - a tool for labeling objects within images, essential for supervised learning  

**Developed Logics**  
- **Data_Segregate**: Organizes images and corresponding labels, aiding in data management and accessibility.
- **Label**: Draws bounding boxes around objects based on annotations, helping with object detection tasks.
- **Label_Manipulate**: Updates class numbers in label files, allowing flexibility in object class identification for training.

---

## Face Recognition

**Libraries/Frameworks Used**  
- **OpenCV**: Version 4.10.0.84  
- **LabelImg**: Version 1.8.6  
- **dlib**: Version 19.24.6 - for precise facial landmark detection, enhancing recognition accuracy  
- **face_recognition**: Version 1.3.0 - widely used for facial detection and recognition  
- **imutils**: Version 0.5.4 - provides additional utilities for efficient image manipulation  

**Developed Logics**  
- **Face_Recognition**: Recognizes and identifies faces in real-time, facilitating attendance tracking and security applications.
- **Attendance_Save**: Automatically logs attendance based on recognized faces, streamlining record-keeping.
- **Test**: A dedicated testing module for face recognition, ensuring functionality and reliability.
- **Tools**: A collection of auxiliary processing functions supporting face recognition tasks.
- **Excel_SC**: Exports recognition data to Excel, enabling easy record management.
- **Excel_SC_DT**: Exports data with date-time stamps, ensuring timestamped records for accurate tracking.
- **Landmark**: Detects facial landmarks, refining the recognition process by mapping facial features.
- **Atten_Score**: Calculates attendance scores, enabling performance evaluation based on engagement.
- **Avg_Atten_Score**: Averages scores across sessions, providing insights into long-term engagement trends.

---

**Note**: Ensure all required libraries and frameworks are installed with the specified versions for seamless operation. 

---

Unlock new possibilities with this AI-powered toolkit, making learning more interactive, measurable, and impactful for young learners!
