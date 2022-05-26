from django.urls import path
from .views import SignUpView, userEditView, ShowProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', userEditView.as_view(), name='edit_profile'),
    path('<int:pk>/ profile', ShowProfileView.as_view(), name="show_profile"),
]
