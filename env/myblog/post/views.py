from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .form import PostForm
# Create your views here.
# function based views

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
        messages.success(request, 'Saved!!!')
    else:
        content = {
            "title": 'Create',
            'form': form,
        }
        messages.error(request, 'Not Saved Properly!!!')
        return render(request, 'form_detail', content)

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    content = {
        "title" : instance.title,
        'instance': instance,
    }
    return render(request, 'post_detail.html', content)

def post_list(request):
    query_set = Post.objects.all()
    content = {
        'obj_list': query_set,
        'title': 'List'
    }
    return render(request, 'index.html', content)

def post_update(request,id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Saved!!!')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        content = {
            'title': 'update',
            'form': form,
            'instance': instance,
        }
        messages.warning(request, "Not Saved Properly!!!")
        return render(request, 'post_form.html', content)

def post_delete(request):
    intance = get_object_or_404(request, commit=False)
    instance.delete()
    messages.success(request, 'Item Deleted Successfully!!!')

def form_create(request):
    if request.method == 'POST':
        #process the data from the request
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            content = {
                'form': form
            }
            return render(request, 'form_detail.html', content)
    else:
        #if the methos == 'GET' or other method, we create a new blank form
        form = PostForm()
        return render(request, 'form_detail.html', {'form':form})
