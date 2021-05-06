from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . models import SurveyEntry


def home_view(request):
    if request.method == 'POST':
        input = request.POST.get
        dict = {}
        query_set = SurveyEntry.objects.all()
        dict['location'] = input('location', False)
        dict['Comment'] = input('comment', False)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        if str(uploaded_file_url)[0] == '/':
            uploaded_file_url=uploaded_file_url[1:]
        dict['media'] = request.build_absolute_uri('/')+uploaded_file_url
        if dict:
            SurveyEntry.objects.create(**dict)
        return render(request, "home.html", {'query_set': query_set})
    return render(request, "home.html")
