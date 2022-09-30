import json
import matplotlib.pyplot as plt
import pandas
import pandas as pd
import numpy as np
import matplotlib
from spectral import *
import sources as s
import openpyxl


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
        # norm_x = x - min(x[168:-2])
        # Магическая константа 168 для того, чтобы график строился в последних 100нм.
        p = plt.plot(xvals[168:-2], x[168:-2])
    plt.grid(1)
    return p


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


def create_df(pts, classTag):
    df = pd.DataFrame.from_dict(pts)
    df.drop(columns=['type', 'probability', 'locked', 'visible', 'attributes', 'groupId', 'pointLabels'],
            axis=1, inplace=True)
    df.loc[df.x > 0, 'x'] = df.x.astype(int)
    df.loc[df.y > 0, 'y'] = df.y.astype(int)
    df.loc[df.classId == 1, 'classId'] = classTag
    return df


def get_xvals_and_vals(view, x, y):
    xvals = view.source.bands.centers
    data = view.source[x, y]
    data = data[np.newaxis, :]
    data = data.reshape(-1, data.shape[-1])
    return xvals, data[0][168:-1]


def add_ref_value_to_df(plastic_name):
    with open('JSONs/{}.json'.format(plastic_name), 'r') as handle:
        parsed = json.load(handle)
        points = parsed['instances']
        df = create_df(points, plastic_name)
        img = s.plastic_name_to_image[plastic_name]
        view = imshow(img)
        # df.insert(3, 'xvalue', [[] for i in range(len(df)])
        df.insert(3, 'ref_values', [[] for i in range(len(df))])
        for i, row, in df.iterrows():
            xv, rv = get_xvals_and_vals(view, row[1], row[2])
            # df.at[i, 'xvalue'] = xv
            # new_df = pd.DataFrame(rv)
            # df = pd.concat([df, new_df], sort=False, axis=1)
            df.at[i, 'ref_values'] = rv
        print(df)
        return df


matplotlib.use('TkAgg')
img = s.HDPE
view = imshow(img)


df_1 = add_ref_value_to_df('LDPE')
df_2 = add_ref_value_to_df('PVC')
df_3 = add_ref_value_to_df('HDPE')
df_4 = add_ref_value_to_df('PS')
df_5 = add_ref_value_to_df('PP')
df_6 = add_ref_value_to_df('PET')


df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6], sort=False, axis=0)
df.reset_index(inplace=True)
df.drop(columns=['index'], axis=1, inplace=True)
print(df.shape)

df.to_excel('C:/result2.xlsx')

# matplotlib.pyplot.show(block=True)

