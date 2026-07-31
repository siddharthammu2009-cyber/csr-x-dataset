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
    Task 1 Solution: Separate DataFrame into feature matrix X and target Series y.
    """
    feature_cols = ['I_magnitude', 'period_days', 'I_band_amplitude', 'V_minus_I_color']
    X = df[feature_cols]
    y = df['star_type']
    return X, y


def split_data(X, y):
    """
    Task 2 Solution: Split X and y into 80% training set and 20% testing set using random_state=42.
    """
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_and_evaluate_model(model, model_name, X_train, X_test, y_train, y_test):
    """
    Task 3 Solution: Train model on training data, evaluate on testing data, print metrics,
    and compute 5-fold cross-validation scores.
    """
    print("\n" + "=" * 60)
    print(f"  Training Model: {model_name}")
    print("=" * 60)
    
    # 1. Fit model on training data
    model.fit(X_train, y_train)
    
    # 2. Make predictions on unseen test data
    y_pred = model.predict(X_test)
    
    # 3. Calculate and print accuracy
    acc = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {acc * 100:.2f}%\n")
    
    # 4. Detailed classification report
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # 5. Confusion matrix
    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    labels = np.unique(y_train)
    cm_df = pd.DataFrame(cm, index=labels, columns=labels)
    print(cm_df)
    
    # 6. 5-Fold Cross Validation on Training Data
    cv_scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"\n5-Fold Cross-Validation Scores: {[round(s, 4) for s in cv_scores]}")
    print(f"Mean CV Accuracy: {cv_scores.mean() * 100:.2f}% (+/- {cv_scores.std() * 100:.2f}%)")
    print("=" * 60)
    
    return model, acc


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
