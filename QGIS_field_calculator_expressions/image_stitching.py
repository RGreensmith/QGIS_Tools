import cv2
# image_paths=['south.jpg','central.jpg']
# image_paths=['southErasedCropped.jpg','centralErasedCropped.jpg']
image_paths=['koala1.jpg','koala4.jpg','koala3.jpg']

# initialized a list of images
imgs = []
 
for path in image_paths:
    imgs.append(cv2.imread(f'./test_images/{path}'))

# showing the original pictures
# cv2.imshow('1',imgs[0])
# cv2.imshow('2',imgs[1])
# cv2.imshow('3',imgs[2])
# cv2.waitKey(0)

stitcher=cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
stitcher.setPanoConfidenceThresh(0.2)
# stitcher.setFeaturesFinder(cv2.SIFT_create())

(dummy,output)=stitcher.stitch(imgs)
 
if dummy != cv2.STITCHER_OK:
  # checking if the stitching procedure is successful
  # .stitch() function returns a true value if stitching is
  # done successfully
    print(f"stitching isn't successful: {dummy}")
else:
    print('Your Panorama is ready!!!')
 
    # final output
    # cv2.imshow('final_result',output)
    # cv2.waitKey(0)
    cv2.imwrite('./test_images/final_result.jpg',output)
