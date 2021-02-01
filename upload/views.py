from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Upload, Comment
from .forms import UploadCreateForm, CommentForm, AddCreateForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import requests




@login_required
def publication_list(request):
    items = Upload.objects.all()
    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    items = paginator.get_page(page)


    return render(request,  'upload/publication_list.html',
                            {'items': items,
                             'section': 'publications'})

@login_required
def add_publication (request):
    if request.method == 'POST':
        form = AddCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload:publication_list')
    else:
        form = AddCreateForm()
        return render(request, 'upload/add_publication.html', {'form': form,
                                                               'section': 'publications'})

@login_required
def upload_publication (request):
    if request.method == 'POST':
        form = UploadCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = UploadCreateForm()
    return render(request, 'upload/upload_publication.html',
                  {'section': 'publications',
                   'form': form})

@login_required
def upload_details(request, id, Issn, **kwargs):
    post = get_object_or_404(Upload,
                                 id=id,
                                 Issn=Issn)
    is_liked = False
    if post.liked.filter(id=request.user.id).exists():
        is_liked = True
    comments = Comment.objects.filter(post=post).order_by('-id')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(post=post, user=request.user, body=body)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()


    url='https://api.elsevier.com/content/serial/title/issn/{}?apiKey=7f348b8072bf6e1e049d8746d93b51d4'
    issns = post.Issn

    r = requests.get(url.format(issns)).json()

    issn_details = {

        'dc_publisher': r['serial-metadata-response']['entry'][0]['dc:publisher'],
        'startcover': r['serial-metadata-response']['entry'][0]['coverageStartYear'],
        'endcover': r['serial-metadata-response']['entry'][0]['coverageEndYear'],
        'subjectarea': r['serial-metadata-response']['entry'][0]['subject-area'][0]['$'],
        'subjectarea1': r['serial-metadata-response']['entry'][0]['subject-area'][-1]['$'],
    }

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'issn_details': issn_details,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),

    }
    return render(request,
                  'upload/details.html',
                   context)

@login_required
def like_public(request):
    post = get_object_or_404(Upload, id=request.POST.get('post_id'))
    is_liked = False
    if post.liked.filter(id=request.user.id).exists():
        post.liked.remove(request.user)
        is_liked = False
    else:
        post.liked.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())

@login_required
def delete_publication(request, id):
        Upload.objects.filter(id=id).delete()
        itemes = Upload.objects.all()
        return redirect('upload:publication_list')
        return render(request, 'upload/publication_list.html', {'section': 'publications',
                                                                'itemes': itemes})






# Create your views here.
