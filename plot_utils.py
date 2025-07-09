from typing import Literal
import plotly.graph_objects as go
from time import sleep


def ieee_figure(fig: go.Figure, columns: Literal["single", "double"]):
    single = 252
    double = 516
    match columns:
        case "single":
            width = single
        case "double":
            width = double
        case _:
            width = double

    fig.update_xaxes(
        showgrid=True,
        # gridwidth=1,
        gridcolor="lightgray",
        minor=dict(showgrid=True),
        mirror=True,
        ticks="outside",
        showline=True,
        linecolor="black",
        title_standoff=5,
    )
    fig.update_yaxes(
        showgrid=True,
        # gridwidth=1,
        gridcolor="lightgray",
        minor=dict(showgrid=True),
        mirror=True,
        ticks="outside",
        showline=True,
        linecolor="black",
        title_standoff=0,
    )
    # fig.update_layout(legend=dict(y=1.1, x=0.5, xanchor="center"))
    fig.update_layout(
        # 3.5in or 88.9mm or 21 picas or 252pts for single column and 7.16in or 182mm or 43 picas or 516pts for double
        font_family="Times New Roman",
        font_size=6,
        margin=dict(l=0, r=0, b=0, t=0),
    )
    height = width
    fig.update_layout(template="plotly_white", width=width, height=height)
    return fig


def write_pdf(fig, name, width=None, height=None):
    fig.write_image(name, width=width, height=height)
    sleep(1)
    fig.write_image(name, width=width, height=height)

