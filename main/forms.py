from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Catergory
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields=["title","content","image","cat"]
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'text-base p-2 border border-gray-800 rounded-lg focus:outline-none focus:border-indigo-500'}),
            'content': forms.Textarea(attrs={'class':'','placeholder':'Write Here','id':'editor'}),
            'image': forms.FileInput(attrs={'class':'hidden'}),
            'cat': forms.Select(attrs={'class':'text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800'}),
            # 'title': forms.TextInput(attrs={'class':'text-black w-3/4 mx-5 my-5'}),
            # 'content': forms.Textarea(attrs={'class':'text-black w-3/4 mx-5 my-10 mb-10','id':'editor'}),
            # 'cat': forms.Select(attrs={'class':'text-black w-3/4 mx-5 mb-5'}),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Catergory 
        fields=["title","description","image","url"]
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'text-black w-3/4 mx-5 my-5 px-4 py-2'}),
            'description': forms.Textarea(attrs={'class':'text-black w-3/4 mx-5 my-4 px-4 py-2' ,'id':'editor'}),
            'url': forms.TextInput(attrs={'class':'text-black w-3/4 mx-5 my-4 mb-10 px-4 py-2','id':'editor'}),
            'image': forms.FileInput(attrs={'class':'text-white w-3/4 mx-5 my-5'}),
        }
        
 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Unused


# class RegistrationFrom(UserCreationForm): 
#     # username = forms.CharField(required=True,help_text='Enter Username',widget=forms.CharField(attrs={'class':'bg-black'}))
#     email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email Address','class':'block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40'}))
#     password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40'}))
#     password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Enter Password Again','class':'block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40'}))
#     class Meta:
#         model = User
#         fields =["username","email",'password1',"password2"]
        
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder':'Enter Your Email Address','class':'block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40'})
#         }