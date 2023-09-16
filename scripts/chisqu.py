# rapid dev script to run chi-square tests

from datetime import datetime
import numpy as np
from scipy.stats import chisquare


def main():
  constructions = ["dobe", "that", "cata", "extr", "topi", "ddat", "seem", "slui", "toug"]
  model_labels = ["delta-uid", "mu-uid", "rtm", "low-ic"]

  delta_uid_results = np.array([[130, 125], [41, 41], [60, 40], [39, 30], [64, 54], [40, 43], [36, 33], [60, 33], [28, 39]])
  mu_uid_results = np.array([[136, 119], [49, 33], [60, 40], [35, 34], [74, 44], [38, 45], [36, 33], [47, 46], [28, 39]])
  rtm_results = np.array([[108, 147], [48, 34], [59, 41], [27, 42], [62, 56], [32, 51], [32, 37], [39, 54], [17, 50]])
  low_ic_results = np.array([[153, 102], [45, 37], [68, 32], [53, 16], [74, 44], [59, 24], [48, 21], [58, 35], [45, 22]])
  model_results = np.array([delta_uid_results, mu_uid_results, rtm_results, low_ic_results])
  random_baseline_results = np.array([[127.5, 127.5], [41, 41], [50, 50], [34.5, 34.5], [59, 59], [41.5, 41.5], [34.5, 34.5], [46.5, 46.5], [33.5, 33.5]])

  for j in range(4):
    print("\n%s" % model_labels[j])
    for i in range(9):
      do_chi_squ(model_results[j][i], random_baseline_results[i], constructions[i])


def do_chi_squ(results_model, random_baseline, construction):
  chi2, p = chisquare(f_obs=results_model, f_exp=random_baseline)
  print('%s, chi2=%.3f, p-value=%.3f' % (construction, chi2, p))


# boilerplate
if __name__ == "__main__":
  startTime = datetime.now()
  main()
  print(datetime.now() - startTime)
else:
  print("Script can only run as a stand-alone.")
