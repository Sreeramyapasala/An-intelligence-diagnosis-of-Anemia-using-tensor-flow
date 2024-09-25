from django.shortcuts import render
from django.views import View

class Android(View):
    def get(self,request):
        return render(request,"1_Landing.html")


from PIL import Image
import numpy as np
from django.http import JsonResponse
from keras.models import load_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def upload_image(request):
    if 'image' in request.FILES:
        
        uploaded_image = request.FILES['image']
        
        result = image_processing(uploaded_image)
        

        response_data = {'message': result}
        print(response_data)
        return JsonResponse(response_data, status=201)

    else:
        response_data = {'error': 'No image provided'}
        print(response_data)
        return JsonResponse(response_data, status=400)
    
from PIL import Image, ImageOps



model = load_model("C:/Users/91799/Music/Anemia/Deploy/PROJECT/Android/keras_model.h5")


def image_processing(uploaded_image): 

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(uploaded_image).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['Anemia','NoAnemia']
        prediction = model.predict(data)
        idd = np.argmax(prediction)
        predicted_class = (classes[idd])
        if predicted_class == 'Anemia':
            result = 'Anemia'
        elif predicted_class == 'NoAnemia':
            result = 'NoAnemia'
        else:
            result = 'WRONG INPUT'
        return result


