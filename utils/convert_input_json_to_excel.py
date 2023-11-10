import pandas as pd
import json

# Đọc dữ liệu từ file JSON
with open('data.json') as f:
    data = json.load(f)
    
parameter, location, vehicle, demand, time_matrix = data['parameter'], data['location'], data['vehicle'], data['demand'], data['time_matrix']
location_df, vehicle_df, demand_df, time_matrix_df = pd.DataFrame(location), pd.DataFrame(vehicle), pd.DataFrame(demand), pd.DataFrame(time_matrix)

location_df.rename(columns={0: 'point_id', 1: 'point_type_id', 2: 'latitude', 3: 'longitude'}, inplace=True)
vehicle_df.rename(columns={0: 'vehicle_id', 1: 'registeredtonnage', 2: 'convertedtonnage', 3: 'cbm', 4: 'point_belong_id', 5: 'unloading_time_point_end', 6: 'loading_time_point_depart', 7: 'unloading_time_point', 8: 'cost_fixed', 9: 'cost_unloading_point', 10: 'cost_loading_point'}, inplace=True)
demand_df.rename(columns={0: 'item_id', 1: 'point_from', 2: 'point_to', 3: 'item_weight', 4: 'item_volume', 5: 'item_qty'}, inplace=True)
time_matrix_df.rename(columns={0: 'point_from_id', 1: 'point_to_id', 2: 'distance', 3: 'travel_time'}, inplace=True)

# Ghi vào một file Excel với mỗi DataFrame là một sheet
with pd.ExcelWriter('input_1D.xlsx') as writer:
    location_df.to_excel(writer, sheet_name='location', index=False)
    vehicle_df.to_excel(writer, sheet_name='vehicle', index=False)
    demand_df.to_excel(writer, sheet_name='demand', index=False)
    time_matrix_df.to_excel(writer, sheet_name='time_matrix', index=False)
