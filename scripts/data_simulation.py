# rapid dev script to simulate and plot data

from datetime import datetime
import random
import matplotlib.pyplot as plt
import numpy as np


def main():
  output_file = open("/home/.../datasimulationresults.txt", "w")
  construction_actual = [124, 41, 50, 37, 58, 55, 38, 49, 45]
  canonical_actual = [132, 41, 50, 32, 60, 28, 31, 44, 22]
  constructions = ["do-be to", "that drop", "cataphora", "extra-position", "topicalisation", "2NP-dative", "seems-raising", "sluicing", "tough-raising"]
  list_of_lists_of_f1s = []

  for c in range(0, len(construction_actual)):
    list_of_f1s = []
    for _ in range(1000):
      model_true_positives = random_construction_choice(construction_actual[c])
      model_true_negatives = random_construction_choice(canonical_actual[c])
      model_false_negatives = construction_actual[c] - model_true_positives
      model_false_positives = canonical_actual[c] - model_true_negatives


      precision = model_true_positives / (model_true_positives + model_false_positives)
      recall = model_true_positives / (model_true_positives + model_false_negatives)
      f1 = 2 * ((precision * recall) / (precision + recall))
      list_of_f1s.append(f1)
    
    output_file.write(constructions[c] + "\n")
    q1 = round(np.percentile(list_of_f1s, 25), 3)
    q2 = round(np.percentile(list_of_f1s, 50), 3)
    q3 = round(np.percentile(list_of_f1s, 75), 3)

    output_file.write("Q1 (25th percentile):" + str(q1) + "\n")
    output_file.write("Q2 (50th percentile):" + str(q2) + "\n")
    output_file.write("Q3 (75th percentile):" + str(q3) + "\n\n")

    list_of_lists_of_f1s.append(list_of_f1s)


  fig = plt.figure(1, figsize=(12, 4))


  # Create an axes instance
  ax = fig.add_subplot(111)
  plt.axhline(y = 0.5, color = '#424242', linestyle = '--')
  ax.set_title('Distribution of F1-Scores for Random Model\n(Simulated N=1000 per construction)', fontsize=13)

  # Create the boxplot
  bp = ax.boxplot([list_of_lists_of_f1s[0], list_of_lists_of_f1s[1], list_of_lists_of_f1s[2], list_of_lists_of_f1s[3], list_of_lists_of_f1s[4], list_of_lists_of_f1s[5], list_of_lists_of_f1s[6], list_of_lists_of_f1s[7], list_of_lists_of_f1s[8]], patch_artist=True)

  colours = ['#000000', '#303030', '#cdcdcd', '#e0e0e0', '#f9f9f9', '#424242', '#626262', '#888888', '#adadad']
  colours_meds = ['#d2d2d2', '#d2d2d2', '#2d2d2d', '#2d2d2d', '#2d2d2d', '#d2d2d2', '#d2d2d2', '#d2d2d2', '#d2d2d2']

  for i in range(0, len(bp['boxes'])):
    bp['boxes'][i].set(color=colours[i])
    bp['boxes'][i].set(facecolor=colours[i])

  # Customize the boxplot
  #for box in bp['boxes']:
      #box.set(color='#7570b3', linewidth=2)
      #box.set(facecolor='#1b9e77')

  for whisker in bp['whiskers']:
      whisker.set(color='#949494', linewidth=2)

  for cap in bp['caps']:
      cap.set(color='#949494', linewidth=2)

  for i in range(0, len(bp['medians'])):
    bp['medians'][i].set(color=colours_meds[i], linewidth=2)
  
  for flier in bp['fliers']:
      flier.set(marker='o', color='#e7298a', alpha=0.5)

  # Set the tick labels
  
  ax.set_xticklabels(['do-be to', 'that drop', 'cataphora', 'extra-\nposition', 'topica-\nlisation', '2NP-\ndative', 'seems-\nraising', 'sluicing', 'tough-\nraising'])

  ax.set_ylim(0, 1)

  ax.set_yticks(np.arange(0, 1.1, 0.1))
  # Set y-axis label
  ax.set_ylabel('F1-Scores', fontsize=12)

  plt.savefig('/home/.../datasimulationresults.png', bbox_inches='tight', dpi = 200)

  output_file.close()


def random_construction_choice(times):
    results = [random.randint(0, 1) for _ in range(times)]
    count_heads = results.count(1)
    return count_heads

  




# boilerplate
if __name__ == "__main__":
  startTime = datetime.now()
  main()
  print(datetime.now() - startTime)
else:
  print("Script can only run as a stand-alone.")
