from django.urls import path
from . import views
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add/', views.AddView.as_view()),
    # path('about/', TemplateView.as_view(template_name='todo/about.html'))
    path('about/', views.AboutView.as_view()),
    # path('about/<str:name_from_url>/', views.AboutView.as_view()),
    # path('about/<int:id>/', RedirectView.as_view(url='/about/')),
    path('about/<str:id>/', views.RedirectAbout.as_view()),
    path('redirect/', views.RedirectAbout_1.as_view()),
    # path('todo/<int:id>/', views.detailView, name="todo"),
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name="todo"),
    path('edit/<int:pk>/',views.EditTodoView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteTodoView.as_view(), name='delete'),
]
