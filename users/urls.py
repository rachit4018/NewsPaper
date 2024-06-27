from django.urls import reverse_lazy,path
from .views import SignUpView

urlpatterns =[
    path('signup/', SignUpView.as_view(),name='signup'),
]