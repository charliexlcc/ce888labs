from numpy import array
from matplotlib import pyplot
from statsmodels.stats.power import TTestIndPower

def power(sample1, sample2, reps, size, alpha):
   for i in range(reps):
      sample_a=sample1[i,:]
      effect_sizes=array(range(size))
      analysis=TTestIndPower()
      analysis.plot_power(dep_var='nobs',nobs=sample_a,effect_sizes=effect_sizes)
      pyplot.show()

      sample_b=sample2[i,:]
      analysis.plot_power(dep_var='nobs', nobs=sample_b, effect_sizes=effect_sizes)
      pyplot.show()


