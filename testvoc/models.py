#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=20)
    #a choice of question type
    CET4 = 'C4'
    CET6 = 'C6'
    TOEFL = 'TF'
    IELTS = 'IS'
    QUESTION_TYPE_CHOICE = (
        (CET4, 'CET4'),
        (CET6, 'CET6'),
        (TOEFL, 'TOEFL'),
        (IELTS, 'IELTS'),
    )
    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE_CHOICE,
        default=CET4,
    )


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    correct_choice = models.BooleanField(default=False)
    