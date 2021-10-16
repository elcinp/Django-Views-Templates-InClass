from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def home(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request,'app/home.html',context)




# if request.method == 'GET':
#         print(f'You are using {request.method} Method!')

    # print(request.user)
    # AnonymousUser

    # print(request.path)
    # /

    # print(request.method)
    # print(request.META)