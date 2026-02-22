from django.urls import path
from .views import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleDoneView, TaskUpdateDeadlineView, move_up, move_down

app_name = "tasks"

urlpatterns = [
    path("create/<int:pk>", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete"),
    path('<int:pk>/toggle/', TaskToggleDoneView.as_view(), name='toggle_done'),
    path('<int:pk>/update-deadline/', TaskUpdateDeadlineView.as_view(), name='update_deadline'),
    path("<int:pk>/move-up/", move_up, name="move_up"),
    path("<int:pk>/move-down/", move_down, name="move_down"),
]

