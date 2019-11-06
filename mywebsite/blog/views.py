from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from blog import models, forms

 
def index(request):
    return render(request,'blog/index.html',{
        'title' : 'Ihsan Magazine',
        'content' : models.Post.objects.all
    })

def detail(request,id):
    try : 
        model = models.Post.objects.get(id=id)
    except Exception : 
        raise Http404 ()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('blog-detail', id=id)
    else:
        form = forms.CommentForm(initial={'post' : model})
    return render(request,'blog/detail.html', {
        'title' : model.title,
        'model' : model,
        'form': form
        
    })
    
 
# Create your views here.