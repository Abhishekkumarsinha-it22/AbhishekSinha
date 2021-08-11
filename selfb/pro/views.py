from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blogpost,categories,comments
from django.http import HttpResponseRedirect
from .form import commentform
from django.shortcuts import render,get_object_or_404
# Create your views here.
def singleview(request, blocks):
    post2 = categories.objects.all()
    post3 = Blogpost.objects.filter(blogid=blocks)
    post4 = get_object_or_404(Blogpost, blogid=blocks)
    comment = comments.objects.filter(coment=post4)


    if request.method == 'POST':
        coform = commentform(request.POST or None)
        if coform.is_valid():
            content = request.POST.get('comment')
            name = request.POST.get('name')
            mail = request.POST.get('email')
            comment = comments.objects.create(coment=post4, name=name, email=mail, comment=content)
            comment.save()
            return HttpResponseRedirect('/pro/profp')
    else:
        coform = commentform()


    return render(request, 'pro/singlepage.html', {'post3': post3, 'blocks': blocks,'comment_form':coform, 'comment':comment,'post2':post2})


def profpf(request):
    post2 = categories.objects.all()
    post = Blogpost.objects.all().order_by('blogid')
    p = Paginator(post,3)
    page_n = request.GET.get('page')
    '''post1 = p.get_page(page)'''

    try:
        post1 = p.page(page_n)
    except:
        post1 = p.page(p.num_pages)



    return render(request, 'pro/index.html', {'post1': post1,'post2': post2})

def categories1(request, cats):
    post2 = categories.objects.all()
    post3 = Blogpost.objects.filter(categories=cats)
    p1 = Paginator(post3, 3)
    page_n1 = request.GET.get('page')
    '''post1 = p.get_page(page)'''

    try:
        post3 = p1.page(page_n1)
    except:
        post3 = p1.page(p1.num_pages)

    return render(request, 'pro/categories.html', {'cats': cats, 'post3': post3, 'post2': post2})


