from random import randint
from spectral import *
import matplotlib.pyplot as plt
import numpy as np
import datasets as d
import sources as s
import matplotlib
import superannotate


def rand_pixel(coords: list) -> (int, int):
    r_x = randint(coords[0], coords[1])
    r_y = randint(coords[2], coords[3])
    return r_x, r_y


# def draw_n_random_plots(n, view):
#     for i in range(n):
#         x, y = rand_pixel([1, 300, 1, 300])
#         print_spplot_of_pixel(view, x, y)


def draw_all_plots_in_current_set(data, view):
    for i in range(len(data)):
        x, y = rand_pixel(data[i])
        print_spplot_of_pixel(view, x, y)


def print_spplot_of_pixel(view, x, y):
    (r, c) = (int(x + 0.5), int(y + 0.5))
    if view.spectrum_plot_fig_id is None:
        f = plt.figure()
        view.spectrum_plot_fig_id = f.number
    try:
        f = plt.figure(view.spectrum_plot_fig_id)
    except:
        f = plt.figure()
        view.spectrum_plot_fig_id = f.number
    s = f.gca()
    plot_last_100nm(view.source[r, c], view.source)
    s.xaxis.axes.relim()
    s.xaxis.axes.autoscale(True)
    plt.show()
    # f.show()
    # f.canvas.draw()
    # print(view.source[r, c].ndim)


def plot_last_100nm(data, source=None):
    if source is not None and hasattr(source, 'bands') and source.bands.centers is not None:
        xvals = source.bands.centers
    if data.ndim == 1:
        data = data[np.newaxis, :]
    data = data.reshape(-1, data.shape[-1])
    if source is not None and hasattr(source, 'metadata') and 'bbl' in source.metadata:
        data = np.array(data)
        data[:, np.array(source.metadata['bbl']) == 0] = None
    for x in data:
        # Магическая константа 168 для того, чтобы график строился в последних 100нм.
        p = plt.plot(xvals[168:], x[168:])
    plt.grid(1)
    return p


# Вместо HDPE можно вписать любой из шести типов пластика и получить график нескольких точек из датасета.
# Точки будут выбраны случайным образом из квадрата, взятого из датасета, функцией rand_pixel().
matplotlib.use('TkAgg')
img = s.HDPE
view = imshow(img)
#draw_all_plots_in_current_set(d.HDPE_rects, view)
matplotlib.pyplot.show(block=True)
















