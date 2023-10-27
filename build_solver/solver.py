import pandas as pd
from scipy.spatial import ConvexHull
import plotly.graph_objs as go
from plotly.offline import plot
import sys

def solver(input_path, output_path):
    df = pd.read_csv(input_path)  # Sử dụng Pandas để đọc file CSV
    # Xử lý dữ liệu trong DataFrame 'df' ở đây
    x_list, y_list = df["x"].values.astype(int), df["y"].values.astype(int)
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
    x = [point[0] for point in convex_hull_points]
    x.append(convex_hull_points[0][0])
    y = [point[1] for point in convex_hull_points]
    y.append(convex_hull_points[0][1])
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

    # graph = figure.to_html(full_html=False, default_height=500, default_width=700)
    # graph.write_html("ouput.html")
    plot(figure, filename=output_path, auto_open=False)
    return
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Sử dụng: your_task.py <input_file> <output_file>")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    solver(input_path, output_path)