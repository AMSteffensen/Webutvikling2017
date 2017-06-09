# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader

from .forms import UsersForm


def index(request):
    template = loader.get_template('frontpage/frontpage.html')
    context = {}
    return HttpResponse(template.render(context, request))


def test(request):
    template = loader.get_template("dj-testing/test.html")

    name = "Daniel"
    favFood = "Bananas"

    context = {
        'myName': name,
        'myFood': favFood,
    }

    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template("dj-testing/about.html")
    context = {}
    return HttpResponse(template.render(context, request))


## User registration page
class UserFormView(View):
    form_class = UsersForm
    template_name = "user/registration/registration_form.html"


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # normalized data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('website:index')


        return render(request, self.template_name, {'form': form})













