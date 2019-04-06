#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-02 20:22 
# @Author : ryuchen
# @Site :  
# @File : views.py 
# @Desc : 
# ==================================================
import json
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from core.decorators.excepts import excepts
from contrib.users.models import Tutor, Education
from .serializers import TutorSerializers


def user_chanle(username):
	user = dict()
	if username:
		user['username'] = username
		user['first_name'] = username
		user['last_name'] = username
		user['password'] = make_password('1234567')
		user['is_superusre'] = False
		user['is_staff'] = True
		user['is_active'] = True
	return user


class SimpleTutor(object):
	model = Tutor
	queryset = Tutor.objects.all()
	serializer_class = TutorSerializers


class TutorDetail(SimpleTutor, generics.RetrieveUpdateDestroyAPIView):
	@excepts
	@csrf_exempt
	def get(self, request, *args, **kwargs):
		res = {
			"code": "00000000",
			"data": {
				"status": 200,
			}
		}
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		res['data'] = serializer.data
		return Response(res)

	@excepts
	@csrf_exempt
	def put(self, request, *args, **kwargs):
		res = {
			"code": "00000000",
			"data": {
				"status": 200,
			}
		}
		data = request.data
		username = data.get('user')
		data["user"] = user_chanle(username)
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=data, partial=partial, context={"academy": "", 'user': "", "education": ""})
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(res)

	@excepts
	@csrf_exempt
	def delete(self, request, *args, **kwargs):
		res = {
			"code": "00000000",
			"data": {
				"status": 200,
			}
		}
		instance = self.get_object()
		self.perform_destroy(instance)
		return Response(res)


class TutorList(SimpleTutor, generics.ListCreateAPIView):
	@excepts
	@csrf_exempt
	def get(self, request, *args, **kwargs):
		res = {
			'code': status.HTTP_200_OK,
			'data': []
		}
		queryset = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
		else:
			serializer = self.get_serializer(queryset, many=True)
		res["data"] = serializer.data

		return Response(res)

	# 添加
	@excepts
	@csrf_exempt
	def post(self, request, *args, **kwargs):
		res = {
			'code': status.HTTP_200_OK,
			'data': {}
		}
		data = request.data
		bulk = isinstance(data, list)
		if not bulk:
			username = data.get('user')
			data["user"] = user_chanle(username)
			serializer = self.get_serializer(data=data, context={"academy": "", 'user': "", "education": ""})
		else:
			for item in data:
				username = item['user']
				item["user"] = user_chanle(username)
			serializer = self.get_serializer(data=data, many=True, context={"academy": "", "user": "", "education": ""})
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		res['data'] = serializer.data
		return Response(res)
