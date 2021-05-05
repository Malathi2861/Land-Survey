from django.shortcuts import render
from . models import SurveyEntry
# from templates import home

def home_view(request):
    # print(request.POST)
    input = request.GET
    dict = {}
    print(111, input)
    print(22, type(input))
    print(33, request.GET['location'])
    if input['location'] is not [None, '']:
        dict['location'] = input['location']
    if input['comment'] is not ['']:
        dict['Comment'] = input['comment']
    if input['Choose file'] is not ['']:
        dict['media'] = input['Choose file']
    # date =
    output = SurveyEntry.objects.create(**dict)
    print(output)
    query_set = SurveyEntry.objects.all()
    for i in query_set:
        print('entered into loop')
        print(i.location,
              i.date,
              i.Comment,
              i.media)
        print('end of the loop')
    return render(request, "home.html", {'query_set': query_set})
