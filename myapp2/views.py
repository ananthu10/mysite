from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {'insert_me': "hello ia ma ananathu  its return ed from python",
               "test": "testing##########"}
    return render(request, 'myapp2/index.html', context=my_dict)
