from django.shortcuts import render
from .models import example, example_run
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
from .forms import UploadFileForm
import pandas as pd
import subprocess
import os

# constant path file for solver
ROOT = os.getcwd() # Get current directory which run script
file_input_path = ROOT + '/data_user_temp/request_file_of_user.csv'
file_output_path = ROOT + '/data_user_temp/out_graph.html'
exe_path = ROOT + "/build_solver/dist/solver"

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # get file input for solver from user by POST method HTTP
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)
            # Save file was recieved from user
            df.to_csv(file_input_path)
            
            # Call exe parse input, output path and exe path
            subprocess.call([exe_path, file_input_path, file_output_path])
            
            # Read html output file from solver
            with open(file_output_path, 'r') as file:
                graph = file.read()
            
            # Return file html for render result
            return render(request, 'convex_hull.html', {'graph': graph})

    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

# Create your views here.
def home (request):
    
    return render(request, "index.html")