from django.urls import path, include
from app.controllers.enum import get_enum_values
from app.routes import delivery, storage, user

app_name = "storage"
urlpatterns = [
    #Inventory urlpatterns
    path('', include(user.urlpatterns)),
    path('', include(storage.urlpatterns)),
    path('', include(delivery.urlpatterns)),
    path('enum/get', get_enum_values, name='get-enum-values'),
    
]   