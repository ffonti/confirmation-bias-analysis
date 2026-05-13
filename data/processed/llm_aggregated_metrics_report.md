# Aggregated Confirmation Bias Metrics Report

## 1. Overall Summary (Dataset & Model)
|                                      |   CB_SAS_mean |   CB_SAS_std |   CB_NLI_mean |   CB_NLI_std |   CB_GPT_mean |   CB_GPT_std |   CB_OVERALL_mean |   CB_OVERALL_std |
|:-------------------------------------|--------------:|-------------:|--------------:|-------------:|--------------:|-------------:|------------------:|-----------------:|
| ('3_fever', 'deepseek_r1_1.5b')      |    0.0558613  |    0.138156  |   -0.00586065 |     0.309942 |       0.31326 |     0.408161 |        0.121087   |         0.197949 |
| ('3_fever', 'gemma3')                |    0.0948843  |    0.0883789 |   -0.00706841 |     0.32684  |       0.47104 |     0.351521 |        0.186285   |         0.161138 |
| ('3_fever', 'llama3.2')              |    0.0560417  |    0.11033   |   -0.0532033  |     0.268552 |       0.35978 |     0.366279 |        0.120873   |         0.16114  |
| ('3_fever', 'mistral_nemo')          |    0.105246   |    0.118537  |   -0.00333906 |     0.351212 |       0.46588 |     0.355516 |        0.189262   |         0.191702 |
| ('4_truthfulqa', 'deepseek_r1_1.5b') |   -0.013695   |    0.144149  |   -0.0352776  |     0.245517 |       0.0662  |     0.320719 |        0.00574248 |         0.153691 |
| ('4_truthfulqa', 'gemma3')           |    0.0343939  |    0.0881676 |   -0.0176705  |     0.202287 |       0.21454 |     0.388106 |        0.0770878  |         0.152865 |
| ('4_truthfulqa', 'llama3.2')         |   -0.007667   |    0.106408  |   -0.0368682  |     0.15194  |       0.20628 |     0.36998  |        0.0539149  |         0.144963 |
| ('4_truthfulqa', 'mistral_nemo')     |   -0.00424648 |    0.123897  |   -0.031845   |     0.216859 |       0.20644 |     0.412476 |        0.0567829  |         0.167809 |
| ('5_mmlu_pro', 'deepseek_r1_1.5b')   |    0.0240131  |    0.122511  |   -0.0221293  |     0.290898 |       0.02872 |     0.360372 |        0.0102013  |         0.178545 |
| ('5_mmlu_pro', 'gemma3')             |    0.0235718  |    0.0805072 |   -0.0554763  |     0.267209 |      -0.00304 |     0.414549 |       -0.0116482  |         0.179719 |
| ('5_mmlu_pro', 'llama3.2')           |    0.028      |    0.103265  |   -0.00447263 |     0.208766 |       0.16446 |     0.403675 |        0.0626625  |         0.168938 |
| ('5_mmlu_pro', 'mistral_nemo')       |    0.0189726  |    0.0988992 |   -0.021592   |     0.236394 |      -0.02634 |     0.435827 |       -0.00965312 |         0.179941 |

## 2. Summary by Dataset
| dataset      |   CB_SAS_mean |   CB_SAS_std |   CB_NLI_mean |   CB_NLI_std |   CB_GPT_mean |   CB_GPT_std |   CB_OVERALL_mean |   CB_OVERALL_std |
|:-------------|--------------:|-------------:|--------------:|-------------:|--------------:|-------------:|------------------:|-----------------:|
| 3_fever      |    0.0780084  |     0.117306 |    -0.0173678 |     0.316023 |      0.40249  |     0.376962 |         0.154377  |         0.181756 |
| 4_truthfulqa |    0.00219635 |     0.118924 |    -0.0304153 |     0.206933 |      0.173365 |     0.379154 |         0.048382  |         0.157133 |
| 5_mmlu_pro   |    0.0236394  |     0.102364 |    -0.0259176 |     0.253215 |      0.04095  |     0.410948 |         0.0128906 |         0.179238 |

