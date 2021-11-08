import pandas as pd
import plotly_express as px
import csv

file_data = pd.read_csv('data.csv')
grouped_file_data_mean = file_data.groupby(['student_id', 'level'], as_index = False)['attempt'].mean()


scatter_plot = px.scatter(grouped_file_data_mean, x = 'student_id', y = 'level', color = 'attempt', size = 'attempt')
scatter_plot.show()