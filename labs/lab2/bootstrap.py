import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np
from random import sample
from sklearn.utils import resample


def boostrap(dataset, sample_size, iterations,CI):
	# <---INSERT YOUR CODE HERE--->
    stats=list()
    n_size=int(len(dataset)*sample_size)
    for i in range(iterations):
		# Sample (with replacement) from the given dataset
        sample=resample(dataset,n_samples=n_size)
        # Calculate user-defined statistic and store it
        mean=np.mean(sample)
        stats.append(mean)


	# Sort the array of per-sample statistics and cut off ends
    stats=sorted(stats)
    data_mean=np.mean(stats)
    lower=np.percentile(stats,((1-CI)/2)*100)
    upper=np.percentile(stats,(CI+((1-CI)/2))*100)
    return data_mean, lower, upper


if __name__ == "__main__":
	df = pd.read_csv('./salaries.csv')

	data = df.values.T[1]
	boots = []
	for i in range(100, 100000, 1000):
		boot = boostrap(data, data.shape[0], i,0.95)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
	#sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')


	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))



