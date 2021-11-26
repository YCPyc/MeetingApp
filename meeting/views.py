from django.shortcuts import render,redirect
from .models import Post
from .forms import DiscussionForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from django.http import JsonResponse
import json
# Create your views here.

# A function based view for front page
def frontPage(request):
    allPosts = Post.objects.all()
    return render(request,'meeting/frontpage.html',{'allPosts':allPosts})

# A function based view for topic detail page
def postDetail(request,pk):
    post = Post.objects.get(pk=pk)
    allPosts = Post.objects.all()
    # when a form is submitted
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('postDetail',pk = post.pk)
    else:
        form = DiscussionForm()
    # difficulty: mutiple views for one url
    return render(request,'meeting/posts_detail.html',{'post':post,'form':form, 'allPosts':allPosts})

# A class-based view for add page
class addPage(CreateView):
    model = Post
    template_name = 'meeting/addPage.html'
    fields=('title','time_duration','intro','body','image')

# A class-based view for update page
class updatePage(UpdateView):
    model = Post
    template_name = 'meeting/updatePage.html'
    fields=('title','time_duration','intro','body',)

# A class-based view for delete page
class deletePage(DeleteView):
    model = Post
    template_name = 'meeting/deletePage.html'
    fields=('title','time_duration','intro','body',)
    success_url = reverse_lazy('frontPage')

#video chatting:
twilio_account_sid = 'AC54aa1972e4451073618c2b5e4e5200f1'
twilio_api_key_sid = 'SKdc0e35e8eca2d4badf6643757ead6684'
twilio_api_key_secret = 'jGpDKQGSkKyveN2FCWPCT6QFRlwPMoPL'

fake = Faker()
def videologin(request,pk):
    
    identity = request.GET.get('identity', fake.user_name())
    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity = identity)
    token.add_grant(VideoGrant(room='MyRoom' ))
    response = {
        'identity': token.identity,
        #no decode
        'token': token.to_jwt()
       }

    return JsonResponse(response)
