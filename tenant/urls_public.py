from django.contrib import admin
from django.urls import path
from person_details_shared import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.shared_view),
]