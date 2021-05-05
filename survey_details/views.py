from django.shortcuts import render
from . models import SurveyEntry


def home_view(request):
    if request.method == 'GET':
        input = request.GET
        dict = {}
        query_set = SurveyEntry.objects.all()
        if input.get('location', False):
            dict['location'] = input['location']
        if input.get('comment', False):
            dict['Comment'] = input['comment']
        if input.get('Choose file', False):
            dict['media'] = input['Choose file']
        if dict:
            SurveyEntry.objects.create(**dict)
        return render(request, "home.html", {'query_set': query_set})
