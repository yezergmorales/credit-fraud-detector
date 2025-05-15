# Credit Fraud || Dealing with Imbalanced Datasets

This project is a simple example of how to deal with imbalanced datasets using Python.

## Motivation

- Understand the little distribution of the "little" data that was provided to us.
- Create a 50/50 sub-dataframe ratio of "Fraud" and "Non-Fraud" transactions. (NearMiss Algorithm)
- Determine the Classifiers we are going to use and decide which one has a higher accuracy.
- Create a Neural Network and compare the accuracy to our best classifier.
- Understand common mistaked made with imbalanced datasets.

## Credit Card Fraud Detection Dataset

It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

Content
The dataset contains transactions made by credit cards in September 2013 by European cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification.

## Dependencies

uv installation
uv is a single command line executable. There are a number of ways to install it, but the easiest is to use the provided installation script:

```console
# Windows
# probably it is needed to deactivate Windows Defender or antivirus
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
$env:Path = "C:\Users\your_user\.local\bin;$env:Path"

# MacOS & Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

uv commands
```console
# Create a .venv with uv
# modify pyproject.toml whether is needed
uv sync

# Update the project’s environment
uv sync 

# Add dependencies to your `pyproject.toml` with the uv add command. 
uv add 'requests==2.31.0'
uv add make

# Add a git dependency
uv add git+https://github.com/psf/requests

# To remove a package, you can use uv remove:
uv remove requests
```

How to use uv to execute your script?
```console
$ uv run src\my_package\main.py 
(Linux) $ uv run src/my_package/main.py
Hello world
```

## Using Ruff and MyPy

Ruff is already in pyproject.toml
```console
ruff check                          # Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py  # Lint `file.py`.
ruff check @arguments.txt           # Lint using an input file, treating its contents as newline-delimited command-line arguments.
```
MyPy can be used as a VSCode extension

## Tests

Run the tests in cmd
```console
pytest tests/
```


