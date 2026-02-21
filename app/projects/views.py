from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Project

# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    #User validation
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).order_by("-created_at")


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

    # User validation
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ["title", "description"]
    template_name = "projects/partials/project_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()

        if self.request.htmx:
            html = render_to_string(
                "projects/partials/project_card.html",
                {"project": self.object},
                request=self.request
            )
            return HttpResponse(html)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("projects:list")