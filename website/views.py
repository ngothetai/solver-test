from django.shortcuts import render
from .models import example, example_run
import pandas as pd
from plotly.offline import plot
import plotly.express as px

# Create your views here.
def home (request):
    return render(request, "index.html")