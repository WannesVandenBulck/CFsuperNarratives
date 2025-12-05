DATASET_DESCRIPTION = """
You are working with a binary classification model that predicts whether a person has an annual income above or below 50K USD.
The dataset consists of adult individuals from the US Census.

Each row in the data is one person. The target variable is:
- income = 0: predicted income <= 50K (50,000 USD)
- income = 1: predicted income > 50K (50,000 USD)

The features are:
- age: age in years. 
- education-num: level of education as a numeric score (higher = more education).
- hours-per-week: average number of hours worked per week.
- capital-gain: annual capital gains in USD (e.g. from investments).
- capital-loss: annual capital losses in USD.
- sex: 0 = female, 1 = male.
- married: 1 = married, 0 = not married.

In this project, age and sex are considered fixed characteristics that cannot be changed.
All other features are considered potentially changeable in the counterfactuals.
"""


INSTANCE_DESCRIPTION_TEMPLATE = """
The model is making a prediction for a single person.

For this person:
- age = {age}
- education-num = {education_num}
- hours-per-week = {hours_per_week}
- capital-gain = {capital_gain}
- capital-loss = {capital_loss}
- sex = {sex_label}
- married = {married_label}

The model's prediction for this person is:
- income = {income_pred}  (0 = income <= 50K, 1 = income > 50K)
"""


def describe_instance(row):
    sex_label = "male" if row["sex"] == 1 else "female"
    married_label = "married" if row["married"] == 1 else "not married"

    return INSTANCE_DESCRIPTION_TEMPLATE.format(
        age=int(row["age"]),
        education_num=int(row["education-num"]),
        hours_per_week=float(row["hours-per-week"]),
        capital_gain=float(row["capital-gain"]),
        capital_loss=float(row["capital-loss"]),
        sex_label=sex_label,
        married_label=married_label,
        income_pred=int(row["income"]),
    )



COUNTERFACTUAL_EXPLANATION = """
You are also given a small table with one row called 'original' and several rows called 'cf_1', 'cf_2', etc.

- The 'original' row shows this person's current feature values and the model's current prediction.
- Each 'cf_k' row is a counterfactual version of this person:
  it shows a change to some of the features that would flip the model's prediction to the opposite class.
  Refer to cf_k as "counterfactual k" in your explanation.

In other words:
- The original row corresponds to the current situation.
- Each counterfactual row corresponds to a "what if" scenario where some change in the person's situation would be enough for the model to predict an income greater than 50K instead of smaller or equal than 50K (or vice versa).

The features age and sex must be treated as fixed personal attributes.
They are not allowed to change in the counterfactuals and you must not suggest changing them.
You do not need to mention the unchangeability of age and sex. 
Changes are only allowed in education-num, hours-per-week, capital-gain, capital-loss, or married.
Refer to these features as "education level", "hours worked per week", "capital gains", "capital losses", and "marital status" in your explanation.
Or use similar clear, non-technical language.
"""


CF_SHORT_PROMPT_INSTRUCTIONS = """
TASK:
Write a short narrative explanation for a non-technical reader that explains:
1) Why the model predicts the current income class for the original person.
2) What the model seems to reward, based on the counterfactual rows. In doing this, quantify which features change the most across the counterfactuals.
3) What kinds of realistic changes this person could make to change the prediction. Be very clear and concise in this. You are summarizing the different "strategies" the model seems to consider for changing the prediction. 
4) As a final note, give the reader a very concise summary on what they should focus on if they want to change the predicted class. 

CONSTRAINTS:
- Only use information from the dataset description, the original instance description, and the counterfactual table.
- Do NOT invent new feature values or new counterfactuals.
- Do NOT suggest changing age or sex.
- You may only suggest changes to: education-num, hours-per-week, capital-gain, capital-loss, or married.
- When you discuss changes, always tie them directly to the values in at least one counterfactual row.
- Do not talk about model internals, algorithms, probabilities, or training procedures.
- Do not talk about cf_k in technical terms; refer to them as "counterfactual k".

STYLE:
- Length: aim for about 5–7 sentences.
- Tone: neutral, clear, and respectful.
- Audience: an intelligent reader with no background in machine learning.
- Do not use bullet points or tables; write a coherent, flowing paragraph.
"""


