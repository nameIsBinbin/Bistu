#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:11 
# @Author : ryuchen
# @Site :  
# @File : urls.py 
# @Desc : 
# ==================================================
from django.conf.urls import url
from .views import MajorList, MajorDetail, AcademyList, AcademyDetail, ResearchList, ResearchDetail
from .views import OpeningReportList, OpeningReportUpload
from .views import ReformList, ReformUpload
from .views import PaperList, PaperUpload

urlpatterns = [
    url(r"^research/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", ResearchDetail.as_view(),
        name="research-detail"),
    url(r"^researches/$", ResearchList.as_view(), name="research-list"),
    url(r"^majors/$", MajorList.as_view(), name="major-list"),
    url(r"^major/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", MajorDetail.as_view(),
        name="major-detail"),
    url(r"^academies/$", AcademyList.as_view(), name="academy-list"),
    url(r"^academy/(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})$", AcademyDetail.as_view(),
        name="academy-detail"),

    url(r"^opening_reports/$", OpeningReportList.as_view(), name="opening_report-list"),
    url(r"^opening_report_upload/$", OpeningReportUpload.as_view(), name="opening_report-upload"),

    url(r"^reforms/$", ReformList.as_view(), name="reform-list"),
    url(r"^reform_upload/$", ReformUpload.as_view(), name="reform-upload"),

    url(r"^papers/$", PaperList.as_view(), name="paper-list"),
    url(r"^paper_upload/$", PaperUpload.as_view(), name="paper-upload"),
]
