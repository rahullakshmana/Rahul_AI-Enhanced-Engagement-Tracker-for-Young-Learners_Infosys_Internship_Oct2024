import cv2

img = cv2.imread('image2.jpg')
template = cv2.imread('template.jpg', 0)

if img is None:
    print("Error: Could not read image2.jpg")
if template is None:
    print("Error: Could not read template.jpg")

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

cv2.imshow('Detected Template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
