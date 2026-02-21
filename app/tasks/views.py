from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
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

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title"]
    template_name = "tasks/partials/task_edit_form.html"

    def get_queryset(self):
        return Task.objects.filter(project__user=self.request.user)

    def form_valid(self, form):
        self.object = form.save()
        html = render_to_string(
            "tasks/partials/task_item.html",
            {"task": self.object},
            request=self.request
        )
        return HttpResponse(html)

    def form_invalid(self, form):
        html = render_to_string(
            "tasks/partials/task_edit_form.html",
            {"form": form, "task": self.object},
            request=self.request
        )
        return HttpResponse(html, status=400)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(project__user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse("")

class TaskToggleDoneView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, project__user=request.user)
        task.is_done = not task.is_done
        task.save()
        html = render_to_string(
            "tasks/partials/task_item.html",
            {"task": task},
            request=request
        )
        return HttpResponse(html)

class TaskUpdateDeadlineView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["deadline"]

    # User validation
    def get_queryset(self):
        return Task.objects.filter(project__user=self.request.user)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(
            request,
            "tasks/partials/task_deadline_form.html",  # твой шаблон формы
            {"task": self.object}
        )

    def form_valid(self, form):
        self.object = form.save()
        return render(
            self.request,
            "tasks/partials/task_item.html",
            {"task": self.object}
        )