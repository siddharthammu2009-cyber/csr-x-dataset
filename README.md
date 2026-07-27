## Preprocess Dataset (`cleanup`)

---

## 1. Overview & Objectives

Welcome to Project 0! In this project, you will write your first real-world data engineering pipeline in Python.

Astronomers observe millions of stars using telescopes and store raw data in text files. However, before any Machine Learning model can read this data, it must be cleaned, formatted, and transformed.

By completing this assignment, you will learn:
1. What **`pandas`** is and how to use it to work with tables of data.
2. How to convert text numbers into real decimal numbers (`floats`).
3. How to perform **Feature Engineering** (calculating a star's color/temperature from raw brightness values).
4. How to drop missing values (`NaN`) and balance data across categories.

---

## 2. Background: What is OGLE-III Data?

The **Optical Gravitational Lensing Experiment (OGLE-III)** is an astronomical survey that monitored tens of millions of stars in space. In this project, we are classifying four distinct physical types of variable stars:

1. **Cepheid**: Classical fundamental-mode pulsating giant stars used to measure cosmic distances across galaxies.
2. **RR Lyrae**: Ancient, low-mass pulsating stars commonly found in old star clusters.
3. **Mira**: Evolved, cool red super-giants undergoing massive thermal pulsations over hundreds of days.
4. **Eclipsing Binary**: Systems where two stars orbit each other, periodically blocking each other's light from Earth's view.

---

## 3. Getting Started

1. Download the distribution zip file and extract it into your workspace directory.
2. Open the project folder inside **GitHub Codespaces** or VS Code.
3. Open your terminal in VS Code (`Ctrl + ~` or `Cmd + ~`) and install the `pandas` library by running:
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Absolute Beginner's Primer: What is `pandas`?

In Python, **`pandas`** is a library built specifically for working with tabular data (like an Excel spreadsheet or SQL table). In pandas:
- A table of data is called a **DataFrame** (`df`).
- A single column in that table is called a **Series** (`df['column_name']` or `df[0]`).

### Key Concepts You Need to Know:

#### A. 0-Indexed Columns in Text Files
When `pandas` reads a file without column headers, it automatically names the columns using numbers starting from `0`:
- Column `0`: Star OGLE Identifier (e.g., `OGLE-LMC-CEP-0002`)
- Column `1`: $I$-band Magnitude (Infrared Brightness)
- Column `2`: $V$-band Magnitude (Visual Green Brightness)
- Column `3`: Pulsation/Orbital Period in days
- Column `5` or `6` (depending on star type): Brightness variation amplitude

#### B. What is `NaN`?
`NaN` stands for **Not a Number**. When telescopes record invalid readings, corrupted data, or missing measurements, pandas represents them as `NaN`.

---

## 5. Guided Implementation Walkthrough

Open `clean_data.py`. You will see two functions that say `raise NotImplementedError`. Your task is to replace `raise NotImplementedError` in both functions with working Python code!

---

### Task 1: Complete `clean_file(star_type, config)`

This function takes two inputs:
1. `star_type`: A string representing the class label (e.g., `"Cepheid"` or `"Mira"`).
2. `config`: A Python dictionary containing the file details:
   - `config["filename"]`: The file name (e.g., `"cepF.dat"`).
   - `config["amp_col"]`: The column index for amplitude (`5` or `6`).

#### Step-by-Step Code Instructions:

#### Step 1.1: Build the Filepath
Combine the folder path (`RAW_DIR`) and the filename (`config["filename"]`) using Python's `os.path.join`:
```python
filepath = os.path.join(RAW_DIR, config["filename"])
```

#### Step 1.2: Read the File into Pandas
Use `pd.read_csv()` to read the space-delimited text file into a DataFrame. Pass these exact arguments:
- `filepath`: The path variable you just created.
- `sep=r'\s+'`: Tells pandas that columns are separated by one or more spaces.
- `header=None`: Tells pandas that the file has no column names (so columns will be numbered `0, 1, 2, 3...`).
- `comment='#'`: Tells pandas to skip any comment lines starting with `#`.

```python
df = pd.read_csv(filepath, sep=r'\s+', header=None, comment='#')
```

#### Step 1.3: Convert Columns to Numbers (`pd.to_numeric`)
Raw text files store everything as text strings. We must convert them to decimal numbers (`floats`) using `pd.to_numeric()`. Adding `errors='coerce'` tells pandas: *"If you find bad text or corrupted numbers, turn them into `NaN` so we can drop them later."*

Convert the 4 required columns:
```python
i_mag = pd.to_numeric(df[1], errors='coerce')
v_mag = pd.to_numeric(df[2], errors='coerce')
period = pd.to_numeric(df[3], errors='coerce')
amplitude = pd.to_numeric(df[config["amp_col"]], errors='coerce')
```

#### Step 1.4: Calculate Star Color Index ($V - I$)
In astrophysics, a star's surface temperature is calculated by subtracting its $I$-band magnitude from its $V$-band magnitude ($V - I$ color). You can subtract pandas Series directly using the minus operator `-`:
```python
color_index = v_mag - i_mag
```

#### Step 1.5: Build a New Clean DataFrame
Create a new pandas DataFrame by passing a dictionary where the keys are string column names, and the values are the variables you created above. Also add a `'star_type'` column set to the `star_type` input parameter:

```python
clean_df = pd.DataFrame({
    'I_magnitude': i_mag,
    'period_days': period,
    'I_band_amplitude': amplitude,
    'V_minus_I_color': color_index,
    'star_type': star_type
})
```

#### Step 1.6: Drop Missing Values and Return
Call `.dropna()` on your `clean_df` to remove any rows containing `NaN` values, and return it:
```python
return clean_df.dropna()
```

---

### Task 2: Complete `balance_and_merge(dataframes, samples_per_class=1500)`

This function takes a list of DataFrames (`dataframes`) and an integer `samples_per_class` (default `1500`). 

Some star files have 26,000 stars, while Miras only have 1,433. If we don't balance them, our ML model will become biased toward Eclipsing Binaries!

#### Step-by-Step Code Instructions:

#### Step 2.1: Create a List for Balanced Data
Start by initializing an empty list to hold your sampled DataFrames:
```python
balanced_dfs = []
```

#### Step 2.2: Loop Through `dataframes`
Write a `for` loop to iterate through each DataFrame in `dataframes`:
```python
for df in dataframes:
```

#### Step 2.3: Check Length and Subsample
Inside the loop:
1. Check if the length of `df` (using `len(df)`) is greater than `samples_per_class`.
2. If `len(df) > samples_per_class`, use `df.sample(n=samples_per_class, random_state=42)` to randomly select 1,500 rows.
3. Otherwise, if `len(df) <= samples_per_class`, keep `df` as it is.
4. Append the DataFrame to your `balanced_dfs` list using `.append()`.

```python
if len(df) > samples_per_class:
    df_sampled = df.sample(n=samples_per_class, random_state=42)
else:
    df_sampled = df
balanced_dfs.append(df_sampled)
```

#### Step 2.4: Concatenate and Return
After the loop finishes, combine all DataFrames in `balanced_dfs` into one master DataFrame using `pd.concat()`, passing `ignore_index=True`, and return the result:

```python
return pd.concat(balanced_dfs, ignore_index=True)
```

---

## 6. Testing Your Script

Run your finished script in the terminal:
```bash
python clean_data.py
```

### Expected Output:
```text
Loading raw OGLE-III datasets...
Cleaning Cepheid data...
Cleaning RR Lyrae data...
Cleaning Mira data...
Cleaning Eclipsing Binary data...
Merging and balancing dataset...

============================================================
Data cleaning complete! Saved to data/processed/stars_dataset.csv
Total rows: 5933
Class distribution:
star_type
Cepheid             1500
RR Lyrae            1500
Eclipsing Binary    1500
Mira                1433
============================================================
```

Congratulations! You have created a clean dataset for machine learning.
