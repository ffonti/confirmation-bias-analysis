# Aggregated Confirmation Bias Metrics Report

## 1. Overall Summary (Dataset & Model)
|                                      |   CB_SAS_mean |   CB_SAS_std |   CB_NLI_mean |   CB_NLI_std |   CB_GPT_mean |   CB_GPT_std |   CB_OVERALL_mean |   CB_OVERALL_std |
|:-------------------------------------|--------------:|-------------:|--------------:|-------------:|--------------:|-------------:|------------------:|-----------------:|
| ('3_fever', 'deepseek_r1_1.5b')      |    0.0558613  |    0.138156  |   -0.00586065 |     0.309942 |      0.31326  |     0.408161 |        0.121087   |         0.197949 |
| ('3_fever', 'gemma3')                |    0.0948843  |    0.0883789 |   -0.00706841 |     0.32684  |      0.47104  |     0.351521 |        0.186285   |         0.161138 |
| ('3_fever', 'gpt_4o')                |    0.0246588  |    0.0743162 |   -0.00554307 |     0.254913 |      0.14486  |     0.264209 |        0.0546586  |         0.119186 |
| ('3_fever', 'llama3.2')              |    0.0560417  |    0.11033   |   -0.0532033  |     0.268552 |      0.35978  |     0.366279 |        0.120873   |         0.16114  |
| ('3_fever', 'mistral_nemo')          |    0.105246   |    0.118537  |   -0.00333906 |     0.351212 |      0.46588  |     0.355516 |        0.189262   |         0.191702 |
| ('3_fever', 'phi4')                  |    0.0247478  |    0.092359  |    0.0215205  |     0.291578 |      0.2303   |     0.363816 |        0.0921894  |         0.1676   |
| ('3_fever', 'qwen2.5')               |    0.0913242  |    0.100879  |    0.0836002  |     0.333867 |      0.40842  |     0.385198 |        0.194448   |         0.196995 |
| ('4_truthfulqa', 'deepseek_r1_1.5b') |   -0.013695   |    0.144149  |   -0.0352776  |     0.245517 |      0.0662   |     0.320719 |        0.00574248 |         0.153691 |
| ('4_truthfulqa', 'gemma3')           |    0.0343939  |    0.0881676 |   -0.0176705  |     0.202287 |      0.21454  |     0.388106 |        0.0770878  |         0.152865 |
| ('4_truthfulqa', 'gpt_4o')           |    0.0195332  |    0.0900179 |   -0.0313281  |     0.19752  |      0.218266 |     0.383928 |        0.0688237  |         0.149423 |
| ('4_truthfulqa', 'llama3.2')         |   -0.007667   |    0.106408  |   -0.0368682  |     0.15194  |      0.20628  |     0.36998  |        0.0539149  |         0.144963 |
| ('4_truthfulqa', 'mistral_nemo')     |   -0.00424648 |    0.123897  |   -0.031845   |     0.216859 |      0.20644  |     0.412476 |        0.0567829  |         0.167809 |
| ('4_truthfulqa', 'phi4')             |    0.0230631  |    0.0897646 |   -0.0200346  |     0.178177 |      0.1729   |     0.381584 |        0.0586428  |         0.140321 |
| ('4_truthfulqa', 'qwen2.5')          |   -0.00496025 |    0.10896   |   -0.0233552  |     0.200406 |      0.13104  |     0.364422 |        0.0342415  |         0.147222 |
| ('5_mmlu_pro', 'deepseek_r1_1.5b')   |    0.0240131  |    0.122511  |   -0.0221293  |     0.290898 |      0.02872  |     0.360372 |        0.0102013  |         0.178545 |
| ('5_mmlu_pro', 'gemma3')             |    0.0235718  |    0.0805072 |   -0.0554763  |     0.267209 |     -0.00304  |     0.414549 |       -0.0116482  |         0.179719 |
| ('5_mmlu_pro', 'gpt_4o')             |    0.00940367 |    0.0741472 |   -0.00915043 |     0.22483  |      0.1133   |     0.431688 |        0.0378511  |         0.171175 |
| ('5_mmlu_pro', 'llama3.2')           |    0.028      |    0.103265  |   -0.00447263 |     0.208766 |      0.16446  |     0.403675 |        0.0626625  |         0.168938 |
| ('5_mmlu_pro', 'mistral_nemo')       |    0.0189726  |    0.0988992 |   -0.021592   |     0.236394 |     -0.02634  |     0.435827 |       -0.00965312 |         0.179941 |
| ('5_mmlu_pro', 'phi4')               |    0.00854998 |    0.0741303 |   -0.00782033 |     0.217401 |     -0.0058   |     0.365755 |       -0.00169012 |         0.151673 |
| ('5_mmlu_pro', 'qwen2.5')            |    0.0361982  |    0.0865412 |    0.00451356 |     0.242766 |      0.13636  |     0.443456 |        0.0590239  |         0.185651 |