## 3. Summary by Model
| model            |   CB_SAS_mean |   CB_SAS_std |   CB_NLI_mean |   CB_NLI_std |   CB_GPT_mean |   CB_GPT_std |   CB_OVERALL_mean |   CB_OVERALL_std |
|:-----------------|--------------:|-------------:|--------------:|-------------:|--------------:|-------------:|------------------:|-----------------:|
| deepseek_r1_1.5b |     0.0220598 |    0.138116  |    -0.0210892 |     0.283477 |      0.13606  |     0.385843 |         0.0456769 |         0.185384 |
| gemma3           |     0.05095   |    0.0912729 |    -0.0267384 |     0.270893 |      0.227513 |     0.431336 |         0.0839083 |         0.183662 |
| llama3.2         |     0.0254582 |    0.109778  |    -0.0315147 |     0.215898 |      0.243507 |     0.389268 |         0.0791501 |         0.161319 |
| mistral_nemo     |     0.0399908 |    0.123547  |    -0.0189253 |     0.274697 |      0.215327 |     0.449876 |         0.0787974 |         0.19806  |

## 4. Severity Distribution (Dataset & Model)
| dataset      | model            | Severity             |   Count |   Percentage |
|:-------------|:-----------------|:---------------------|--------:|-------------:|
| 3_fever      | deepseek_r1_1.5b | High (> 0.5)         |      12 |          2.4 |
| 3_fever      | deepseek_r1_1.5b | Moderate (0.1 - 0.5) |     268 |         53.6 |
| 3_fever      | deepseek_r1_1.5b | Null/Low (<= 0.1)    |     220 |         44   |
| 3_fever      | gemma3           | High (> 0.5)         |      18 |          3.6 |
| 3_fever      | gemma3           | Moderate (0.1 - 0.5) |     338 |         67.6 |
| 3_fever      | gemma3           | Null/Low (<= 0.1)    |     144 |         28.8 |
| 3_fever      | llama3.2         | High (> 0.5)         |       4 |          0.8 |
| 3_fever      | llama3.2         | Moderate (0.1 - 0.5) |     277 |         55.4 |
| 3_fever      | llama3.2         | Null/Low (<= 0.1)    |     219 |         43.8 |
| 3_fever      | mistral_nemo     | High (> 0.5)         |      35 |          7   |
| 3_fever      | mistral_nemo     | Moderate (0.1 - 0.5) |     297 |         59.4 |
| 3_fever      | mistral_nemo     | Null/Low (<= 0.1)    |     168 |         33.6 |
| 4_truthfulqa | deepseek_r1_1.5b | High (> 0.5)         |       1 |          0.2 |
| 4_truthfulqa | deepseek_r1_1.5b | Moderate (0.1 - 0.5) |     130 |         26   |
| 4_truthfulqa | deepseek_r1_1.5b | Null/Low (<= 0.1)    |     369 |         73.8 |
| 4_truthfulqa | gemma3           | High (> 0.5)         |       1 |          0.2 |
| 4_truthfulqa | gemma3           | Moderate (0.1 - 0.5) |     219 |         43.8 |
| 4_truthfulqa | gemma3           | Null/Low (<= 0.1)    |     280 |         56   |
| 4_truthfulqa | llama3.2         | Moderate (0.1 - 0.5) |     197 |         39.4 |
| 4_truthfulqa | llama3.2         | Null/Low (<= 0.1)    |     303 |         60.6 |
| 4_truthfulqa | mistral_nemo     | High (> 0.5)         |       3 |          0.6 |
| 4_truthfulqa | mistral_nemo     | Moderate (0.1 - 0.5) |     191 |         38.2 |
| 4_truthfulqa | mistral_nemo     | Null/Low (<= 0.1)    |     306 |         61.2 |
| 5_mmlu_pro   | deepseek_r1_1.5b | High (> 0.5)         |       1 |          0.2 |
| 5_mmlu_pro   | deepseek_r1_1.5b | Moderate (0.1 - 0.5) |     154 |         30.8 |
| 5_mmlu_pro   | deepseek_r1_1.5b | Null/Low (<= 0.1)    |     345 |         69   |
| 5_mmlu_pro   | gemma3           | Moderate (0.1 - 0.5) |     120 |         24   |
| 5_mmlu_pro   | gemma3           | Null/Low (<= 0.1)    |     380 |         76   |
| 5_mmlu_pro   | llama3.2         | Moderate (0.1 - 0.5) |     209 |         41.8 |
| 5_mmlu_pro   | llama3.2         | Null/Low (<= 0.1)    |     291 |         58.2 |
| 5_mmlu_pro   | mistral_nemo     | Moderate (0.1 - 0.5) |     124 |         24.8 |
| 5_mmlu_pro   | mistral_nemo     | Null/Low (<= 0.1)    |     376 |         75.2 |

