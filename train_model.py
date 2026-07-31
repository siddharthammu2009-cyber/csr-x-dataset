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
        filepath = os.path.join("stars_dataset.csv")
    
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
    feature_cols = ['I_magnitude','period_days','I_band_amplitude','V_minus_I_color']
    X = df[feature_cols]
    y = df['star_type']
    return X,y
    


def split_data(X, y):
    """
    Task 2: Split X and y into 80% training set and 20% testing set using random_state=42.
    
    Use scikit-learn's `train_test_split` function.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
    return X_train, X_test, y_train, y_test
    


def train_and_evaluate_model(model, model_name, X_train, X_test, y_train, y_test):
    """
    Task 3: Train model on training data, evaluate on testing data, print metrics,
    and compute 5-fold cross-validation scores.
    """
    print("\n" + "=" * 60)
    print(f"  Training Model: {model_name}")
    print("=" * 60)
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {acc * 100:.2f}%\n")

    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    

    cv_scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"5-Fold Cross-Validation Scores: {cv_scores}")
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
