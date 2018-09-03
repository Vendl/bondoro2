from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from posts import models
from posts.models import Hirek, Programok

class IndexView(TemplateView):
    template_name = 'posts/index.html'


class AboutView(TemplateView):
    template_name = 'posts/about.html'


class PressView(TemplateView):
    template_name = 'posts/press.html'


class ContactsView(TemplateView):
    template_name = 'posts/contacts.html'



class TamogatokListView(ListView):
    context_object_name = 'tamogatok'
    model = models.Tamogatok
    template_name = 'posts/sponsors.html'



class HirekListView(ListView):
    context_object_name = 'hirek'
    model = models.Hirek
    template_name = 'posts/hir_list.html'


    def get_queryset(self):
        return Hirek.objects.all()

class HirekDetailView(DetailView):
    context_object_name = 'hir'
    model = models.Hirek
    template_name = 'posts/hirek_detail.html'


class ProgramListView(ListView):
    context_object_name = 'programok'
    model = models.Programok
    template_name = 'posts/programok_list.html'

    def get_queryset(self):
        return Programok.objects.all()


class ProgramokDetailView(DetailView):
    context_object_name = 'program'
    model = models.Programok
    template_name = 'posts/programok_detail.html'





#
