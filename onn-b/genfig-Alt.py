import json
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd
from dateutil import parser

arr = json.load(open("ONN-Alt-B-30dW-30dR_2020-12-01_2022-07-01.json"))

fig = plt.figure()

mono_font = {'fontname':'monospace'}


def buildbarchart(i=int):
    print(i)
    pt = arr[i]
    constituentNames = []
    constituentWeights = []
    plt.clf()
    constituentsDF = pd.read_json(json.dumps(pt['indexConstituents']), orient='split')
    for (_, row) in constituentsDF.iterrows():
        constituentNames.append(row['geckoId'])
        constituentWeights.append(row['weight'])
    dt = pt['isoInstant'][:10]
    indexval = pt['indexValue']
    df = pd.DataFrame({'assets':constituentNames, 'weights':constituentWeights})
    df.sort_values('weights', inplace=True)
    ax = plt.axes()
    ax.set_xlim((0.0, 1.0))
    hbars = ax.barh(df['assets'].tolist(), df['weights'].tolist(), align='center')
    ax.bar_label(hbars, fmt='%.3f')
    plt.subplots_adjust(left=0.20)
    plt.title(f"Date: {dt}, Index: {indexval:.2f}", **mono_font)
    #plt.show()

animator = ani.FuncAnimation(fig, buildbarchart, frames=len(arr))

animator.save(r'ONN-Alt-B.gif')
animator.save(r'ONN-Alt-B.mp4', writer=ani.FFMpegWriter(fps=10))

# References
# https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe
