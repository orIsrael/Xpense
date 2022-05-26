from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile
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


class ShowProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/show_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        user_page = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context['user_page'] = user_page

        return context
