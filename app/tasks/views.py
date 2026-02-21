from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from projects.models import Project
from .models import Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]

    def form_valid(self, form):
        project = get_object_or_404(
            Project,
            pk=self.kwargs["pk"],
            user=self.request.user
        )
        form.instance.project = project
        self.object = form.save()

        html = render_to_string(
            "tasks/partials/task_item.html",
            {"task": self.object},
            request=self.request
        )
        return HttpResponse(html)
