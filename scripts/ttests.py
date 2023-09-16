# rapid dev script to run ttests on the f1scores of the different models

from datetime import datetime
import statistics
import scipy.stats


def main():
  perfectly_random_f1scores = [0.4921, 0.4938, 0.5, 0.507, 0.4957, 0.5625, 0.5205, 0.5053, 0.5641]
  delta_uid = [0.6398, 0.3492, 0.5918, 0.5714, 0.5345, 0.5275, 0.5075, 0.5926, 0.48]
  mu_uid = [0.6361, 0.459, 0.6296, 0.5143, 0.5172, 0.5263, 0.3774, 0.4524, 0.5618]
  rtm = [0.4, 0.5143, 0.6555, 0.4, 0.5556, 0.427, 0.3019, 0.4808, 0.2424]
  low_ic = [0.6964, 0.3273, 0.5897, 0.75, 0.5926, 0.7447, 0.7342, 0.507, 0.8]

  print("means")
  print(round(statistics.mean(perfectly_random_f1scores), 3))
  print(round(statistics.mean(delta_uid), 3))
  print(round(statistics.mean(mu_uid), 3))
  print(round(statistics.mean(rtm), 3))
  print(round(statistics.mean(low_ic), 3))

  print("\nstdevs")
  print(round(statistics.stdev(perfectly_random_f1scores), 3))
  print(round(statistics.stdev(delta_uid), 3))
  print(round(statistics.stdev(mu_uid), 3))
  print(round(statistics.stdev(rtm), 3))
  print(round(statistics.stdev(low_ic), 3))

  print("\nttests")
  t_statistic, p_value = scipy.stats.ttest_rel(delta_uid, perfectly_random_f1scores, alternative="greater")
  print(str(round(t_statistic, 3)) + ", " + str(round(p_value, 3)))
  t_statistic, p_value = scipy.stats.ttest_rel(mu_uid, perfectly_random_f1scores, alternative="greater")
  print(str(round(t_statistic, 3)) + ", " + str(round(p_value, 3)))
  t_statistic, p_value = scipy.stats.ttest_rel(rtm, perfectly_random_f1scores, alternative="greater")
  print(str(round(t_statistic, 3)) + ", " + str(round(p_value, 3)))
  t_statistic, p_value = scipy.stats.ttest_rel(low_ic, perfectly_random_f1scores, alternative="greater")
  print(str(round(t_statistic, 3)) + ", " + str(round(p_value, 3)))


# boilerplate
if __name__ == "__main__":
  startTime = datetime.now()
  main()
  print(datetime.now() - startTime)
else:
  print("Script can only run as a stand-alone.")
