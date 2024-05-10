from keras.models import  load_model
model = load_model("model.keras")
import cv2 as cv
path = 'TumorImages/y18.jpg'

image = cv.imread(path)
image = cv.resize(image,(256,256))
cv.imshow("Image" , image)
cv.waitKey(0)
image = image[None,:,:,:]

out = model.predict(image)

if out[0][0]> 0.5:
    print("Classified as Yes ")
else:
    print("Classified as No ")
