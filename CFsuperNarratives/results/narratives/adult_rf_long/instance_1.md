# Instance 1

## Original instance and counterfactuals

|          |   age |   education-num |   hours-per-week |   capital-gain |   capital-loss |   sex |   married |   income |
|:---------|------:|----------------:|-----------------:|---------------:|---------------:|------:|----------:|---------:|
| original |    17 |               8 |               20 |              0 |              0 |     0 |         1 |        0 |
| cf_1     |    17 |              13 |               20 |          23570 |           3933 |     0 |         1 |        1 |
| cf_2     |    17 |              16 |               50 |          83981 |              0 |     0 |         1 |        1 |
| cf_3     |    17 |               8 |               74 |           8757 |           1165 |     0 |         1 |        1 |
| cf_4     |    17 |              11 |               20 |          11956 |           1244 |     0 |         1 |        1 |
| cf_5     |    17 |              11 |               20 |           8082 |              0 |     0 |         1 |        1 |
| cf_6     |    17 |              16 |               75 |          89917 |              0 |     0 |         1 |        1 |
| cf_7     |    17 |               8 |               69 |           8919 |              0 |     0 |         1 |        1 |
| cf_8     |    17 |               8 |               45 |          29086 |              0 |     0 |         1 |        1 |
| cf_9     |    17 |               8 |               53 |          12632 |              0 |     0 |         1 |        1 |
| cf_10    |    17 |              14 |                5 |          80251 |              0 |     0 |         1 |        1 |
| cf_11    |    17 |               8 |               45 |          61599 |              0 |     0 |         1 |        0 |
| cf_12    |    17 |              12 |               20 |          30116 |              0 |     0 |         0 |        1 |
| cf_13    |    17 |               8 |               62 |           8388 |              0 |     0 |         1 |        1 |
| cf_14    |    17 |               8 |               37 |          70099 |              0 |     0 |         0 |        0 |
| cf_15    |    17 |              15 |               20 |          97661 |              0 |     0 |         1 |        1 |
| cf_16    |    17 |               8 |               20 |          19342 |            911 |     0 |         0 |        0 |
| cf_17    |    17 |              12 |               20 |          36094 |              0 |     0 |         0 |        1 |
| cf_18    |    17 |               8 |               58 |          94597 |              0 |     0 |         1 |        1 |
| cf_19    |    17 |               8 |               62 |          18798 |              0 |     0 |         1 |        1 |
| cf_20    |    17 |               8 |               65 |          71236 |              0 |     0 |         1 |        1 |
| cf_21    |    17 |               6 |               84 |          14702 |              0 |     0 |         1 |        0 |
| cf_22    |    17 |              11 |               20 |          11146 |              0 |     0 |         0 |        1 |
| cf_23    |    17 |              12 |               96 |          65904 |              0 |     0 |         1 |        1 |
| cf_24    |    17 |               8 |               43 |          71612 |              0 |     0 |         1 |        1 |
| cf_25    |    17 |              15 |               20 |          72536 |              0 |     0 |         1 |        1 |
| cf_26    |    17 |               8 |               54 |          93499 |              0 |     0 |         1 |        1 |
| cf_27    |    17 |              15 |               20 |          30322 |              0 |     0 |         1 |        1 |
| cf_28    |    17 |               8 |               50 |           7140 |            401 |     0 |         1 |        1 |
| cf_29    |    17 |               8 |               20 |          12792 |              0 |     0 |         0 |        1 |
| cf_30    |    17 |              10 |               20 |          84416 |              0 |     0 |         0 |        1 |
| cf_31    |    17 |              16 |               20 |          47865 |              0 |     0 |         0 |        1 |
| cf_32    |    17 |               8 |               44 |          96265 |              0 |     0 |         1 |        1 |
| cf_33    |    17 |               8 |               58 |          97453 |              0 |     0 |         0 |        1 |
| cf_34    |    17 |               8 |               50 |          83981 |              0 |     0 |         1 |        1 |
| cf_35    |    17 |              16 |               20 |          11701 |           1026 |     0 |         1 |        1 |
| cf_36    |    17 |               8 |               74 |          72921 |              0 |     0 |         0 |        1 |
| cf_37    |    17 |               1 |               55 |          92565 |              0 |     0 |         1 |        0 |
| cf_38    |    17 |               6 |               63 |          12498 |              0 |     0 |         1 |        0 |
| cf_39    |    17 |               8 |               54 |          85846 |              0 |     0 |         0 |        1 |
| cf_40    |    17 |               8 |               59 |          66958 |              0 |     0 |         1 |        1 |
| cf_41    |    17 |               8 |               44 |          63431 |            505 |     0 |         1 |        0 |
| cf_42    |    17 |               8 |               43 |          80442 |              0 |     0 |         1 |        1 |
| cf_43    |    17 |              13 |               20 |          83947 |              0 |     0 |         1 |        1 |
| cf_44    |    17 |               8 |               64 |          10150 |              0 |     0 |         1 |        1 |
| cf_45    |    17 |              13 |               20 |          57583 |              0 |     0 |         1 |        1 |
| cf_46    |    17 |               8 |               65 |          82257 |              0 |     0 |         1 |        1 |
| cf_47    |    17 |              12 |               20 |          74852 |              0 |     0 |         1 |        1 |
| cf_48    |    17 |               8 |               44 |          15347 |              0 |     0 |         1 |        1 |
| cf_49    |    17 |              14 |               20 |          58351 |              0 |     0 |         1 |        1 |
| cf_50    |    17 |               8 |               20 |          18719 |            967 |     0 |         0 |        0 |

