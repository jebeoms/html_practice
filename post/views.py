from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from bcuser.models import Bcuser

def post_list(request):
    posts=Post.objects.all()
    return render(request,'post_list.html',{'posts':posts})


def post_detail(request, pk):
    # 해당 댓글를 찾지 못하면 서버는 404 에러를 반환
    post=get_object_or_404(Post, pk=pk) # Post : models의 Post 데이터베이스
    comments=post.comments.all()

    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            # commit=False : 데이터베이스에 즉시 저장하지 말고 객체를 반환하여 수정을 허용
            comment.post=post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form=CommentForm()

    return render(request, 'post_detail.html', {'post':post,'comments':comments,'comment_form':comment_form})



def post_new(request):
    if request.method == 'POST':
        # form=PostForm(request.POST) # 입력정보 받아오기
        form=PostForm(request.POST, request.FILES)
        if form.is_valid(): #title, body 갖고 왔니?
            post=form.save(commit=False)
            user_id=request.session.get('user')
            bloguser=Bcuser.objects.get(pk=user_id)
            post.author=bloguser
            # post.author = request.user
            post.publiShed_date = timezone.now()
            # post.imgfile = request.FILES['imgfile']
            post.save()
            return redirect('post_list') # post 후 목록확인
    else:
        form=PostForm()
    return render(request, 'post_new.html', {'form':form})

# pk=post.pk

def post_modify(request ,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            user_id = request.session.get('user')
            bloguser = Bcuser.objects.get(pk=user_id)
            post.author = bloguser
            post.publiShed_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_modify.html', {'form': form})

# def post_modify(request, post_id):
#     post = Post.objects.get(id=post_id)
#     if request.method == "POST":
#         post.title = request.POST['title']
#         post.body = request.POST['body']
#         post.date = timezone.now()
#     try:
#         post.image = request.FILES['image']
#     except:
#         post.image = None
#         post.save()
#         return redirect('/detail/'+str(post.id),{'post':post})
#     else:
#         post=Post()
#         return render(request, 'post_modify.html', {'post':post})

# def product_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES) # 꼭 !!!! files는 따로 request의 FILES로 속성을 지정해줘야 함
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.author = request.user
#             product.detailfunc = product.detailfunc.replace("'", "").replace("[", "").replace("]", "")
#             product.save()
#             return redirect('sales:index')
#     else:
#         form = PostForm() # request.method 가 'GET'인 경우
#     context = {'form':form}
#     return render(request, 'post/product_form.html', context)