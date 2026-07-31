# Machine Learning Model Building with Scikit-Learn (`model_building`)

---

## 1. Overview & Learning Objectives

Now that you have cleaned and preprocessed the raw OGLE-III variable star dataset into `stars_dataset.csv`, it is time to build your first **Machine Learning Model** in Python.

In this assignment, you will use **`scikit-learn`**—the industry standard Python library for machine learning—to build supervised classification models that predict star types based on physical light curve parameters.

By completing this assignment, you will learn:
1. How machine learning models format data into a **Feature Matrix ($X$)** and **Target Vector ($y$)**.
2. Why we split data into **Training** and **Testing** sets (`train_test_split`).
3. How to instantiate, train (`.fit()`), and evaluate (`.predict()`) a **Decision Tree** and a **Random Forest**.
4. How to evaluate model performance using **Accuracy**, **Precision**, **Recall**, **F1-Score**, and **Confusion Matrices**.
5. How to perform **5-Fold Cross-Validation** (`cross_val_score`) to test model stability.

---

## 2. Background: What is Scikit-Learn?

**`scikit-learn`** (imported in Python as `sklearn`) is a tool kit for machine learning algorithms. Every supervised machine learning workflow in scikit-learn follows 5 fundamental steps:

```text
1. Prepare Data (X, y)   ==>   2. Split Train/Test   ==>   3. Instantiate & Fit Model
                                                                    │
5. Cross-Validation      <==   4. Predict & Evaluate  <─────────────┘
```

---

## 3. Scikit-Learn API Concept & Syntax Reference Sheet

> [!NOTE]
> Read this reference section carefully! It contains all the concepts and syntax formulas you will need to complete the `# TODO` sections in `train_model.py`.

### Concept 1: Feature Matrix ($X$) vs Target Vector ($y$)
In machine learning:
- **Features ($X$)**: The numerical measurements used to make predictions. In our dataset, these are:
  - `I_magnitude`: Average brightness in $I$-band
  - `period_days`: Pulsation or orbital period in days
  - `I_band_amplitude`: Range of brightness variation
  - `V_minus_I_color`: $V - I$ color index (representing star temperature)
- **Target ($y$)**: The category label we want the model to predict (`star_type`).

#### Syntax Example:
```python
feature_cols = ['feature1', 'feature2', 'feature3']
X = df[feature_cols]   # DataFrame containing 2D table of numbers
y = df['target_column'] # 1D Series containing target labels
```

---

### Concept 2: Train / Test Split (`train_test_split`)
If you test a machine learning model on the exact same data it trained on, it can cheat by memorizing the answers (known as **overfitting**). 

To measure real-world performance, we split our data:
- **Training Set (80%)**: Used by the model to learn patterns.
- **Testing Set (20%)**: Held out to test predictions on unseen data.

#### Syntax Example:
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
*(Passing `random_state=42` ensures that the random split is reproducible every time you run the script!)*

---

### Concept 3: The 3 Core Model Methods (`fit`, `predict`, `score`)

In scikit-learn, every classifier object uses the exact same 3 method calls:

```python
# 1. Fit (Train model on training data)
model.fit(X_train, y_train)

# 2. Predict (Generate predictions for unseen test data)
y_pred = model.predict(X_test)

# 3. Calculate Accuracy
acc = accuracy_score(y_test, y_pred)
```

---

### Concept 4: Evaluation Metrics

#### A. Accuracy Score
The fraction of predictions the model got right out of the total:
$$\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}}$$

#### B. Classification Report (`classification_report`)
Prints detailed metrics for each star category:
- **Precision**: Out of all stars predicted as *Cepheids*, how many were actually *Cepheids*?
- **Recall**: Out of all real *Cepheids* in the test set, how many did the model correctly identify?
- **F1-Score**: The harmonic mean of Precision and Recall.

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

#### C. Confusion Matrix (`confusion_matrix`)
A table showing where the model gets confused between categories (e.g. mistaking an Eclipsing Binary for an RR Lyrae star).

---

### Concept 5: 5-Fold Cross-Validation (`cross_val_score`)
Instead of testing on a single test split, **5-Fold Cross-Validation** splits the training set into 5 equal slices (folds), trains on 4 folds, tests on the 5th fold, and repeats this 5 times. 

```python
from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(model, X_train, y_train, cv=5)
print("5-Fold Scores:", cv_scores)
print("Mean Accuracy:", cv_scores.mean())
```

---

## 4. Guided Implementation Walkthrough

Open `train_model.py`. You will see three functions containing `# TODO` blocks and `raise NotImplementedError`. Your task is to complete all three functions using the concept reference guide above!

---

### Task 1: Complete `prepare_features_and_target(df)`

1. Create a list called `feature_cols` containing: `['I_magnitude', 'period_days', 'I_band_amplitude', 'V_minus_I_color']`.
2. Extract $X$ by selecting `df[feature_cols]`.
3. Extract $y$ by selecting `df['star_type']`.
4. Return `X, y`.

---

### Task 2: Complete `split_data(X, y)`

1. Call `train_test_split(X, y, test_size=0.2, random_state=42)`.
2. Return the 4 variables: `X_train, X_test, y_train, y_test`.

---

### Task 3: Complete `train_and_evaluate_model(model, model_name, X_train, X_test, y_train, y_test)`

1. **Train Model**: Call `model.fit(X_train, y_train)`.
2. **Make Predictions**: Call `y_pred = model.predict(X_test)`.
3. **Compute Accuracy**: Compute `accuracy_score(y_test, y_pred)` and print it.
4. **Print Classification Report**: Call `classification_report(y_test, y_pred)` and print the output.
5. **Cross-Validation**: Call `cross_val_score(model, X_train, y_train, cv=5)` and print the mean CV score and standard deviation.

---

## 5. Testing Your Assignment Script

Run your completed script in the terminal:
```bash
python train_model.py
```

### Expected Output:
```text
Loading dataset from: data/stars_dataset.csv
Dataset loaded successfully with 5933 rows and 5 columns.

Extracting features and target...

Splitting dataset into train and test sets...
Training set size: 4746 samples
Testing set size:  1187 samples

============================================================
  Training Model: Decision Tree Classifier
============================================================
Test Accuracy: 98.99%

Classification Report:
                  precision    recall  f1-score   support

         Cepheid       1.00      0.99      1.00       324
Eclipsing Binary       0.97      0.99      0.98       296
            Mira       1.00      0.99      1.00       282
        RR Lyrae       0.99      0.99      0.99       285

        accuracy                           0.99      1187

5-Fold Cross-Validation Scores: [0.9863, 0.9852, 0.9884, 0.9916, 0.9863]
Mean CV Accuracy: 98.76% (+/- 0.22%)
============================================================

============================================================
  Training Model: Random Forest Classifier
============================================================
Test Accuracy: 99.07%

Mean CV Accuracy: 99.07% (+/- 0.26%)
============================================================
```

Congratulations! You have built and evaluated your first machine learning models using Scikit-Learn.
