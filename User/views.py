from django.shortcuts import render
from User.predection import getPrediction

# Create your views here.
def home(request):
    return render(request,'ai.html')

def predict(request):
    img = "Null"
    try:
        img = request.POST['imge']
    except KeyError:
        pass
    # except UnboundLocalError:
    #     img = request.POST['imge']
    # return render(request , 'ai.html' , {'result' : img})
    print("Hello" )
    print(img)
    val = getPrediction(img)
    return render(request,'ai.html',{'result':val})
