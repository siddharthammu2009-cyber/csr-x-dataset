# Terminal Commands, Git & GitHub Codespaces Setup Guide

---

## 1. Overview

This guide introduces essential **Terminal Commands**, **Python Environments**, and **Git Workflows** tailored for working in **GitHub Codespaces**.

When working in GitHub Codespaces, you are using a cloud-hosted Linux environment running Visual Studio Code.

To open the terminal inside GitHub Codespaces:
- Press **`Ctrl + ~`** (Windows/Linux) or **`Cmd + ~`** (macOS).
- Or click **Terminal $\rightarrow$ New Terminal** in the top menu bar.

---

## 2. Essential Terminal Navigation Commands

When using the terminal, you navigate directories (folders) and inspect files using text commands instead of clicking with a mouse:

| Command | Full Name | What It Does | Example Usage in Codespaces |
|---|---|---|---|
| `pwd` | **P**rint **W**orking **D**irectory | Displays the absolute folder path you are currently inside. | `pwd` $\rightarrow$ `/workspaces/csr-x` |
| `ls` | **L**i**s**t | Lists all files and subfolders in your current folder. Use `ls -la` to see hidden files. | `ls` or `ls -la` |
| `cd` | **C**hange **D**irectory | Navigates into a target folder, up one level (`cd ..`), or back home (`cd ~`). | `cd model_building`, `cd ..` |

### Step-by-Step Terminal Walkthrough:

```bash
# 1. Print current working directory path
pwd

# 2. List all files and folders in the workspace
ls

# 3. Navigate into the assignment directory
cd model_building

# 4. Verify your current folder location
pwd

# 5. Move back up to the root project directory
cd ..
```

---

## 3. Python Virtual Environments & Package Management

### A. Working in GitHub Codespaces
GitHub Codespaces automatically manages isolated Python environments for you. To install or update project dependencies (`pandas`, `scikit-learn`, `matplotlib`, `seaborn`), run:

```bash
pip install -r requirements.txt
```

### B. Creating a Local Virtual Environment (`venv`)
If you ever run Python on your own local laptop outside of Codespaces, you should create a virtual environment (`venv`) to keep your project packages isolated:

```bash
# 1. Create a virtual environment named 'venv'
python3 -m venv venv

# 2. Activate the virtual environment:
# On macOS / Linux / GitHub Codespaces:
source venv/bin/activate

# On Windows (PowerShell):
venv\Scripts\activate

# (Notice (venv) appears at the beginning of your terminal prompt!)

# 3. Install required packages into the active venv
pip install -r requirements.txt

# 4. Deactivate when finished
deactivate
```

---

## 4. Essential Git Workflow (Saving & Pushing to GitHub)

Git tracks changes to your code and allows you to sync snapshots to your GitHub repository. Follow this standard 4-step Git workflow:

```text
1. git status  ==>  2. git add .  ==>  3. git commit -m "msg"  ==>  4. git push
(Check changes)     (Stage files)        (Save snapshot)           (Upload to GitHub)
```

### Step-by-Step Git Commands:

1. **`git status`**: See which files have been modified, created, or deleted.
   ```bash
   git status
   ```

2. **`git add .`**: Stage all modified and new files to prepare them for a snapshot.
   ```bash
   git add .
   ```

3. **`git commit -m "your message"`**: Save a local snapshot of staged files with a clear comment.
   ```bash
   git commit -m "Completed scikit-learn model building assignment"
   ```

4. **`git push`**: Push your local commits to your remote GitHub repository.
   ```bash
   git push
   ```

---

## 5. Summary Reference Cheat Sheet

```bash
# === Navigation ===
pwd                    # Where am I?
ls                     # What files are here?
cd model_building      # Go into model_building folder
cd ..                  # Go up one folder

# === Python Packages ===
pip install -r requirements.txt  # Install required packages

# === Git Workflow ===
git status             # Check changed files
git add .              # Stage all changes
git commit -m "update" # Save local snapshot
git push               # Upload changes to GitHub
```
