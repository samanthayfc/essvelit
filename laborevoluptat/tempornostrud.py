import plotly.graph_objects as go

fig = go.Figure(data=[go.Heatmap(z=[[1, 2], [3, 4]]), go.Heatmap(z=[[5, 6], [7, 8]])])
fig.update_layout(annotations=[dict(xaxis='x', yaxis='y')])
