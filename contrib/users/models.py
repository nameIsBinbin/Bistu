#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 10:22 
# @Author : ryuchen
# @Site :  
# @File : models.py 
# @Desc : 
# ==================================================
import uuid

from contrib.defines.enums import *
from contrib.academy.models import Academy, Major

from django.db import models
from django.contrib.auth.models import User


class Education(models.Model):
    """
    学历模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    edu_begin_time = models.DateField(help_text="开始时间")
    edu_finish_time = models.DateField(help_text="结束时间")
    edu_school_name = models.CharField(max_length=128, null=True, help_text="学校名称")
    edu_study_major = models.CharField(max_length=128, null=True, help_text="专业方向")

    def __str__(self):
        return "学校：{0}  专业：{1}".format(self.edu_school_name, self.edu_study_major)

    class Meta:
        verbose_name = "学历"
        verbose_name_plural = verbose_name


class Class(models.Model):
    """
    班级模型
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="唯一标识ID")
    cla_name = models.CharField(max_length=128, null=False, help_text="班级名称")
    cla_code = models.IntegerField(null=True, help_text="班级代码")

    def __str__(self):
        return "代码：{0}  名称：{1}".format(self.cla_code, self.cla_name)

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = verbose_name


class Tutor(models.Model):
    """
    导师模型
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tut_number = models.IntegerField(null=False, unique=True, help_text="导师工号")
    tut_gender = models.CharField(max_length=64, choices=[(tag.name, tag.value) for tag in GenderChoice], help_text="性别")
    tut_title = models.CharField(max_length=64, choices=[(tag.name, tag.value) for tag in TitleChoice], help_text="职称")
    tut_cardID = models.CharField(max_length=128, null=True, unique=True, help_text="身份证号")
    tut_birth_day = models.DateField(help_text="出生日期")
    tut_entry_day = models.DateField(help_text="入职日期")
    tut_political = models.CharField(max_length=64, choices=[(tag.name, tag.value) for tag in PoliticalChoice], help_text="政治面貌")
    tut_telephone = models.IntegerField(null=True, help_text="电话号码")
    tut_degree = models.CharField(max_length=64, choices=[(tag.name, tag.value) for tag in DegreeChoice], help_text="学位")
    education = models.OneToOneField(Education, null=True, on_delete=models.SET_NULL, help_text="学历")
    academy = models.OneToOneField(Academy, null=True, on_delete=models.SET_NULL, help_text="所属学院")
    major = models.ManyToManyField(Major)

    def __str__(self):
        return "工号：{0}  姓名：{1}".format(self.tut_number, self.user.last_name + self.user.first_name)

    class Meta:
        verbose_name = "导师"
        verbose_name_plural = verbose_name


class Student(models.Model):
    """
    学生模型
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_number = models.IntegerField(null=False, unique=True, help_text="学号")
    stu_gender = models.CharField(max_length=64, choices=[(tag.name, tag.value) for tag in GenderChoice], help_text="性别")
    stu_cardID = models.CharField(max_length=128, null=True, unique=True, help_text="身份证号")
    stu_birth_day = models.DateField(help_text="出生日期")
    stu_source = models.CharField(max_length=128, null=False, help_text="生源地")
    stu_political = models.CharField(max_length=64, choices=[(tag.name, tag.value) for tag in PoliticalChoice], help_text="政治面貌")
    stu_telephone = models.IntegerField(null=True, help_text="电话号码")
    stu_status = models.CharField(max_length=64, choices=[(tag.name, tag.value) for tag in StatusChoice], help_text="在校状态")
    stu_is_superb = models.BooleanField(default=False, help_text="是否优秀毕业生")
    stu_class = models.OneToOneField(Class, null=True, on_delete=models.SET_NULL, help_text="所属班级")
    education = models.OneToOneField(Education, null=True, on_delete=models.SET_NULL, help_text="学历")
    tutor = models.OneToOneField(Tutor, null=True, on_delete=models.SET_NULL, help_text="指导老师")
    major = models.OneToOneField(Major, null=True, on_delete=models.SET_NULL, help_text="学科专业")

    def __str__(self):
        return "学生编号：{0}     学生姓名：{1}".format(self.stu_number, self.user.last_name + self.user.first_name)

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name