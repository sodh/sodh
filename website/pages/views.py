from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext, loader
from django.contrib import messages

def home(request):
    '''
    This is the homepage of the website.
    '''

    template = loader.get_template('pages/index.html')

    if request.method == 'POST':
        command = request.POST.get('command')
        selectedFile = request.POST.get('selectedFIle')

        if command is not '':
            messages.success(request, "Please wait while \"%s\" is executed on %s." % (command, selectedFile) )
        else:
            messages.error(request, "Please type in a valid command.")

    context = RequestContext(request, {
        'title': "Sodh : Generic Research Assistant",
        'menuindex': 1,
        'messages': messages,
    })

    return HttpResponse(template.render(context))
