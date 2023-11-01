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

# constant path file for solver
ROOT = os.getcwd() # Get current directory which run script
file_input_path = os.path.join(ROOT, 'data_user_temp/request_file_of_user.csv')
file_output_path = os.path.join(ROOT, '/data_user_temp/out_graph.html')
exe_path = os.path.join(ROOT, '/exe_solvers/ConvexHull/solver')


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
    if request.method == 'POST':
        # Lấy giá trị từ biểu mẫu
        username = request.POST.get('username')
        data_count = request.POST.get('dataCount')
        upload_file = request.FILES.get('file')
        add_to_database = request.POST.get('addToDatabase')

        # Xử lý dữ liệu theo nhu cầu
        if add_to_database:
            pass
            # Lưu trữ dữ liệu vào cơ sở dữ liệu ở đây (ví dụ: Django ORM)
            # Cần import và sử dụng các model và các phương thức lưu trữ dữ liệu của Django

        # Thực hiện xử lý khác (ví dụ: lưu trữ file tải lên)
        if upload_file:
            with open('uploaded_file.csv', 'wb+') as destination:
                for chunk in upload_file.chunks():
                    destination.write(chunk)
        print(username)
        print(data_count)
        print(add_to_database)

        # Trả về một phản hồi cho người dùng
    return render(request, 'upload_file.html')



# Create your views here.
def home (request):
    return render(request, "index.html")