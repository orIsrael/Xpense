from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
<<<<<<< HEAD
from django.views import generic
from .models import UserProfile
from .forms import editProfileForm, ProfileForm
=======
from django.views.generic import CreateView, UpdateView
from .forms import editProfileForm
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


<<<<<<< HEAD
class userEditView(generic.UpdateView):
=======
class userEditView(UpdateView):
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)
    form_class = editProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


<<<<<<< HEAD
class ShowProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/show_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        user_page = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context['user_page'] = user_page

        return context
=======
# class ShowProfileView(DetailView):
#     form_class = ProfileForm
#     template_name = 'registration/user_profile.html'

#     def get_context_data(self, *args, **kwargs):
#         users = UserProfile.objects.all()
#         context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

#         page_user = get_object_or_404(UserProfile, self.kwargs['pk'])

#         context["page_user"] = page_user
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)