## Counterfactual super narrative

The model currently predicts that this 17‑year‑old married woman will have an annual income at or below 50,000 USD. In her current situation, she has a mid‑range education level (education level 8), works 20 hours per week, and has no capital gains or capital losses recorded. Across the alternative “what if” scenarios, the features that change most often when the prediction flips to income above 50,000 are capital gains, hours worked per week, and education level, while marital status changes less frequently. Capital gains are especially striking: in almost all counterfactuals where the prediction is higher income, capital gains jump from 0 to values in the tens of thousands, often between about 8,000 and over 90,000 USD, suggesting that the model treats substantial investment income as a strong signal of higher overall income. Hours worked per week also often increase from 20 to much higher levels, such as 43–75 hours in counterfactuals 3, 7, 13, 18, 19, 20, 23, 26, 28, 32, 33, 36, 39, 40, 44, and 46, indicating that working many more hours is another route the model associates with higher income. Education level tends to be higher in many of the higher‑income scenarios as well: for example, education levels of 11, 12, 13, 14, 15, or 16 appear in counterfactuals 1, 2, 4, 5, 6, 10, 12, 15, 17, 22, 23, 25, 27, 30, 31, 35, 43, 45, 47, and 49, compared with the original level of 8. Marital status changes from married to not married in some higher‑income scenarios (such as counterfactuals 12, 17, 22, 29, 30, and 31), but there are also many higher‑income scenarios where marital status stays married, so this seems less central than capital gains, hours, and education.

From these patterns, the model appears to consider several main strategies for moving from a lower‑income to a higher‑income prediction. One strategy is “high capital gains with similar work hours,” where capital gains rise sharply while hours stay around 20, as in counterfactuals 1, 4, 5, 10, 15, 25, 27, 31, 35, 43, 45, 47, and 49. A second strategy is “many more work hours plus some capital gains,” where hours increase into the 40–90 hour range and capital gains are also positive, as in counterfactuals 3, 7, 8, 9, 13, 18, 19, 20, 23, 24, 26, 28, 32, 33, 36, 39, 40, 42, 44, 46, and 48. A third strategy is “higher education combined with capital gains,” where education level rises above 8 and capital gains are substantial, sometimes even when hours remain low, as in counterfactuals 2, 6, 10, 15, 25, 27, 30, 31, 35, 43, 45, 47, and 49. Finally, there is a “change in marital status plus capital gains” pattern, where the person is not married and has positive capital gains, as in counterfactuals 12, 17, 22, 29, and 30, though this pattern is less consistent than the others. Overall, the concrete numbers in the table show that the model most strongly associates higher income with large capital gains, often supported by either more hours worked, higher education, or both, while marital status plays a secondary and less consistent role.
