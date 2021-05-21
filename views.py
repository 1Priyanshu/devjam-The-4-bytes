from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import post,Rating
from .forms import Reviewform
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse, reverse_lazy



def Upvoteview(request,pk):
    Post = get_object_or_404(post, id=request.POST.get('post_id'))
    Post.upvotes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail',args = [str(pk)]))

def about(request):
    return render(request,'blog/about.html')


def contact(request):
    return render(request,'blog/contact.html')


def home(request):
    context = {
        'posts':post.objects.all()
    }
    return render(request,'blog/home.html',context) 

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-dateposted']
  
  
  
    
class PostDetailView(DetailView):
    model = post

    





class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['Project_name' , 'Content' , 'Brief' , 'TAGS','Link' , 'Image' ]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    

        
class PostUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin):
    model = post
    fields = ['Project_name' , 'Content' , 'Brief' , 'TAGS']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
             return False


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    form_class=Reviewform
    
    

    

# Create your views here.
