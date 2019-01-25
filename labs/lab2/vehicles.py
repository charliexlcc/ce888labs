import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    print((df.columns))
    sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )
    sns_plot.savefig("scaterplot.png", bbox_inches='tight')

    cur_flt=df.values.T[0]
    new_flt=df.values.T[1]
    new_flt = new_flt[~np.isnan(new_flt)]#delete nan values

    print(cur_flt)
    print(new_flt)


    plt.clf()
    sns_plot_cur = sns.distplot(cur_flt, bins=20, kde=False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('current fleet')
    axes.set_ylabel('current fleet count')
    sns_plot_cur.savefig("histogram_cur.png", bbox_inches='tight')


    plt.clf()
    sns_plot_new = sns.distplot(new_flt, bins=20, kde=False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('new fleet')
    axes.set_ylabel('new fleet count')
    sns_plot_new.savefig("histogram_new.png", bbox_inches='tight')










