from django.shortcuts import render
import requests
from .models import Lecture

url = "http://18.214.131.153:5000/course"

# Create your views here.

def lecture(request):
    response = requests.get(url)
    data = response.json()['data']

    for i in data:
        lecture = Lecture()
        lecture.subject = i['subject']
        lecture.dept = i['dept']
        lecture.professor = i['professor']
        lecture.instruction_id = i['instruction_id']
        lecture.rq_year = i['rq_year']
        lecture.rq_semester = i['rq_semester']
        lecture.area = i['area']
        lecture.url = i['url']
        lecture.credit = i['credit']
        lecture.class_time = i['class_time']
        lecture.required = i['required']
        lecture.foreigner = i['foreigner']
        lecture.team_teaching = i['team_teaching']
        lecture.mooc = i['mooc']
        lecture.online = i['online']
        lecture.number_of_people = i['number_of_people']
        lecture.note = i['note']
        
        lecture.save()

    return redirect('/')

def show_lecture(request):
    info_list = Lecture.objects.all()
    return render(request, 'test.html',{'info': info_list})



