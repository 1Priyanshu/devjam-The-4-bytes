from django.urls import path
from . import views
from .views import Upvoteview,ReviewCreateView,PostListView,PostCreateView,PostUpdateView,PostDetailView
urlpatterns = [
    path('',PostListView.as_view(), name = 'home'),
    path('post/<int:pk>/',PostDetailView.as_view() , name = 'post-detail'),
    path('post/new',PostCreateView.as_view() , name = 'post-create'),
    path('about/' , views.about,name ='blog-about' ),
    path('contact/' , views.contact,name ='contact' ),
    path('<int:pk>/update/',PostUpdateView.as_view() , name = 'post-update'),
    path('post/<int:pk>/review/',ReviewCreateView.as_view() , name = 'review'),
    path('post/<int:pk>/upvote',views.Upvoteview, name = 'upvote'),
]
 