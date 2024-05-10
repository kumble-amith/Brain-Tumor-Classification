
def getPrediction(path):
    
    
    from keras.models import  load_model
    import cv2 as cv
    try:
        model = load_model("model.keras")
    except IOError :
        return "No model Exception"
    except ValueError :
        return "No model value Exception"
    
    path = "TumorImages/"+path

    image = cv.imread(path)

    if(image == None):
        return "Please Place image in the TumorImages Folder and then Select"
    return "Image Success"
    image = cv.resize(image,(256,256))
    image = image[None,:,:,:]
    return "Pass"
    out = model.predict(image)

    if out[0][0]> 0.5:
        return "Classified as Yes "
    else:
        return "Classified as No "
