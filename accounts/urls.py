from django.urls import path

from .views import SignUpView, userEditView, userProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', userEditView.as_view(), name='edit_profile'),
    path('show_profile/', userProfileView.as_view(), name='show_profile'),
]
