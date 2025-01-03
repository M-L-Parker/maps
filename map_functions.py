

import numpy as np
import plotly.graph_objects as go
from datetime import datetime


def make_map(current_distance):

    # Define the globe layout
    fig = go.Figure()

    # Add the globe surface
    fig.add_trace(go.Scattergeo(
        lon=[],  # Empty to show the base globe initially
        lat=[],
        mode='markers',
        marker=dict(size=0.1),
        geo='geo',
    ))

    # derive the current target fraction
    start_date = datetime(2022, 1, 7)
    end_date = datetime(2029, 11, 4)
    current_date = datetime.now()
    total_duration = end_date - start_date
    elapsed_duration = current_date - start_date
    fraction_of_time = elapsed_duration / total_duration


    # Add the travelled arc to the globe
    total_distance=40075.017
    fraction=current_distance/total_distance

    num_points = 500
    longitudes = np.linspace(0, 360*fraction, num_points)
    latitudes = np.zeros(num_points)  # Equator

    fig.add_trace(go.Scattergeo(
        lon=longitudes,
        lat=latitudes,
        mode='lines',
        line=dict(width=2, color='green'),
    ))

    # Add a starting line
    fig.add_trace(go.Scattergeo(
        lon=[0, 0],
        lat=[-3, 3],
        mode='lines',
        line=dict(width=2, color='green'),
    ))

    # add a dot to mark current position
    fig.add_trace(go.Scattergeo(
        lon=[360*fraction],
        lat=[0],
        mode='markers',
        marker=dict(size=10, color='green', line=dict(width=2, color='black')),
    ))

    # add a dot to mark current target position
    fig.add_trace(go.Scattergeo(
        lon=[360*fraction_of_time],
        lat=[0],
        mode='markers',
        marker=dict(size=10, color='yellow', line=dict(width=2, color='black')),
    ))

    # Update layout to make the figure larger
    fig.update_layout(
        width=1000,
        height=1000
    )

    # Globe settings
    fig.update_geos(
        projection_type="orthographic",
        showcountries=True,
        showcoastlines=True,
        showland=True,
        landcolor="lightgreen",
        oceancolor="lightblue",
        lakecolor="lightblue",
        showocean=True,
    )

    fig.update_layout(showlegend=False)

    return fig