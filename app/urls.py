from django.urls import path
import app.views

urlpatterns = [
    path('signup/', app.views.SignUp, name='signup'),
    path('login/', app.views.Login.as_view(), name='login'),
    path('validate_username/', app.views.validate_username, name='validate_username'),
]
