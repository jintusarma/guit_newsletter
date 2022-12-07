from django.shortcuts import render,redirect
from .forms import PostForm,CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .models import Post,Catergory

# for load more button
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def home(requests):
    posts = Post.objects.all()
    total_posts = Post.objects.count()
    # Ordering is done in models.py
    # posts = posts.order_by("-id")    
    cats = Catergory.objects.all()
        
    data = {
        'object_list': posts,
        'cat_list': cats,
        'total_posts':total_posts,
    }
    return render(requests,'main/home.html',data)

# def load_more(requests):
    offset = int(requests.POST['offset'])
    limit = 3
    print("Load more")
    posts = Post.objects.all()[offset:limit+offset]
    total_data = Post.objects.count()
    data={}
    posts_json = serializers.serialize('json',posts)
    return JsonResponse( data = {
            'posts':posts_json,
            'totalResults':total_data,
        }
    )

def load_more(request):
    offset=int(request.POST['offset'])
    limit=2
    posts=Post.objects.all()[offset:limit+offset]
    totalData=Post.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })

# def sign_up(requests):
#     if requests.method == 'POST':
#         form = RegistrationFrom(requests.POST)
#         if form.is_valid():
#             user = form.save()
#             login(requests,user)
#             return redirect('/home')
#     else:
#         form = RegistrationFrom()
        
#     return render(requests,'registration/signupform.html',{"form":form}) 


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signupform.html', {'form': form})

@login_required(login_url='/login')
def create_post(requests):
    if requests.method == 'POST':
        form = PostForm(requests.POST,requests.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = requests.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
    return render(requests,'main/uploadform.html',{"form":form})
    # return render(requests,'main/quill.html',{"form":form})
    
class Homeview(ListView):
    model, cat = Post, Catergory
    # to get newer posts 1st 
    def get_queryset(self, *args, **kwargs):
        # print("HOME REACHED")
        # print(kwargs, args)
        query_set = super(Homeview, self).get_queryset(*args, **kwargs)
        query_set = query_set.order_by("-id")
    
        return query_set
    
    template_name = 'main/home.html'
    

class EditnDeletePost(ListView):
    model = Post
    template_name= 'main/Admin/update_n_delete.html'
    
class ArticleDetailView(DetailView):
    model= Post
    template_name = 'main/test/blog.html'
    
class AddCategory(CreateView):
    model = Catergory
    form_class = CategoryForm
    template_name = 'main/Admin/add_category.html'
    # fields = '__all__'
    
class ViewCategory(ListView):
    model = Catergory
    template_name = 'main/view_category.html'
    
class DeletePost(DeleteView):
    model= Post
   
    success_url ="/"
    template_name = 'main/test/delete_post.html'

def approve_post(requests):
    blog_list = Post.objects.all().order_by('-add_date')
    if requests.user.is_superuser:
        if requests.method == "POST":
            id_list = requests.POST.getlist('boxes')        # to get the id of checked boxes and store it in the if_list as the boxes is the name of checkboxes
            
            # Uncheck all Blog
            blog_list.update(status=False)
                        
            # Update in Database
            for x in id_list:
                Post.objects.filter(pk=int(x)).update(status=True)
            return redirect('home')
        else:
            return render(requests,'main/Admin/Approval_Table.html',
                      {"blog_list":blog_list})
    else:
        # messages.success (requests, ("You aren't authorize to view this page"))
        
        return redirect('/home')
    return render(requests,'main/Admin/Approval_Table.html')


def category(requests, url):
    cat = Catergory.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    data = {
        'cat_list':cat,
        'object_list':posts,
    }
    return render(requests, 'main/test/category.html',data)