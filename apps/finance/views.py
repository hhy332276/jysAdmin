from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(requests):
    return render(requests,'finance/index.html')

