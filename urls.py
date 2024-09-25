from django.urls import path
from . import views
urlpatterns = [
    path("",views.Android.as_view(),name="Android"),
    # path("api/upload/", views.ImageView.as_view(), name='image-upload'),
    path('upload-image/', views.upload_image, name='upload_image'),
]