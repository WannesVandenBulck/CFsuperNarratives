# scripts/experiments/make_cf_tables.py

import os
import pickle
import pandas as pd
import dice_ml
from dice_ml import Dice
from sklearn.metrics import classification_report, roc_auc_score


# 0. Basic configuration

# Path to your trained random forest model
MODEL_PATH = r"C:\Users\wavandenbulck\Desktop\CFsuperNarratives\data\random_forest_model.pkl"

# Folder where your train/test CSVs live
DATA_DIR = "data"

# Where to save CF tables
CF_TABLE_DIR = os.path.join("data", "cf_tables")
os.makedirs(CF_TABLE_DIR, exist_ok=True)

# How many counterfactuals per instance
TOTAL_CFS = 15


# 1. Load model and data

with open(MODEL_PATH, "rb") as f:
    rf = pickle.load(f)

X_test = pd.read_csv(os.path.join(DATA_DIR, "X_test.csv"))
y_test = pd.read_csv(os.path.join(DATA_DIR, "y_test.csv"))
X_train = pd.read_csv(os.path.join(DATA_DIR, "X_train.csv"))
y_train = pd.read_csv(os.path.join(DATA_DIR, "y_train.csv"))


# 2. Evaluate model and select instances predicted <= 50K

print("=== Test performance ===")
y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred))

accuracy = (y_test.values.flatten() == y_pred).mean()
print(f"Accuracy: {accuracy:.2f}")

AUC = roc_auc_score(y_test, rf.predict_proba(X_test)[:, 1])
print(f"AUC: {AUC:.2f}")

# We assume: income = 0 => <= 50K, income = 1 => > 50K
INSTANCE_INDICES = [i for i, p in enumerate(y_pred) if p == 0]
# Limit to first N low-income cases
MAX_CASES = 1  # <- change this number
INSTANCE_INDICES = INSTANCE_INDICES[:MAX_CASES]

print(f"Using only the first {MAX_CASES} low-income instances:")
print(INSTANCE_INDICES)
print()
print(f"Will generate counterfactuals for {len(INSTANCE_INDICES)} instances predicted <= 50K (class 0).")
print("First few indices:", INSTANCE_INDICES[:20])


# 3. Prepare data for DiCE

df_train = X_train.copy()
# ensure target column is named "income"
df_train["income"] = y_train.values.ravel()

continuous_features = [
    "age",
    "education-num",
    "hours-per-week",
    "capital-gain",
    "capital-loss",
]

categorical_features = [
    "sex",
    "married",
]

# Features that DiCE is allowed to change (age and sex are fixed)
mutable_features = [
    "education-num",
    "hours-per-week",
    "capital-gain",
    "capital-loss",
    "married",
]

data_dice = dice_ml.Data(
    dataframe=df_train,
    continuous_features=continuous_features,
    categorical_features=categorical_features,
    outcome_name="income",
)

model_dice = dice_ml.Model(
    model=rf,
    backend="sklearn",
)

exp = Dice(
    data_dice,
    model_dice,
    method="random",  # model-agnostic explainer
)


# 4. Helper to build CF table

def build_cf_table_for_instance(idx: int) -> pd.DataFrame:
    """
    For X_test row idx, generate CFs and return a table with:
    - row 'original'
    - rows 'cf_1', 'cf_2', ...
    """
    # query instance as DataFrame
    query_instance = X_test.iloc[[idx]]

    # generate counterfactuals
    dice_cf = exp.generate_counterfactuals(
        query_instance,
        total_CFs=TOTAL_CFS,
        desired_class="opposite",
        features_to_vary=mutable_features,
    )

    cf_df = dice_cf.cf_examples_list[0].final_cfs_df.copy()

    # build original row with same columns
    orig_df = query_instance.copy()

    # add the model prediction as 'income' if not present
    if "income" in cf_df.columns and "income" not in orig_df.columns:
        orig_df["income"] = rf.predict(query_instance)[0]

    # re-order columns to match cf_df
    orig_df = orig_df[cf_df.columns]

    # nice indices
    orig_df.index = ["original"]
    cf_df.index = [f"cf_{i+1}" for i in range(len(cf_df))]

    # combine
    cf_table = pd.concat([orig_df, cf_df], axis=0)
    return cf_table


# 5. Main loop

if __name__ == "__main__":
    for idx in INSTANCE_INDICES:
        print(f"Generating CF table for instance {idx} (predicted <= 50K)...")
        cf_table = build_cf_table_for_instance(idx)
        out_path = os.path.join(CF_TABLE_DIR, f"instance_{idx}.csv")
        cf_table.to_csv(out_path)
        print(f"Saved {out_path}")