## 5. Normalized Framing Adherence Score (Dataset & Model)
| dataset      | model            | Metric   | Framing       |    Score |
|:-------------|:-----------------|:---------|:--------------|---------:|
| 3_fever      | deepseek_r1_1.5b | SAS      | Neutral       | 0.775152 |
| 3_fever      | deepseek_r1_1.5b | SAS      | Leading/Conf. | 0.793626 |
| 3_fever      | deepseek_r1_1.5b | SAS      | Contradictory | 0.765695 |
| 3_fever      | deepseek_r1_1.5b | NLI      | Neutral       | 0.479975 |
| 3_fever      | deepseek_r1_1.5b | NLI      | Leading/Conf. | 0.499734 |
| 3_fever      | deepseek_r1_1.5b | NLI      | Contradictory | 0.44027  |
| 3_fever      | deepseek_r1_1.5b | GPT      | Neutral       | 0.3637   |
| 3_fever      | deepseek_r1_1.5b | GPT      | Leading/Conf. | 0.54668  |
| 3_fever      | deepseek_r1_1.5b | GPT      | Contradictory | 0.23342  |
| 3_fever      | gemma3           | SAS      | Neutral       | 0.802957 |
| 3_fever      | gemma3           | SAS      | Leading/Conf. | 0.824699 |
| 3_fever      | gemma3           | SAS      | Contradictory | 0.777256 |
| 3_fever      | gemma3           | NLI      | Neutral       | 0.531507 |
| 3_fever      | gemma3           | NLI      | Leading/Conf. | 0.578372 |
| 3_fever      | gemma3           | NLI      | Contradictory | 0.515303 |
| 3_fever      | gemma3           | GPT      | Neutral       | 0.66922  |
| 3_fever      | gemma3           | GPT      | Leading/Conf. | 0.88772  |
| 3_fever      | gemma3           | GPT      | Contradictory | 0.41668  |
| 3_fever      | llama3.2         | SAS      | Neutral       | 0.786883 |
| 3_fever      | llama3.2         | SAS      | Leading/Conf. | 0.80335  |
| 3_fever      | llama3.2         | SAS      | Contradictory | 0.775329 |
| 3_fever      | llama3.2         | NLI      | Neutral       | 0.471416 |
| 3_fever      | llama3.2         | NLI      | Leading/Conf. | 0.497003 |
| 3_fever      | llama3.2         | NLI      | Contradictory | 0.478745 |
| 3_fever      | llama3.2         | GPT      | Neutral       | 0.61306  |
| 3_fever      | llama3.2         | GPT      | Leading/Conf. | 0.80124  |
| 3_fever      | llama3.2         | GPT      | Contradictory | 0.44146  |
| 3_fever      | mistral_nemo     | SAS      | Neutral       | 0.787442 |
| 3_fever      | mistral_nemo     | SAS      | Leading/Conf. | 0.811569 |
| 3_fever      | mistral_nemo     | SAS      | Contradictory | 0.758946 |
| 3_fever      | mistral_nemo     | NLI      | Neutral       | 0.383235 |
| 3_fever      | mistral_nemo     | NLI      | Leading/Conf. | 0.510267 |
| 3_fever      | mistral_nemo     | NLI      | Contradictory | 0.349514 |
| 3_fever      | mistral_nemo     | GPT      | Neutral       | 0.66548  |
| 3_fever      | mistral_nemo     | GPT      | Leading/Conf. | 0.93818  |
| 3_fever      | mistral_nemo     | GPT      | Contradictory | 0.4723   |
| 4_truthfulqa | deepseek_r1_1.5b | SAS      | Neutral       | 0.744198 |
| 4_truthfulqa | deepseek_r1_1.5b | SAS      | Leading/Conf. | 0.743175 |
| 4_truthfulqa | deepseek_r1_1.5b | SAS      | Contradictory | 0.750023 |
| 4_truthfulqa | deepseek_r1_1.5b | NLI      | Neutral       | 0.517786 |
| 4_truthfulqa | deepseek_r1_1.5b | NLI      | Leading/Conf. | 0.527352 |
| 4_truthfulqa | deepseek_r1_1.5b | NLI      | Contradictory | 0.537985 |
| 4_truthfulqa | deepseek_r1_1.5b | GPT      | Neutral       | 0.3227   |
| 4_truthfulqa | deepseek_r1_1.5b | GPT      | Leading/Conf. | 0.35098  |
| 4_truthfulqa | deepseek_r1_1.5b | GPT      | Contradictory | 0.28478  |
| 4_truthfulqa | gemma3           | SAS      | Neutral       | 0.759823 |
| 4_truthfulqa | gemma3           | SAS      | Leading/Conf. | 0.772948 |
| 4_truthfulqa | gemma3           | SAS      | Contradictory | 0.755751 |
| 4_truthfulqa | gemma3           | NLI      | Neutral       | 0.531856 |
| 4_truthfulqa | gemma3           | NLI      | Leading/Conf. | 0.53212  |
| 4_truthfulqa | gemma3           | NLI      | Contradictory | 0.538786 |
| 4_truthfulqa | gemma3           | GPT      | Neutral       | 0.62274  |
| 4_truthfulqa | gemma3           | GPT      | Leading/Conf. | 0.57122  |
| 4_truthfulqa | gemma3           | GPT      | Contradictory | 0.35668  |
| 4_truthfulqa | llama3.2         | SAS      | Neutral       | 0.753796 |
| 4_truthfulqa | llama3.2         | SAS      | Leading/Conf. | 0.760529 |
| 4_truthfulqa | llama3.2         | SAS      | Contradictory | 0.764362 |
| 4_truthfulqa | llama3.2         | NLI      | Neutral       | 0.508939 |
| 4_truthfulqa | llama3.2         | NLI      | Leading/Conf. | 0.514745 |
| 4_truthfulqa | llama3.2         | NLI      | Contradictory | 0.541074 |
| 4_truthfulqa | llama3.2         | GPT      | Neutral       | 0.54812  |
| 4_truthfulqa | llama3.2         | GPT      | Leading/Conf. | 0.49042  |
| 4_truthfulqa | llama3.2         | GPT      | Contradictory | 0.28414  |
| 4_truthfulqa | mistral_nemo     | SAS      | Neutral       | 0.722419 |
| 4_truthfulqa | mistral_nemo     | SAS      | Leading/Conf. | 0.724274 |
| 4_truthfulqa | mistral_nemo     | SAS      | Contradictory | 0.726397 |
| 4_truthfulqa | mistral_nemo     | NLI      | Neutral       | 0.483458 |
| 4_truthfulqa | mistral_nemo     | NLI      | Leading/Conf. | 0.500694 |
| 4_truthfulqa | mistral_nemo     | NLI      | Contradictory | 0.501003 |
| 4_truthfulqa | mistral_nemo     | GPT      | Neutral       | 0.59792  |
| 4_truthfulqa | mistral_nemo     | GPT      | Leading/Conf. | 0.5673   |
| 4_truthfulqa | mistral_nemo     | GPT      | Contradictory | 0.36086  |
| 5_mmlu_pro   | deepseek_r1_1.5b | SAS      | Neutral       | 0.763024 |
| 5_mmlu_pro   | deepseek_r1_1.5b | SAS      | Leading/Conf. | 0.786093 |
| 5_mmlu_pro   | deepseek_r1_1.5b | SAS      | Contradictory | 0.774086 |
| 5_mmlu_pro   | deepseek_r1_1.5b | NLI      | Neutral       | 0.521459 |
| 5_mmlu_pro   | deepseek_r1_1.5b | NLI      | Leading/Conf. | 0.595693 |
| 5_mmlu_pro   | deepseek_r1_1.5b | NLI      | Contradictory | 0.567427 |
| 5_mmlu_pro   | deepseek_r1_1.5b | GPT      | Neutral       | 0.53324  |
| 5_mmlu_pro   | deepseek_r1_1.5b | GPT      | Leading/Conf. | 0.4937   |
| 5_mmlu_pro   | deepseek_r1_1.5b | GPT      | Contradictory | 0.46498  |
| 5_mmlu_pro   | gemma3           | SAS      | Neutral       | 0.789979 |
| 5_mmlu_pro   | gemma3           | SAS      | Leading/Conf. | 0.786142 |
| 5_mmlu_pro   | gemma3           | SAS      | Contradictory | 0.774356 |
| 5_mmlu_pro   | gemma3           | NLI      | Neutral       | 0.553784 |
| 5_mmlu_pro   | gemma3           | NLI      | Leading/Conf. | 0.547402 |
| 5_mmlu_pro   | gemma3           | NLI      | Contradictory | 0.525804 |
| 5_mmlu_pro   | gemma3           | GPT      | Neutral       | 0.75238  |
| 5_mmlu_pro   | gemma3           | GPT      | Leading/Conf. | 0.58886  |
| 5_mmlu_pro   | gemma3           | GPT      | Contradictory | 0.5919   |
| 5_mmlu_pro   | llama3.2         | SAS      | Neutral       | 0.78209  |
| 5_mmlu_pro   | llama3.2         | SAS      | Leading/Conf. | 0.789088 |
| 5_mmlu_pro   | llama3.2         | SAS      | Contradictory | 0.775088 |
| 5_mmlu_pro   | llama3.2         | NLI      | Neutral       | 0.56656  |
| 5_mmlu_pro   | llama3.2         | NLI      | Leading/Conf. | 0.537079 |
| 5_mmlu_pro   | llama3.2         | NLI      | Contradictory | 0.531368 |
| 5_mmlu_pro   | llama3.2         | GPT      | Neutral       | 0.6617   |
| 5_mmlu_pro   | llama3.2         | GPT      | Leading/Conf. | 0.57468  |
| 5_mmlu_pro   | llama3.2         | GPT      | Contradictory | 0.41022  |
| 5_mmlu_pro   | mistral_nemo     | SAS      | Neutral       | 0.776757 |
| 5_mmlu_pro   | mistral_nemo     | SAS      | Leading/Conf. | 0.76524  |
| 5_mmlu_pro   | mistral_nemo     | SAS      | Contradictory | 0.755753 |
| 5_mmlu_pro   | mistral_nemo     | NLI      | Neutral       | 0.555592 |
| 5_mmlu_pro   | mistral_nemo     | NLI      | Leading/Conf. | 0.506892 |
| 5_mmlu_pro   | mistral_nemo     | NLI      | Contradictory | 0.495002 |
| 5_mmlu_pro   | mistral_nemo     | GPT      | Neutral       | 0.7494   |
| 5_mmlu_pro   | mistral_nemo     | GPT      | Leading/Conf. | 0.60872  |
| 5_mmlu_pro   | mistral_nemo     | GPT      | Contradictory | 0.63506  |
