from ast import Delete
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Hero, Villain, HeroTeam, VillainTeam
from django.urls import reverse
from django.shortcuts import redirect, render
# at top of file with other imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heroteams'] = HeroTeam.objects.all()
        context['villainteams'] = VillainTeam.objects.all()
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
    fields = ['name', 'secret_identity', 'img', 'bio', 'abilities', 'affiliations', 'villains']
    template_name = 'hero_create.html'
    def get_success_url(self):
        return reverse('hero_detail', kwargs={'pk': self.object.pk})

class HeroDetail(DetailView):
    model = Hero
    template_name = 'hero_detail.html'

class HeroUpdate(UpdateView):
    model = Hero
    fields = ['name', 'secret_identity', 'img', 'bio', 'abilities', 'affiliations', 'villains']
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
    fields = ['name', 'img', 'bio', 'abilities', 'affiliations', 'nemesis']
    template_name = 'villain_create.html'
    def get_success_url(self):
        return reverse('villain_detail', kwargs= {'pk': self.object.pk})

class VillainUpdate(UpdateView):
    model = Villain
    fields = ['name', 'img', 'bio', 'abilities', 'affiliations', 'nemesis']
    template_name = 'villain_update.html'
    def get_success_url(self):
        return reverse('villain_detail', kwargs= {'pk': self.object.pk})

class VillainDelete(DeleteView):
    model = Villain
    template_name = 'villain_delete_confirmation.html'
    success_url = '/villains/'

class HeroTeamCreate(CreateView):
    model = HeroTeam
    fields = ['name', 'img', 'heroes']
    template_name = 'heroteam_create.html'
    def get_success_url(self):
        return reverse('heroteam_detail', kwargs={'pk': self.object.pk})

class HeroTeamDetail(DetailView):
    model = HeroTeam
    template_name = 'heroteam_detail.html'

class HeroTeamUpdate(UpdateView):
    model = HeroTeam
    fields = ['name', 'img', 'heroes']
    template_name = 'heroteam_update.html'
    def get_success_url(self):
        return reverse('heroteam_detail', kwargs= {'pk': self.object.pk})

class HeroTeamDelete(DeleteView):
    model = HeroTeam
    template_name = 'heroteam_delete_confirmation.html'
    success_url = 'home'

class VillainTeamCreate(CreateView):
    model = VillainTeam
    fields = ['name', 'img', 'villains']
    template_name = 'villainteam_create.html'
    def get_success_url(self):
        return reverse('villainteam_detail', kwargs={'pk': self.object.pk})

class VillainTeamDetail(DetailView):
    model = VillainTeam
    template_name = 'villainteam_detail.html'

class VillainTeamUpdate(UpdateView):
    model = VillainTeam
    fields = ['name', 'img', 'villains']
    template_name = 'villainteam_update.html'
    def get_success_url(self):
        return reverse('villainteam_detail', kwargs= {'pk': self.object.pk})

class VillainTeamDelete(DeleteView):
    model = VillainTeam
    template_name = 'villainteam_delete_confirmation.html'
    success_url = 'home'



class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
