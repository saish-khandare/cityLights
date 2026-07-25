from django.shortcuts import render


from django.http import JsonResponse
from django.views import View

class Flyer(View):
    def get(self, request):
        return JsonResponse({"flyer":"base"}, status=200)