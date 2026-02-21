from django.urls import path
from .views import TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = "tasks"

urlpatterns = [
    path("create/<int:pk>", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete")
]

