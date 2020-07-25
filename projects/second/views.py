from django.shortcuts import render
from django.http import HttpResponseRedirect
from second.models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
             new_item = form.save()
        return HttpResponseRedirect('/second/list/')

    form = PostForm()
    return render(request, 'second/create.html', {'form': form})


def confirm(request):
    form = PostForm(request.POST)
#  PostForm생성자에 request.POST를 넣어주면 바로 알아서 데이터들이 매핑됨
    if form.is_valid():
        return render(request, 'second/confirm.html', {'form': form})
    return HttpResponseRedirect('/second/create/')