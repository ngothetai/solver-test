from django.shortcuts import render
from .models import example, example_run
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
from .forms import UploadFileForm
import pandas as pd
import subprocess
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.shortcuts import render

# constant path file for solver
ROOT = os.getcwd() # Get current directory which run script
file_input_path = os.path.join(ROOT, 'data_user_temp/request_file_of_user.csv')
file_output_path = os.path.join(ROOT, 'data_user_temp/out_graph.html')
exe_path = os.path.join(ROOT, 'utils/exe_solvers/ConvexHull/solver')


# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # get file input for solver from user by POST method HTTP
#             csv_file = request.FILES['file']
#             df = pd.read_csv(csv_file)
#             # Save file was recieved from user
#             df.to_csv(file_input_path)
            
#             # Call exe parse input, output path and exe path
#             subprocess.call([exe_path, file_input_path, file_output_path])
            
#             # Read html output file from solver
#             with open(file_output_path, 'r') as file:
#                 graph = file.read()
            
#             # Return file html for render result
#             return render(request, 'convex_hull.html', {'graph': graph})

#     else:
#         form = UploadFileForm()
#     return render(request, 'upload_file.html', {'form': form})

def process_form(request):
    # Get data from database
    solvers = example.objects.all()
    name_Solver = solvers.values_list('exampleName', flat=True)[0]
    description_Solver = solvers.values_list('description', flat=True)[0]
    image_Solver = solvers.values_list('image', flat=True)[0]
    exampleID = solvers.values_list('exampleID', flat=True)[0]

    if request.method == 'POST':
        
        # Get data from form
        print(request.POST)
        username = request.POST.get('userName')
        solverName = request.POST.get('solverName')
        upload_file = request.FILES.get('file')
        phoneNumber = request.POST.get('phoneNumber') # data type is string "on" or None
        
        # Process file input
        if upload_file:
            with open(file_input_path, 'wb+') as destination:
                for chunk in upload_file.chunks():
                    destination.write(chunk)
                    
            # Run example
            subprocess.call([exe_path, file_input_path, file_output_path])
            
            # Push data to database
            example_run.objects.create(userName=username, exampleID=exampleID, runStatus='success', paramList={'file_name': upload_file.name})
            
        
            # Read html output file from solver
            with open(file_output_path, 'r') as file:
                graph = file.read()
            
            # Return file html for render result
            # return render(request, 'website/convex_hull.html', {'graph': graph})
            return render(request, 'website/index.html', {'graph': graph, 'nameSolver': name_Solver, 'descriptionSolver': description_Solver, 'imageSolver': image_Solver})
        

        # Return file html for render upload page
    return render(request, 'website/index.html',  {'algorithm': 'DCA-CUT'})

# Create your views here.
def home (request):
    return render(request, "website/index.html")