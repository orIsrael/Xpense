from django.urls import path
<<<<<<< HEAD
from .views import SignUpView, userEditView, ShowProfileView
=======

from .views import SignUpView, userEditView
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', userEditView.as_view(), name='edit_profile'),
<<<<<<< HEAD
    path('<int:pk>/ profile', ShowProfileView.as_view(), name="show_profile"),
=======
    # path('<int:pk>/profile/', ShowProfileView.as_view(), name='show_profile_page'),
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)
]
