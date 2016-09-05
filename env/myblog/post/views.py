from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .form import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# function based views

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'New Post Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    messages.error(request, 'Not Saved Properly!!!')
    return render(request, 'post_form.html', context)

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title" : instance.title,
        'instance': instance,
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    query_set_list = Post.objects.all().order_by("-timestamp")#line all the post in reverse order
    paginator = Paginator(query_set_list, 10) # Show 25 contacts per page
    page_request_var = 'page'#pagnition
    page = request.GET.get(page_request_var)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
        'obj_list': query_set_list,
        'title': 'Blog List',
        'contacts': contacts
    }
    return render(request, 'post_list.html', context)

def post_update(request,id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Saved!!!')
        return HttpResponseRedirect(instance.get_absolute_url())
    content = {
        'title': 'update',
        'instance': instance,
        'form': form,
    }
    return render(request, 'post_form.html', context)

def post_delete(request):
    intance = get_object_or_404(request, commit=False)
    instance.delete()
    messages.success(request, 'Item Deleted Successfully!!!')

def form_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        #if theres already such a form, we gonna redirect to its link and edit it
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "New Form Create Successfully")
        return HttpResponseRedirect(instance.get_absolute_url())
    content = {
        'form': form
    }
    return render(request, 'post_form.html', content)
