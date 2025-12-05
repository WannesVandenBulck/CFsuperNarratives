# Instance 2

## Original instance and counterfactuals

|          |   age |   education-num |   hours-per-week |   capital-gain |   capital-loss |   sex |   married |   income |
|:---------|------:|----------------:|-----------------:|---------------:|---------------:|------:|----------:|---------:|
| original |    25 |               9 |               40 |              0 |              0 |     1 |         1 |        0 |
| cf_1     |    25 |               9 |               14 |          79070 |              0 |     1 |         1 |        1 |
| cf_2     |    25 |              12 |               40 |              0 |           2775 |     1 |         1 |        1 |
| cf_3     |    25 |               9 |               40 |          15628 |              0 |     1 |         0 |        1 |
| cf_4     |    25 |               9 |               40 |          36007 |           2616 |     1 |         1 |        1 |
| cf_5     |    25 |               3 |               40 |          90219 |              0 |     1 |         1 |        1 |
| cf_6     |    25 |               9 |               40 |              0 |           2615 |     1 |         0 |        1 |
| cf_7     |    25 |              16 |               40 |          45568 |              0 |     1 |         1 |        1 |
| cf_8     |    25 |               9 |               40 |              0 |           4032 |     1 |         0 |        1 |
| cf_9     |    25 |               9 |               40 |          52387 |              0 |     1 |         1 |        1 |
| cf_10    |    25 |               1 |               40 |          21875 |              0 |     1 |         1 |        1 |
| cf_11    |    25 |               9 |               40 |          87741 |              0 |     1 |         0 |        1 |
| cf_12    |    25 |               9 |               40 |              0 |           2829 |     1 |         0 |        1 |
| cf_13    |    25 |               9 |               72 |          85358 |              0 |     1 |         1 |        1 |
| cf_14    |    25 |               9 |               40 |          55497 |              0 |     1 |         1 |        1 |
| cf_15    |    25 |              10 |               40 |          34432 |              0 |     1 |         1 |        1 |
| cf_16    |    25 |               9 |               40 |              0 |           1921 |     1 |         1 |        1 |
| cf_17    |    25 |               9 |               40 |          11432 |           2447 |     1 |         1 |        1 |
| cf_18    |    25 |               9 |               40 |           8955 |           1777 |     1 |         1 |        1 |
| cf_19    |    25 |               9 |               40 |          82512 |              0 |     1 |         1 |        1 |
| cf_20    |    25 |              15 |               40 |          76109 |              0 |     1 |         1 |        1 |
| cf_21    |    25 |               7 |               40 |          46647 |              0 |     1 |         1 |        1 |
| cf_22    |    25 |               9 |               40 |          91638 |              0 |     1 |         1 |        1 |
| cf_23    |    25 |               2 |               40 |          60550 |              0 |     1 |         1 |        1 |
| cf_24    |    25 |               9 |               40 |          28380 |              0 |     1 |         1 |        1 |
| cf_25    |    25 |               9 |               40 |          45518 |              0 |     1 |         0 |        1 |
| cf_26    |    25 |               9 |               40 |          48859 |              0 |     1 |         1 |        1 |
| cf_27    |    25 |              10 |               40 |          93501 |              0 |     1 |         1 |        1 |
| cf_28    |    25 |               9 |                6 |          33476 |              0 |     1 |         1 |        1 |
| cf_29    |    25 |               9 |               40 |          76563 |           1174 |     1 |         1 |        1 |
| cf_30    |    25 |               9 |                9 |          93827 |              0 |     1 |         1 |        1 |
| cf_31    |    25 |              10 |               40 |          35405 |              0 |     1 |         1 |        1 |
| cf_32    |    25 |               9 |               40 |          56198 |              0 |     1 |         1 |        1 |
| cf_33    |    25 |              13 |               40 |          87168 |              0 |     1 |         1 |        1 |
| cf_34    |    25 |               9 |               40 |          49123 |              0 |     1 |         1 |        1 |
| cf_35    |    25 |              12 |               40 |          54566 |              0 |     1 |         1 |        1 |
| cf_36    |    25 |              15 |               40 |              0 |           3268 |     1 |         1 |        1 |
| cf_37    |    25 |              13 |               40 |              0 |           2475 |     1 |         1 |        1 |
| cf_38    |    25 |               9 |               40 |          10100 |              0 |     1 |         1 |        1 |
| cf_39    |    25 |              16 |               40 |          68463 |              0 |     1 |         1 |        1 |
| cf_40    |    25 |               9 |               40 |          60954 |              0 |     1 |         1 |        1 |
| cf_41    |    25 |               9 |               81 |              0 |              0 |     1 |         1 |        1 |
| cf_42    |    25 |               9 |               40 |          74095 |              0 |     1 |         0 |        1 |
| cf_43    |    25 |               9 |               40 |          40523 |              0 |     1 |         1 |        1 |
| cf_44    |    25 |               9 |               40 |          37829 |              0 |     1 |         1 |        1 |
| cf_45    |    25 |               9 |               40 |          73932 |              0 |     1 |         1 |        1 |
| cf_46    |    25 |               9 |               40 |          69652 |              0 |     1 |         1 |        1 |
| cf_47    |    25 |              10 |               40 |          59197 |              0 |     1 |         1 |        1 |
| cf_48    |    25 |               9 |               40 |          77496 |              0 |     1 |         1 |        1 |
| cf_49    |    25 |               9 |               98 |          20300 |              0 |     1 |         1 |        1 |
| cf_50    |    25 |              13 |               40 |          46448 |              0 |     1 |         1 |        1 |

