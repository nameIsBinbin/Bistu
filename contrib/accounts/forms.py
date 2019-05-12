#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-05-12 15:22
# @Author : ryuchen
# @Site :
# @File : forms.py
# @Desc :
# ==================================================
from .models import *

from core.definition.enums import *

from django.forms import ModelForm


StatusChoice = [(tag.name, tag.value) for tag in StatusChoice]
GenderChoice = [(choice.name, choice.value) for choice in GenderChoice]
MidCheckChoice = [(choice.name, choice.value) for choice in MidCheckChoice]
SpecialProgramChoice = [(tag.name, tag.value) for tag in SpecialProgramChoice]


class TutorForm(ModelForm):
    ACADEMIES = [(academy.uuid, academy.aca_cname) for academy in Academy.objects.all()]
    MAJORS = [(major.uuid, major.maj_name) for major in Major.objects.all()]
    EDUCATIONS = [(education.uuid, education.edu_study_major) for education in Education.objects.all()]

    def __init__(self, *args, **kwargs):
        super(TutorForm, self).__init__(*args, **kwargs)
        self.fields['tut_gender'].choices = GenderChoice
        self.fields['academy'].choices = self.ACADEMIES
        self.fields['education'].choices = self.EDUCATIONS

    class Meta:
        model = Tutor
        fields = '__all__'


class StudentForm(ModelForm):
    ACADEMIES = [(academy.uuid, academy.aca_cname) for academy in Academy.objects.all()]
    MAJORS = [(major.uuid, major.maj_name) for major in Major.objects.all()]
    CLASSES = [(item.uuid, item.cla_name) for item in Class.objects.all()]
    RESEARCHES = [(research.uuid, research.res_name) for research in Research.objects.all()]
    TUTORS = [(tutor.uuid, tutor.tut_name) for tutor in Tutor.objects.all()]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['stu_gender'].choices = GenderChoice
        self.fields['stu_academy'].choices = self.ACADEMIES
        self.fields['stu_major'].choices = self.MAJORS
        self.fields['stu_class'].choices = self.CLASSES
        self.fields['stu_research'].choices = self.RESEARCHES
        self.fields['stu_tutor'].choices = self.TUTORS
        self.fields['stu_mid_check'].choices = MidCheckChoice
        self.fields['stu_status'].choices = StatusChoice
        self.fields['stu_special_program'].choices = SpecialProgramChoice

    class Meta:
        model = Student
        fields = '__all__'
