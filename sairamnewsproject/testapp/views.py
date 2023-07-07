from django.shortcuts import render

# Create your views here.
def new_info(request):
    return render(request,'testapp/index.html')

def movies_info(request):
    head_msg='Movies Information'
    sub_msg1='RRR - NATU NATU song won OSCAR'
    sub_msg2='DAS KA DAMKI was a HIT movie'
    sub_msg3='Yesterday DASARA was released'
    type = 'movies'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_info(request):
    head_msg='Sports Information'
    sub_msg1='IPL as started'
    sub_msg2='MI vs RCB'
    sub_msg3='RCB wom 2023 TATA IPL CUP'
    type = 'sports'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_info(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'India Pm was Modi ji'
    sub_msg2 = 'April Budget has released'
    sub_msg3 = 'Andhara Pradesh CM Chandra Babu Naidu Sir'
    type = 'politics'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
