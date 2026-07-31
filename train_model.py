import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Path configuration
DATA_PATH = os.path.join("data", "stars_dataset.csv")

def load_dataset(filepath):
    """
    Loads the preprocessed OGLE-III variable star dataset from CSV.
    """
    if not os.path.exists(filepath):
        # Fallback check if executing from root directory
        filepath = os.path.join("model_building", "data", "stars_dataset.csv")
    
    print(f"Loading dataset from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully with {len(df)} rows and {len(df.columns)} columns.")
    return df


def prepare_features_and_target(df):
    """
    Task 1: Separate DataFrame into feature matrix X and target Series y.
    
    Features to extract:
      - 'I_magnitude': Average brightness in I-band
      - 'period_days': Pulsation/orbital period in days
      - 'I_band_amplitude': Brightness variation range
      - 'V_minus_I_color': V - I color index (temperature proxy)
      
    Target to extract:
      - 'star_type': Star classification label (Cepheid, RR Lyrae, Mira, Eclipsing Binary)
    """
    # TODO: Step 1.1 - Define a list of feature column names called `feature_cols`
    # TODO: Step 1.2 - Extract feature matrix X from df using feature_cols
    # TODO: Step 1.3 - Extract target vector y from df['star_type']
    # TODO: Step 1.4 - Return X, y
    
    raise NotImplementedError("Task 1 (prepare_features_and_target) is not implemented yet!")


def split_data(X, y):
    """
    Task 2: Split X and y into 80% training set and 20% testing set using random_state=42.
    
    Use scikit-learn's `train_test_split` function.
    """
    # TODO: Step 2.1 - Call train_test_split(X, y, test_size=0.2, random_state=42)
    # TODO: Step 2.2 - Return X_train, X_test, y_train, y_test
    
    raise NotImplementedError("Task 2 (split_data) is not implemented yet!")


def train_and_evaluate_model(model, model_name, X_train, X_test, y_train, y_test):
    """
    Task 3: Train model on training data, evaluate on testing data, print metrics,
    and compute 5-fold cross-validation scores.
    """
    print("\n" + "=" * 60)
    print(f"  Training Model: {model_name}")
    print("=" * 60)
    
    # TODO: Step 3.1 - Fit the model using X_train and y_train
    # model.fit(...)
    
    # TODO: Step 3.2 - Make predictions on X_test using model.predict(...)
    # y_pred = model.predict(...)
    
    # TODO: Step 3.3 - Compute accuracy score using accuracy_score(y_test, y_pred)
    # accuracy = accuracy_score(...)
    # print(f"Test Accuracy: {accuracy * 100:.2f}%")
    
    # TODO: Step 3.4 - Print full classification report using classification_report(y_test, y_pred)
    # print("\nClassification Report:")
    # print(classification_report(...))
    
    # TODO: Step 3.5 - Compute 5-fold cross-validation on X_train and y_train using cross_val_score
    # cv_scores = cross_val_score(model, X_train, y_train, cv=5)
    # print(f"5-Fold Cross-Validation Scores: {cv_scores}")
    # print(f"Mean CV Accuracy: {cv_scores.mean() * 100:.2f}% (+/- {cv_scores.std() * 100:.2f}%)")
    
    raise NotImplementedError("Task 3 (train_and_evaluate_model) is not implemented yet!")


def main():
    df = load_dataset(DATA_PATH)
    
    print("\nExtracting features and target...")
    X, y = prepare_features_and_target(df)
    
    print("\nSplitting dataset into train and test sets...")
    X_train, X_test, y_train, y_test = split_data(X, y)
    print(f"Training set size: {len(X_train)} samples")
    print(f"Testing set size:  {len(X_test)} samples")
    
    # Model 1: Decision Tree Classifier
    dt_model = DecisionTreeClassifier(random_state=42)
    train_and_evaluate_model(dt_model, "Decision Tree Classifier", X_train, X_test, y_train, y_test)
    
    # Model 2: Random Forest Classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    train_and_evaluate_model(rf_model, "Random Forest Classifier", X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