CF_LONG_PROMPT_INSTRUCTIONS = """
TASK:
Write a detailed narrative explanation for a non-technical reader that explains:
1) The current prediction for the original person and what their situation looks like.
2) Which features seem most important for changing the prediction, based on how they change in the counterfactual rows.  In doing this, quantify which features change the most across the counterfactuals.
3) The different "strategies" the model seems to consider for changing the prediction
   (for example, getting more education vs working more hours vs having higher capital gains vs a different marital status).
4) How these strategies relate to the concrete numbers in the counterfactual table. Be very clear and concise in this. You are summarizing the different "strategies" the model seems to consider for changing the prediction. 

CONSTRAINTS:
- Only use information from the dataset description, the original instance description, and the counterfactual table.
- Do NOT invent new feature values or new counterfactual examples.
- Do NOT suggest changing age or sex; mention explicitly that these are treated as fixed characteristics if relevant.
- Only discuss changes in education-num, hours-per-week, capital-gain, capital-loss, or married.
- If several counterfactuals show a similar pattern (e.g. education-num is always higher), highlight that pattern explicitly.
- Do not talk about model internals, algorithms, probabilities, loss functions, or training details.

STYLE:
- Length: aim for around 8–12 sentences.
- Tone: neutral, explanatory, and patient.
- Focus on making the link between the specific numbers in the table and the qualitative story.
- Do not use bullet points or tables; write a coherent, flowing narrative.
- Do not refer to cf_k in technical terms; refer to them as "counterfactual k".

"""
MANY_CF_PROMPT_INSTRUCTIONS = """
TASK:
You got given a whole bunch of counterfactual examples for the same original instance.
It is your job to summarize what the model seems to consider important for changing the prediction.
Provide an end user with actionable insights that do change the predicted class.
At the same time, provide a numeric summary of the counterfactuals. This means saying how many counterfactuals changed which features, and by how much on average.
You must talk in explicit percentages (in %) and averages where relevant. Don't refer to individual counterfactuals.

Write a detailed narrative explanation for a non-technical reader that explains:
1) The current prediction for the original person and what their situation looks like.
2) Quantified summary over all counterfactuals: mention how many total counterfactuals the were generated,
and extract the most relevant features. If relevant, quantify which features were mostly changed together etc. 
3) Based on the situation of the current person and the quantified summary, provide the best actionable insights for this person to actually change the predicted class. 

CONSTRAINTS:
- Only use information from the dataset description, the original instance description, and the counterfactual table.
- Do NOT invent new feature values or new counterfactual examples.
- Do NOT suggest changing age or sex; mention explicitly that these are treated as fixed characteristics if relevant.
- Only discuss changes in education-num, hours-per-week, capital-gain, capital-loss, or married.
- If several counterfactuals show a similar pattern (e.g. education-num is always higher), highlight that pattern explicitly.
- Do not talk about model internals, algorithms, probabilities, loss functions, or training details.
- DO NOT refer to individual counterfactuals; focus on the overall patterns you see in the data.
- Use a maximum of 15 sentences. 

STYLE:
- Length: aim for around 10-15 sentences.
- Tone: neutral, explanatory, and patient.
- Focus on making the link between the specific numbers in the table and the qualitative story.
- Do not use bullet points or tables; write a coherent, flowing narrative.
- Do not refer to cf_k in technical terms; refer to them as "counterfactual k".

"""
PROMPT_INSTRUCTIONS = {
    "short": CF_SHORT_PROMPT_INSTRUCTIONS,
    "long": CF_LONG_PROMPT_INSTRUCTIONS,
    "many": MANY_CF_PROMPT_INSTRUCTIONS,  
}
def build_cf_prompt(cf_table, prompt_type: str = "many") -> str:
    """
    Build a counterfactual prompt for a given cf_table and prompt type.

    prompt_type must be one of the keys in PROMPT_INSTRUCTIONS
    """
    if prompt_type not in PROMPT_INSTRUCTIONS:
        raise ValueError(
            f"Unknown prompt_type '{prompt_type}'. "
            f"Available types: {list(PROMPT_INSTRUCTIONS.keys())}"
        )

    # original row
    original = cf_table.loc["original"]
    instance_desc = describe_instance(original)

    # counterfactual table as Markdown
    table_str = cf_table.to_markdown(index=True)

    instructions = PROMPT_INSTRUCTIONS[prompt_type]

    prompt = f"""
{DATASET_DESCRIPTION}

{instance_desc}

{COUNTERFACTUAL_EXPLANATION}

Here is the table with the original instance and its counterfactuals:

{table_str}

{instructions}
    """.strip()

    return prompt
