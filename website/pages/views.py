from django.shortcuts import render
from django.contrib import messages

from mind.mapper import Mapper

def home(request):
    '''
    This is the homepage of the website.
    '''

    if request.method == 'POST':
        command = request.POST.get('command')
        selectedFile = request.POST.get('selectedFile')

        if command is not '' and selectedFile is not '':
            mapper = Mapper()
            mapper.mapRE("Cluster","mind/datasets/data_cluster3d.csv",command)

            messages.success(request, "Please wait while \"%s\" is executed on %s." % (command, selectedFile) )
        else:
            messages.error(request, "Please select a file and type in a valid command.")

    args = {
        'title': "Sodh : Generic Research Assistant",
    }

    return render(request, 'pages/index.html', args)
