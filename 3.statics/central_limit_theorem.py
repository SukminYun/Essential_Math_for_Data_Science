import random
import plotly.graph_objects as go

sample_size = 31
sample_count = 1000

# random values between 0.0 to 1.0
x_values = [(sum([random.uniform(0.0,1.0) for i in range(sample_size)])/sample_size) 
            for _ in range(sample_count)]

fig = go.Figure(data=[go.Histogram(x=x_values, nbinsx=20)])
fig.show()