## 2. Summary by Dataset
| dataset      |   CB_SAS_mean |   CB_SAS_std |   CB_NLI_mean |   CB_NLI_std |   CB_GPT_mean |   CB_GPT_std |   CB_OVERALL_mean |   CB_OVERALL_std |
|:-------------|--------------:|-------------:|--------------:|-------------:|--------------:|-------------:|------------------:|-----------------:|
| 3_fever      |    0.0646806  |    0.109438  |    0.00430089 |     0.309141 |     0.341934  |     0.37581  |         0.136972  |         0.179832 |
| 4_truthfulqa |    0.00663163 |    0.11032   |   -0.0280542  |     0.200749 |     0.173667  |     0.378681 |         0.050748  |         0.1526   |
| 5_mmlu_pro   |    0.0212442  |    0.0932761 |   -0.0165896  |     0.24314  |     0.0582371 |     0.415022 |         0.0209639 |         0.176315 |

## 3. Summary by Model
| model            |   CB_SAS_mean |   CB_SAS_std |   CB_NLI_mean |   CB_NLI_std |   CB_GPT_mean |   CB_GPT_std |   CB_OVERALL_mean |   CB_OVERALL_std |
|:-----------------|--------------:|-------------:|--------------:|-------------:|--------------:|-------------:|------------------:|-----------------:|
| deepseek_r1_1.5b |     0.0220598 |    0.138116  |   -0.0210892  |     0.283477 |      0.13606  |     0.385843 |         0.0456769 |         0.185384 |
| gemma3           |     0.05095   |    0.0912729 |   -0.0267384  |     0.270893 |      0.227513 |     0.431336 |         0.0839083 |         0.183662 |
| gpt_4o           |     0.0178652 |    0.0800396 |   -0.0153405  |     0.227103 |      0.158809 |     0.369156 |         0.0537778 |         0.148579 |
| llama3.2         |     0.0254582 |    0.109778  |   -0.0315147  |     0.215898 |      0.243507 |     0.389268 |         0.0791501 |         0.161319 |
| mistral_nemo     |     0.0399908 |    0.123547  |   -0.0189253  |     0.274697 |      0.215327 |     0.449876 |         0.0787974 |         0.19806  |
| phi4             |     0.0187869 |    0.0860473 |   -0.00211147 |     0.234323 |      0.132467 |     0.38364  |         0.049714  |         0.158345 |
| qwen2.5          |     0.0408541 |    0.106724  |    0.0215862  |     0.268605 |      0.225273 |     0.419348 |         0.0959045 |         0.191228 |

