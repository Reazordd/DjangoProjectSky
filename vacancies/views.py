from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from vacancies.models import Vacancy
import json

def hello(request):
    return HttpResponse("Hello world")

@method_decorator(csrf_exempt, name="dispatch")
class VacancyView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        search_text = request.GET.get("text", None)
        if search_text:
            vacancies = vacancies.filter(text__icontains=search_text)

        response = []
        for vacancy in vacancies:
            response.append({
                "id": vacancy.id,
                "text": vacancy.text
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        vacancy_data = json.loads(request.body)
        vacancy = Vacancy()
        vacancy.text = vacancy_data["text"]
        vacancy.save()
        return JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })

class VacancyDetailView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        return JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })