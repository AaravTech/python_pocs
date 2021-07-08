# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())


 
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
 
    # show the images
    cv2.imshow("image", image)
    cv2.imshow("output", output)
    cv2.waitKey(0)

lower = np.array(boundaries[0][0], dtype = "uint8")
upper = np.array(boundaries[0][1], dtype = "uint8")
cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("image", frame)
    cv2.imshow("output", output)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()