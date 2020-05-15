from django.shortcuts import render, reverse, HttpResponseRedirect

from app.models import Post
from app.forms import PostForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def submission(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                is_boast=data['is_boast'],
                content=data['content']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = PostForm()
    return render(request, 'submission.html', {'form': form})
