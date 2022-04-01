from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import editProfileForm, ProfileForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class userEditView(generic.UpdateView):
    form_class = editProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class userProfileView(generic.DetailView):
    form_class = ProfileForm
    template_name = 'registration/show_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
