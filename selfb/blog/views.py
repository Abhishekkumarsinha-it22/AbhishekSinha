from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Projects,Fav,Introduction,categories,HeadIntro,Sharing,comments
from django.core.paginator import Paginator
from .form import commentform

def categ(request,cats):
    cats1 = categories.objects.all()
    cat2 = Projects.objects.filter(categ=cats)
    p1 = Paginator(cat2, 3)
    page_n1 = request.GET.get('page')
    '''post1 = p.get_page(page)'''

    try:
        cat3 = p1.page(page_n1)
    except:
        cat3 = p1.page(p1.num_pages)

    return render(request, 'blog/categories.html', {'cats': cats, 'cat3': cat3, 'cats1': cats1})



def blogview(request):
    Pro = Projects.objects.all()
    fav = Fav.objects.all()
    Intro = Introduction.objects.all()

    return render(request, 'blog/index.html', {'Pro': Pro, 'fav': fav, 'Intro': Intro})

def blogpage(request):
    pro1 = Projects.objects.all()
    share = Sharing.objects.all()
    cat = categories.objects.all()
    head = HeadIntro.objects.all()

    p1 = Paginator(pro1, 3)
    page_n1 = request.GET.get('page')
    '''post1 = p.get_page(page)'''

    try:
        pro = p1.page(page_n1)
    except:
        pro = p1.page(p1.num_pages)



    return render(request, 'blog/blog.html',{'pro': pro,'cat': cat,'share':share,'head': head})


def blogsinglepage(request, id):
    post1 = Projects.objects.filter(proid=id)
    post3 = get_object_or_404(Projects,proid=id)
    comment = comments.objects.filter(coment=post3)
    r = id


    if request.method == 'POST':
        coform = commentform(request.POST or None)
        if coform.is_valid():
            content = request.POST.get('comments1')
            name = request.POST.get('name')
            mail = request.POST.get('email')
            comment = comments.objects.create(coment=post3, name=name, email=mail, comment=content)
            comment.save()
            return HttpResponseRedirect('/blog/blogpage')
    else:
        coform = commentform()


    cats1 = categories.objects.all()
    sidetext = HeadIntro.objects.all()
    share = Sharing.objects.all()

    return render(request,'blog/single.html',{'post':post1,'cats1':cats1,'sidetext':sidetext,'share':share, 'comment_form':coform, 'comment':comment})

