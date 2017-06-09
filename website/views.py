# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


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