from django.db import models

class Lecture(models.Model):
    subject = models.CharField(max_length=100)
    dept = models.CharField(max_length=150)
    professor = models.CharField(max_length=50)
    instruction_id = models.CharField(max_length=100)
    rq_year = models.CharField(max_length=150)
    rq_semester = models.CharField(max_length = 100)
    area = models.CharField(max_length = 100)
    url = models.CharField(max_length = 100)
    credit = models.CharField(max_length = 100)
    class_time = models.CharField(max_length=100)
    required = models.BooleanField()    
    foreginer = models.BooleanField()
    team_teaching = models.BooleanField()
    mooc = models.BooleanField()
    online = models.BooleanField()
    number_of_people = models.BooleanField()
    note = models.BooleanField()

    def __str__(self):
        return self.subject
    

