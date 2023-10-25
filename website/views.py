from django.shortcuts import render
from .models import example, example_run
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from scipy.spatial import ConvexHull
import plotly.graph_objs as go
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)  # Sử dụng Pandas để đọc file CSV
            # Xử lý dữ liệu trong DataFrame 'df' ở đây
            # Ví dụ: In 5 hàng đầu tiên của dữ liệu
            # print(df.head(5))
            x_list, y_list = df["x"].values.astype(int), df["y"].values.astype(int)
            # x_list, y_list = [0, 0, 3, 1], [0, 2, 0, 1]
            # Chuẩn bị tập hợp điểm (x, y)
            points = [(x, y) for x, y in zip(x_list, y_list)]  # Thay x_list và y_list bằng danh sách các điểm của bạn
            # Tính Convex Hull
            hull = ConvexHull(points)
            print("----------", hull)
            
            # Lấy các điểm trên Convex Hull
            convex_hull_points = [points[i] for i in hull.vertices]
            
            # Tạo dữ liệu cho biểu đồ Plotly
            trace_points = go.Scatter(
                x=x_list,
                y=y_list,
                mode='markers',
                marker=dict(color='blue', size=8),
                name='Các điểm'
            )
            print(type([point[0] for point in convex_hull_points]))
            x = [point[0] for point in convex_hull_points]
            x.append(convex_hull_points[0][0])
            y = [point[1] for point in convex_hull_points]
            y.append(convex_hull_points[0][1])
            print("++++++++", x)
            print("++++++++", y)
            trace_convex_hull = go.Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                marker=dict(color='red', size=10),
                name='Convex Hull'
            )
            
            data = [trace_points, trace_convex_hull]
            
            layout = go.Layout(title='Convex Hull', showlegend=True)
            figure = go.Figure(data=data, layout=layout)
            
            graph = figure.to_html(full_html=False, default_height=500, default_width=700)
            
            return render(request, 'convex_hull.html', {'graph': graph})

            #return render(request, 'upload_success.html', {'uploaded_file': csv_file.name})
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

# Create your views here.
def home (request):
    
    return render(request, "index.html")

def convex_hull(x_list, y_list):
    # Chuẩn bị tập hợp điểm (x, y)
    points = [(x, y) for x, y in zip(x_list, y_list)]  # Thay x_list và y_list bằng danh sách các điểm của bạn
    
    # Tính Convex Hull
    hull = ConvexHull(points)
    
    # Lấy các điểm trên Convex Hull
    convex_hull_points = [points[i] for i in hull.vertices]
    
    # Tạo dữ liệu cho biểu đồ Plotly
    trace_points = go.Scatter(
        x=x_list,
        y=y_list,
        mode='markers',
        marker=dict(color='blue', size=8),
        name='Các điểm'
    )
    
    trace_convex_hull = go.Scatter(
        x=[point[0] for point in convex_hull_points],
        y=[point[1] for point in convex_hull_points],
        mode='lines+markers',
        marker=dict(color='red', size=10),
        name='Convex Hull'
    )
    
    data = [trace_points, trace_convex_hull]
    
    layout = go.Layout(title='Convex Hull', showlegend=True)
    figure = go.Figure(data=data, layout=layout)
    
    graph = figure.to_html(full_html=False, default_height=500, default_width=700)
    
    return render('convex_hull.html', {'graph': graph})