## 4. Severity Distribution (Dataset & Model)
| dataset      | model            | Severity             |   Count |   Percentage |
|:-------------|:-----------------|:---------------------|--------:|-------------:|
| 3_fever      | deepseek_r1_1.5b | High (> 0.5)         |      12 |          2.4 |
| 3_fever      | deepseek_r1_1.5b | Moderate (0.1 - 0.5) |     268 |         53.6 |
| 3_fever      | deepseek_r1_1.5b | Null/Low (<= 0.1)    |     220 |         44   |
| 3_fever      | gemma3           | High (> 0.5)         |      18 |          3.6 |
| 3_fever      | gemma3           | Moderate (0.1 - 0.5) |     338 |         67.6 |
| 3_fever      | gemma3           | Null/Low (<= 0.1)    |     144 |         28.8 |
| 3_fever      | gpt_4o           | High (> 0.5)         |       2 |          0.4 |
| 3_fever      | gpt_4o           | Moderate (0.1 - 0.5) |     152 |         30.4 |
| 3_fever      | gpt_4o           | Null/Low (<= 0.1)    |     346 |         69.2 |
| 3_fever      | llama3.2         | High (> 0.5)         |       4 |          0.8 |
| 3_fever      | llama3.2         | Moderate (0.1 - 0.5) |     277 |         55.4 |
| 3_fever      | llama3.2         | Null/Low (<= 0.1)    |     219 |         43.8 |
| 3_fever      | mistral_nemo     | High (> 0.5)         |      35 |          7   |
| 3_fever      | mistral_nemo     | Moderate (0.1 - 0.5) |     297 |         59.4 |
| 3_fever      | mistral_nemo     | Null/Low (<= 0.1)    |     168 |         33.6 |
| 3_fever      | phi4             | High (> 0.5)         |      11 |          2.2 |
| 3_fever      | phi4             | Moderate (0.1 - 0.5) |     197 |         39.4 |
| 3_fever      | phi4             | Null/Low (<= 0.1)    |     292 |         58.4 |
| 3_fever      | qwen2.5          | High (> 0.5)         |      50 |         10   |
| 3_fever      | qwen2.5          | Moderate (0.1 - 0.5) |     273 |         54.6 |
| 3_fever      | qwen2.5          | Null/Low (<= 0.1)    |     177 |         35.4 |
| 4_truthfulqa | deepseek_r1_1.5b | High (> 0.5)         |       1 |          0.2 |
| 4_truthfulqa | deepseek_r1_1.5b | Moderate (0.1 - 0.5) |     130 |         26   |
| 4_truthfulqa | deepseek_r1_1.5b | Null/Low (<= 0.1)    |     369 |         73.8 |
| 4_truthfulqa | gemma3           | High (> 0.5)         |       1 |          0.2 |
| 4_truthfulqa | gemma3           | Moderate (0.1 - 0.5) |     219 |         43.8 |
| 4_truthfulqa | gemma3           | Null/Low (<= 0.1)    |     280 |         56   |
| 4_truthfulqa | gpt_4o           | High (> 0.5)         |       2 |          0.4 |
| 4_truthfulqa | gpt_4o           | Moderate (0.1 - 0.5) |     195 |         39   |
| 4_truthfulqa | gpt_4o           | Null/Low (<= 0.1)    |     303 |         60.6 |
| 4_truthfulqa | llama3.2         | Moderate (0.1 - 0.5) |     197 |         39.4 |
| 4_truthfulqa | llama3.2         | Null/Low (<= 0.1)    |     303 |         60.6 |
| 4_truthfulqa | mistral_nemo     | High (> 0.5)         |       3 |          0.6 |
| 4_truthfulqa | mistral_nemo     | Moderate (0.1 - 0.5) |     191 |         38.2 |
| 4_truthfulqa | mistral_nemo     | Null/Low (<= 0.1)    |     306 |         61.2 |
| 4_truthfulqa | phi4             | Moderate (0.1 - 0.5) |     182 |         36.4 |
| 4_truthfulqa | phi4             | Null/Low (<= 0.1)    |     318 |         63.6 |
| 4_truthfulqa | qwen2.5          | High (> 0.5)         |       1 |          0.2 |
| 4_truthfulqa | qwen2.5          | Moderate (0.1 - 0.5) |     157 |         31.4 |
| 4_truthfulqa | qwen2.5          | Null/Low (<= 0.1)    |     342 |         68.4 |
| 5_mmlu_pro   | deepseek_r1_1.5b | High (> 0.5)         |       1 |          0.2 |
| 5_mmlu_pro   | deepseek_r1_1.5b | Moderate (0.1 - 0.5) |     154 |         30.8 |
| 5_mmlu_pro   | deepseek_r1_1.5b | Null/Low (<= 0.1)    |     345 |         69   |
| 5_mmlu_pro   | gemma3           | Moderate (0.1 - 0.5) |     120 |         24   |
| 5_mmlu_pro   | gemma3           | Null/Low (<= 0.1)    |     380 |         76   |
| 5_mmlu_pro   | gpt_4o           | High (> 0.5)         |       4 |          0.8 |
| 5_mmlu_pro   | gpt_4o           | Moderate (0.1 - 0.5) |     153 |         30.6 |
| 5_mmlu_pro   | gpt_4o           | Null/Low (<= 0.1)    |     343 |         68.6 |
| 5_mmlu_pro   | llama3.2         | Moderate (0.1 - 0.5) |     209 |         41.8 |
| 5_mmlu_pro   | llama3.2         | Null/Low (<= 0.1)    |     291 |         58.2 |
| 5_mmlu_pro   | mistral_nemo     | Moderate (0.1 - 0.5) |     124 |         24.8 |
| 5_mmlu_pro   | mistral_nemo     | Null/Low (<= 0.1)    |     376 |         75.2 |
| 5_mmlu_pro   | phi4             | Moderate (0.1 - 0.5) |      95 |         19   |
| 5_mmlu_pro   | phi4             | Null/Low (<= 0.1)    |     405 |         81   |
| 5_mmlu_pro   | qwen2.5          | High (> 0.5)         |       4 |          0.8 |
| 5_mmlu_pro   | qwen2.5          | Moderate (0.1 - 0.5) |     210 |         42   |
| 5_mmlu_pro   | qwen2.5          | Null/Low (<= 0.1)    |     286 |         57.2 |

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
| 3_fever      | gpt_4o           | SAS      | Neutral       | 0.818531 |
| 3_fever      | gpt_4o           | SAS      | Leading/Conf. | 0.824936 |
| 3_fever      | gpt_4o           | SAS      | Contradictory | 0.812607 |
| 3_fever      | gpt_4o           | NLI      | Neutral       | 0.55505  |
| 3_fever      | gpt_4o           | NLI      | Leading/Conf. | 0.529911 |
| 3_fever      | gpt_4o           | NLI      | Contradictory | 0.561141 |
| 3_fever      | gpt_4o           | GPT      | Neutral       | 0.8795   |
| 3_fever      | gpt_4o           | GPT      | Leading/Conf. | 0.95714  |
| 3_fever      | gpt_4o           | GPT      | Contradictory | 0.81228  |
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
| 3_fever      | phi4             | SAS      | Neutral       | 0.800926 |
| 3_fever      | phi4             | SAS      | Leading/Conf. | 0.807787 |
| 3_fever      | phi4             | SAS      | Contradictory | 0.795413 |
| 3_fever      | phi4             | NLI      | Neutral       | 0.57641  |
| 3_fever      | phi4             | NLI      | Leading/Conf. | 0.554694 |
| 3_fever      | phi4             | NLI      | Contradictory | 0.547684 |
| 3_fever      | phi4             | GPT      | Neutral       | 0.80168  |
| 3_fever      | phi4             | GPT      | Leading/Conf. | 0.92332  |
| 3_fever      | phi4             | GPT      | Contradictory | 0.69302  |
| 3_fever      | qwen2.5          | SAS      | Neutral       | 0.809814 |
| 3_fever      | qwen2.5          | SAS      | Leading/Conf. | 0.82115  |
| 3_fever      | qwen2.5          | SAS      | Contradictory | 0.775488 |
| 3_fever      | qwen2.5          | NLI      | Neutral       | 0.492245 |
| 3_fever      | qwen2.5          | NLI      | Leading/Conf. | 0.524855 |
| 3_fever      | qwen2.5          | NLI      | Contradictory | 0.383047 |
| 3_fever      | qwen2.5          | GPT      | Neutral       | 0.75582  |
| 3_fever      | qwen2.5          | GPT      | Leading/Conf. | 0.88368  |
| 3_fever      | qwen2.5          | GPT      | Contradictory | 0.47526  |
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
| 4_truthfulqa | gpt_4o           | SAS      | Neutral       | 0.759949 |
| 4_truthfulqa | gpt_4o           | SAS      | Leading/Conf. | 0.777299 |
| 4_truthfulqa | gpt_4o           | SAS      | Contradictory | 0.767532 |
| 4_truthfulqa | gpt_4o           | NLI      | Neutral       | 0.534017 |
| 4_truthfulqa | gpt_4o           | NLI      | Leading/Conf. | 0.552405 |
| 4_truthfulqa | gpt_4o           | NLI      | Contradictory | 0.556439 |
| 4_truthfulqa | gpt_4o           | GPT      | Neutral       | 0.64956  |
| 4_truthfulqa | gpt_4o           | GPT      | Leading/Conf. | 0.54026  |
| 4_truthfulqa | gpt_4o           | GPT      | Contradictory | 0.321994 |
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
| 4_truthfulqa | phi4             | SAS      | Neutral       | 0.75699  |
| 4_truthfulqa | phi4             | SAS      | Leading/Conf. | 0.777872 |
| 4_truthfulqa | phi4             | SAS      | Contradictory | 0.76634  |
| 4_truthfulqa | phi4             | NLI      | Neutral       | 0.53592  |
| 4_truthfulqa | phi4             | NLI      | Leading/Conf. | 0.544142 |
| 4_truthfulqa | phi4             | NLI      | Contradictory | 0.555224 |
| 4_truthfulqa | phi4             | GPT      | Neutral       | 0.6308   |
| 4_truthfulqa | phi4             | GPT      | Leading/Conf. | 0.57214  |
| 4_truthfulqa | phi4             | GPT      | Contradictory | 0.39924  |
| 4_truthfulqa | qwen2.5          | SAS      | Neutral       | 0.747328 |
| 4_truthfulqa | qwen2.5          | SAS      | Leading/Conf. | 0.749698 |
| 4_truthfulqa | qwen2.5          | SAS      | Contradictory | 0.752178 |
| 4_truthfulqa | qwen2.5          | NLI      | Neutral       | 0.507052 |
| 4_truthfulqa | qwen2.5          | NLI      | Leading/Conf. | 0.518958 |
| 4_truthfulqa | qwen2.5          | NLI      | Contradictory | 0.526277 |
| 4_truthfulqa | qwen2.5          | GPT      | Neutral       | 0.6347   |
| 4_truthfulqa | qwen2.5          | GPT      | Leading/Conf. | 0.55858  |
| 4_truthfulqa | qwen2.5          | GPT      | Contradictory | 0.42754  |
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
| 5_mmlu_pro   | gpt_4o           | SAS      | Neutral       | 0.810307 |
| 5_mmlu_pro   | gpt_4o           | SAS      | Leading/Conf. | 0.783632 |
| 5_mmlu_pro   | gpt_4o           | SAS      | Contradictory | 0.778931 |
| 5_mmlu_pro   | gpt_4o           | NLI      | Neutral       | 0.588027 |
| 5_mmlu_pro   | gpt_4o           | NLI      | Leading/Conf. | 0.564127 |
| 5_mmlu_pro   | gpt_4o           | NLI      | Contradictory | 0.517271 |
| 5_mmlu_pro   | gpt_4o           | GPT      | Neutral       | 0.8825   |
| 5_mmlu_pro   | gpt_4o           | GPT      | Leading/Conf. | 0.71036  |
| 5_mmlu_pro   | gpt_4o           | GPT      | Contradictory | 0.59706  |
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
| 5_mmlu_pro   | phi4             | SAS      | Neutral       | 0.804743 |
| 5_mmlu_pro   | phi4             | SAS      | Leading/Conf. | 0.7958   |
| 5_mmlu_pro   | phi4             | SAS      | Contradictory | 0.791525 |
| 5_mmlu_pro   | phi4             | NLI      | Neutral       | 0.627832 |
| 5_mmlu_pro   | phi4             | NLI      | Leading/Conf. | 0.583736 |
| 5_mmlu_pro   | phi4             | NLI      | Contradictory | 0.570581 |
| 5_mmlu_pro   | phi4             | GPT      | Neutral       | 0.87512  |
| 5_mmlu_pro   | phi4             | GPT      | Leading/Conf. | 0.73338  |
| 5_mmlu_pro   | phi4             | GPT      | Contradictory | 0.73918  |
| 5_mmlu_pro   | qwen2.5          | SAS      | Neutral       | 0.806971 |
| 5_mmlu_pro   | qwen2.5          | SAS      | Leading/Conf. | 0.781836 |
| 5_mmlu_pro   | qwen2.5          | SAS      | Contradictory | 0.763737 |
| 5_mmlu_pro   | qwen2.5          | NLI      | Neutral       | 0.554378 |
| 5_mmlu_pro   | qwen2.5          | NLI      | Leading/Conf. | 0.529051 |
| 5_mmlu_pro   | qwen2.5          | NLI      | Contradictory | 0.486474 |
| 5_mmlu_pro   | qwen2.5          | GPT      | Neutral       | 0.8295   |
| 5_mmlu_pro   | qwen2.5          | GPT      | Leading/Conf. | 0.6549   |
| 5_mmlu_pro   | qwen2.5          | GPT      | Contradictory | 0.51854  |
