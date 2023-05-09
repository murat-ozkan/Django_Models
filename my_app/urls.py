from django.urls import path
from .views import goodbye, hello
from main.urls import home

# after '/my_app'
urlpatterns = [
    path('', home),
    path('hello/', hello),
    path('goodbye/', goodbye)

]
