from django.shortcuts import render
import os


def index(request):
    print(os.environ.get("PROD_URL"))
    return render(request, "index.html", {"PROD_URL": os.environ.get("PROD_URL")})
