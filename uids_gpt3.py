# rapid dev script

from datetime import datetime
import surprisal
import math



def main():
  m = surprisal.OpenAIModel(model_id='text-davinci-003', openai_api_key="sk-...", openai_org="org-...")
  # text-embedding-ada-002
  input_file = open(".../input.txt", "r", encoding="utf8")
  output_file = open(".../x_scripts/output.txt", "w", encoding="utf8")
  output_file.write("delta-uid\tmu-uid\trtm\tlow-ic\n")

  mean_surprisal_global = -4.702743

  c = 0
  
  for line in input_file:
    c += 1
    print(c)
    line = line.strip()

    logprobs = []
    for sentence in m.surprise([line]):
      logprob = []
      for prob in sentence:
        if not math.isnan(prob[1]):
          logprob.append(-prob[1])
      logprobs.append(logprob)

    total_tokens = 0
    sum_of_deltas = 0.0
    regression_local = 0.0
    regression_global = 0.0
    sum_surprisal = 0.0

    last_prob = 100 # float('NaN')
    mean_surprisal_sentence = sum(logprobs[0]) / len(logprobs[0])

    #delta
    for prob in logprobs[0]:
      if last_prob != 100: #float('NaN')
        sum_of_deltas += abs(last_prob - prob)
      regression_local += abs(mean_surprisal_sentence - prob)
      regression_global += abs(mean_surprisal_global - prob)
      
      total_tokens += 1
      sum_surprisal += prob
      last_prob = prob
    
    avg_delta = round((sum_of_deltas / (total_tokens - 1)), 4)
    avg_regr_local = round((regression_local / total_tokens), 4)
    avg_regr_global = round((regression_global / total_tokens), 4)
    avg_surprisal = round((sum_surprisal / total_tokens), 4)
    avg_global_delta = round((mean_surprisal_global - avg_surprisal), 4)

    output_file.write(str(avg_delta) + "\t" + str(avg_regr_local) + "\t" + str(avg_regr_global) + "\t" + str(avg_global_delta) + "\n")
    output_file.flush()

  input_file.close()
  output_file.close()


# boilerplate
if __name__ == "__main__":
  startTime = datetime.now()
  main()
  print(datetime.now() - startTime)
else:
  print("Script can only run as a stand-alone.")
