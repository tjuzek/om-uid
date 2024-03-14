# Supplementary materials for 'Signal smoothing and syntactic choices: A critical reflection on the UID hypothesis'

This repository contains materials accompanying the [Open Mind article](https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00125/120012/Signal-Smoothing-and-Syntactic-Choices-A-Critical) "Signal smoothing and syntactic choices: A critical reflection on the UID hypothesis". 



## Components

1) C-SALT-mix.tsv
2) C-SALT-mix_uid_analysed.tsv
3) x_gpt3_results.ods
4) uids_gpt3.py
5) Table - Literature Overview
6) Additional plots

---

### 1) C-SALT-mix.tsv

We decided to put the data in a corpus format and call it the Corpus of Syntactic ALTernations mix (C-SALT-mix; "mix", as this comes from both written and spoken language), which is attached as a separate file. This corpus includes nine syntactic phenomena considered alternations in the linguistic literature. The items are sourced from various licensed materials (see LICENSE.md for details). The corpus has been pre-processed for parsing, involving the removal of special characters and final punctuation. Annotations within the corpus are mostly self-explanatory.

Critically, each construction in the corpus has two types:

- Occurrences of the phenomenon, along with their hypothetical baseline counterparts.
- Reversed occurrences where real baseline examples are transformed to include the phenomenon.

For example, a real occurring cataphora sentence is "When she begins a new work, Freeman first sketches out an idea" while the constructed hypothetical counterpart is "When Freeman begins a new work, she first sketches out an idea". Similarly, a real occurrence of a sentence in canonical word order might be "And because Ben was the stronger and the faster, he always won" while the hypothetical counterpart containing a cataphora is "And because he was the stronger and the faster, Ben always won".

The naturalness of the constructed items was evaluated by a native English speaker. 



### 2) C-SALT-mix_uid_analysed.tsv

This file contains the analysis of C-SALT-mix using GPT-3.5 (text-davinci-003, as per https://platform.openai.com/docs/models/gpt-3-5) to collect surprisal values. These values were used to test the different frameworks discussed in the Open Mind paper. Please be aware that the number of tokens is according to GPT-3.5, which is typically 'no_words - 1', although there may be cases where it differs slightly. Importantly, this should not distort the analyses as it is consistent throughout all items. 

Results from GPT-2 were also included and come out similarly. 



### 3) x_gpt3_results.ods

This is a spreadsheet containing the overall scores of the analyses. 



### 4) uids_gpt3.py

This is the rapid development script used to do the analyses for the items. Note that surprisal values slightly fluctuate between executions. 



---

### 5) Table - Literature Overview

In response to a reviewer's suggestion, a table summarising the literature and different papers' perspectives on the UID hypothesis has been included, as part of this readme. It aims to provide an overview of what various papers have to say about UID. While creating a fair and comprehensive overview is challenging, this table can be adjusted if needed, as it is part of this repository and not a static element in a published paper.

| Category        | Literature           | 
| ------------- |:-------------:| 
| **Positive results <br /> (in&#160;supoprt&#160;of&#160;UID)**      | Jaeger 2006; &ensp; Levy and Jaeger 2007; &ensp; Jaeger 2010; &ensp; Jaeger 2011; &ensp; Demberg et al. 2012; &ensp; Kurumada and Jaeger 2013; &ensp; Temperley and Gildea 2015; &ensp; Kurumada and Jaeger 2015 | 
| **Mixed results**                                                   |  Horch and Reich 2016; &ensp; Yu et al. 2016 | 
| **Inconclusive results**                                            | Juzek and Bizzoni 2021 | 
| **Negative results**                                                | Jain et al. 2018; &ensp; Ranjan et al. 2020; &ensp; Zhan and Levy 2018 | 



### 6) Additional plots

The plot in the paper is rather dense, so this repository includes additional plots for further clarification. 

<br />

This is Figure 3 from the paper with **colour coding** (taken from https://davidmathlogic.com/colorblind): 

![fig3colour](https://github.com/arizus/uid/blob/main/alternationsresults3_colour.png?raw=true)

<br />

Here, constructions highlighted for which the data comes from **exclusively spoken** corpora: 

![fig3spoken](https://github.com/arizus/uid/blob/main/alternationsresults3_spoken.png?raw=true)

<br />

In the following plot, surprisal values were extracted using **GPT-2**. While the F1-Scores exhibit slight variation, the UID variants continue to face challenges and are surpassed by the Low-IC hypothesis:

![fig3spoken](https://github.com/arizus/uid/blob/main/alternationsresults_gpt2.png?raw=true)

---



## License

The license under which the materials in this repository fall is yet to be determined. Please see the LICENSE.md file for more information. 



## Contact

See [https://modlang.fsu.edu/person/tom-juzek](https://modlang.fsu.edu/person/tom-juzek) for email. 

