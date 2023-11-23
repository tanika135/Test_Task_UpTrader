from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class MenuIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        return render(request, 'app_menu/index.html')
