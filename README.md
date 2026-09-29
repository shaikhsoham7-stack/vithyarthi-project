# vithyarthi-project
A  Python-based bioinformatics project that analyzes DNA sequences. It validates nucleotide bases, calculates nucleotide composition and GC content, generates the complementary sequence, and performs DNA-to-mRNA transcription using basic Python programming concepts.
# DNA Sequence Analyzer

## 1. Overview

DNA has four parts called nucleotide bases

- A = Adenine

- T = Thymine

- G = Guanine

- C = Cytosine

This project gets a DNA sequence from the person using it and does basic things with it

The project uses simple Python ideas instead of complicated. Machine learning

## 2. Features

### Module 1: Sequence Input and Validation

- Takes a DNA sequence

- Changes lower case letters to upper case

- Checks if only A T G and C are there

- Does not accept sequences

### Module 2: Sequence Analysis

- Finds how long the sequence is

- Counts A T G and C

- Figures out GC content

- Figures out AT content

### Module 3: Sequence Operations

- Finds the complement

- Finds the reverse

- Finds the complement

### Testing

The project has tests for validation analysis and sequence operations

## 3. Technologies Used

- Python 3

- Python standard library

- unittest

- Git and GitHub

No extra Python programs are needed

## 4. Project Structure

```text

DNA-Sequence-Analyzer/

│

├── main.py

├── validator.py

├── analyzer.py

├── sequence_operations.py

├── utils.py

├── requirements.txt

│

├── data/

│   └── sample_sequences.txt

│

├── tests/

│   ├── test_validator.py

│   ├── test_analyzer.py

│   └── test_operations.py

│

├── README.md

└── statement.md

```

## 5. Requirements

Install Python 3 on your computer

Check if Python is installed

```bash

python --version

```

If that does not work on Windows try

```bash

py --version

```

## 6. How to Run

Open the project folder in VS Code

Open the terminal and type

```bash

python main.py

```

On some Windows systems type

```bash

py main.py

```

The program will show a menu

## 7. Example

```text

================================

DNA SEQUENCE ANALYZER

================================

1. Enter DNA Sequence

2. Validate Sequence

3. Analyze Sequence

4. Find Complement

5. Find Reverse

6. Find Reverse Complement

7. Exit

Enter your choice: 1

Enter DNA sequence: ATGCATGC

Sequence saved successfully.

```

Then choose analysis

```text

--- Sequence Analysis ---

Sequence      : ATGCATGC

Length        : 8

A count       : 2

T count       : 2

G count       : 2

C count       : 2

GC content    : 50.00%

AT content    : 50.00%

```

## 8. Running Tests

From the project folder type

```bash

python -m unittest discover -s tests -p "test_*.py"

```

If using the Windows Python launcher type

```bash

py -m unittest discover -s tests -p "test_*.py"

```

A successful test run should show something like

```text

.........

----------------------------------------------------------------------

Ran 9 tests in...

OK

```

## 9. Basic GitHub Setup

### Step 1: Create a GitHub account

Go to GitHub and make an account if you do not have one

### Step 2: Install Git

Install Git for Windows

Check installation

```bash

git --version

```

### Step 3: Configure Git

Change the example details to your own

```bash

git config --global user.name "Your Name"

git config --global user.email "your@email.com"

```

### Step 4: Open the project folder

Open the terminal in the project folder

Type

```bash

git init

```

### Step 5: Add files

Type

```bash

git add.

```

### Step 6: Make the commit

Type

```bash

git commit -m "Initial DNA Sequence Analyzer project"

```

### Step 7: Create a GitHub repository

Make a new empty repository called

```text

DNA-Sequence-Analyzer

```

Do not add another README if you already have the README in this project folder

### Step 8: Connect the local project

GitHub will give you commands for your repository. They will look like

```bash

git remote add origin YOUR_REPOSITORY_URL

git branch -M main

git push -u origin

```

Use the exact repository URL from GitHub

## 10. Future Enhancements

Possible future changes include

- Reading sequences from FASTA files

- RNA transcription

- Finding simple patterns

- Finding start and stop codes

- Saving analysis results

- Adding a graphical user interface

These are future changes and not needed for the basic version

## 11. Educational Note

This project is, for learning programming and basic bioinformatics ideas. It should not be used for diagnosis or making medical decisions
