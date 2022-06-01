from ast import Delete
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Hero, Villain, Comic
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comics'] = Comic.objects.all()
        return context

class About(TemplateView):
    template_name = 'about.html'

class HeroesList(TemplateView):
    template_name = 'heroes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heroes'] = Hero.objects.all()
        return context

class HeroCreate(CreateView):
    model = Hero
    fields = ['name', 'secret_identity', 'img', 'bio', 'powers', 'universe', 'affiliations', 'villains']
    template_name = 'hero_create.html'
    def get_success_url(self):
        return reverse('hero_detail', kwargs={'pk': self.object.pk})

class HeroDetail(DetailView):
    model = Hero
    template_name = 'hero_detail.html'

class HeroUpdate(UpdateView):
    model = Hero
    fields = ['name', 'secret_identity', 'img', 'bio', 'powers', 'universe', 'affiliations', 'villains']
    template_name = 'hero_update.html'
    def get_success_url(self):
        return reverse('hero_detail', kwargs={'pk': self.object.pk})

class HeroDelete(DeleteView):
    model = Hero
    template_name = 'hero_delete_confirmation.html'
    success_url = '/heroes/'

class VillainsList(TemplateView):
    template_name = 'villains_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['villains'] = Villain.objects.all()
        return context

class VillainDetail(DetailView):
    model = Villain
    template_name = 'villain_detail.html'

class VillainCreate(CreateView):
    model = Villain
    fields = ['name', 'img', 'bio', 'powers', 'universe', 'affiliations', 'nemesis', ]
    template_name = 'villain_create.html'
    def get_success_url(self):
        return reverse('villain_detail', kwargs= {'pk': self.object.pk})

class VillainUpdate(UpdateView):
    model = Villain
    fields = ['name', 'img', 'bio', 'powers', 'universe', 'affiliations', 'nemesis', ]
    template_name = 'villain_update.html'
    def get_success_url(self):
        return reverse('villain_detail', kwargs= {'pk': self.object.pk})

class VillainDelete(DeleteView):
    model = Villain
    template_name = 'villain_delete_confirmation.html'
    success_url = '/villains/'

class ComicAppearance(View):

    def get(self, request, pk, hero_pk):
        assoc = request.GET.get("assoc")
        if assoc == 'remove':
            Comic.objects.get(pk=pk).heroes.remove(hero_pk)
        if assoc == 'add':
            Comic.objects.get(pk=pk).heroes.add(hero_pk)
        return redirect('home')