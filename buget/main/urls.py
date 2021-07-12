from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("update/<pk>", PlansUpdate.as_view(), name="update"),
    path("delete/<pk>", PlansDelete.as_view(), name="delete"),
    path("pay/<id>", pay, name="pay"),
]
