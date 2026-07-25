from django.shortcuts import render

import time

from django.http import JsonResponse
from django.views import View

class HealthCheckView(View):
    def get(self, request):
        return JsonResponse(
            {"status":"alive", "time":time.time()},
            status=200            
        ) 