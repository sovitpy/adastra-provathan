from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, RiskPercentange

# Create your views here.


@csrf_exempt
def addHeartBeat(request):
    """
    request:
        label: str
        value: int
    """
    json_body = json.loads(request.body)
    patient = RiskPercentange.objects.create(
        patient_id=1, label=json_body["label"], value=json_body["value"])
    return HttpResponse("OK")

@csrf_exempt
def getPatient(request):
    risks = Patient.objects.filter(pk=1)
    qs = serializers.serialize("json", risks)
    return HttpResponse(f"{qs}", content_type="application/json")

@csrf_exempt
def getHeartBeat(request):
    risks = RiskPercentange.objects.all()
    qs = serializers.serialize("json", risks)
    return HttpResponse(f"{qs}", content_type="application/json")



def changeBP(request, bp):
    patient = Patient.objects.get(pk=1)
    patient.blood_pressure = float(bp)
    patient.save()
    return HttpResponse("ok")

def changeHeartBeat(request, heartBeat):
    patient = Patient.objects.get(pk=1)
    patient.heartbeats = float(heartBeat)
    patient.save()
    return HttpResponse("ok")