## Counterfactual super narrative

The model currently predicts that this 25‑year‑old married man, with an education level of 9, working 40 hours per week, with no capital gains or losses, has an annual income at or below 50,000 USD. In the alternative “what if” scenarios, his age and sex stay the same, but the model changes its prediction to an income above 50,000 whenever certain other aspects of his situation change. Looking across all the counterfactuals, the feature that changes most often and by the largest amounts is capital gains: in many scenarios, it jumps from 0 to very high values, such as 15,628 in counterfactual 3, 36,007 in counterfactual 4, 52,387 in counterfactual 9, and even above 90,000 in counterfactuals 5, 22, 30, and 48. Capital losses also change in several scenarios, going from 0 to values like 2,615 in counterfactual 6, 2,829 in counterfactual 12, and over 3,000 in counterfactual 36, which the model also treats as consistent with a higher income.

Education level is another important lever: in some scenarios, increasing it from 9 to 10, 12, 13, 15, or 16 (for example in counterfactuals 15, 20, 33, 35, 36, 37, 39, 47, and 50) goes hand in hand with the model predicting an income above 50,000, sometimes together with higher capital gains or capital losses. There are also a few cases where education is actually lower than 9, such as 7, 3, 2, or even 1 in counterfactuals 21, 5, 23, and 10, but the model still predicts higher income because capital gains are extremely high in those scenarios, suggesting that very large investment income can outweigh lower formal education. Hours worked per week changes less often, but when it does, the changes are large: in counterfactual 41, hours rise from 40 to 81 with no change in capital gains or losses, and in counterfactuals 13 and 49 they rise to 72 and 98 respectively, which the model also associates with higher income; in contrast, in counterfactuals 1, 28, and 30, hours drop sharply (to 14, 6, and 9), but this is paired with very high capital gains, again showing that investment income can compensate for fewer work hours.

Marital status changes in a smaller number of scenarios, but when it does, it often appears together with other favorable changes. For example, in counterfactuals 3, 6, 8, 11, 12, 25, and 42, the person is not married instead of married, and at the same time either capital gains or capital losses are positive and often quite large, which the model treats as a combination that leads to higher income. Putting this together, the model seems to consider several main strategies for moving this person into the higher‑income group: one strategy is to keep education and hours the same but add substantial capital gains or capital losses; another is to increase education level, sometimes with moderate capital gains or losses; a third is to work many more hours per week even without investment income; and a fourth is to combine being not married with positive capital gains or losses. All of these strategies are grounded in the specific numbers in the table, and they show that, for this person, the model is especially sensitive to large changes in capital gains, followed by changes in education level, hours worked, and, to a lesser extent, marital status.
