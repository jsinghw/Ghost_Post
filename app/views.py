from django.shortcuts import render, reverse, HttpResponseRedirect

from app.models import Post
from app.forms import PostForm

# Create your views here.


def index(request, sort='', filter=''):
    sort = request.GET.get('sort')
    filter = request.GET.get('filter')

    if filter is None:
        if sort is None:
            data = Post.objects.all()
        else:
            if sort == 'vote_score':
                data = Post.objects.extra(
                    select={
                        'vote_score': 'upvotes - downvotes'
                    }).extra(
                        order_by=['-vote_score']
                )
            else:
                data = data.order_by(sort)
    else:
        if filter == 'is_boast=True':
            data = Post.objects.filter(is_boast=True)
        elif filter == 'is_boast=False':
            data = Post.objects.filter(is_boast=False)
        else:
            data = Post.objects.all()
        if sort is None:
            data = data.order_by()
        else:
            if sort == 'vote_score':
                data = Post.objects.extra(
                    select={
                        'vote_score': 'upvotes - downvotes'
                    }).extra(
                        order_by=['-vote_score']
                )
            else:
                data = data.order_by(sort)

    return render(request, 'index.html', {'data': data})


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


def upvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def downvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))
