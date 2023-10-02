# Working with Python: Assessment Test

## Introduction

This project involves basic data manipulation with JSON files, focusing on tasks related to data processing of the MASSive dataset and file management. 

## Table of Contents

- [Project Tasks/Features](#features)
   - [Question 1 - Python3 Development Environment](#question-1-python3-development-environment)
   - [Question 2 - Working with Files](#question-2-working-with-files)
- [Installation](#installation)
   - [Pre-requisites](#pre-requisites)
   - [Installation Instructions](#installation-instructions)

## Project Tasks/Features<a name="features"></a>
### Question 1 - Python3 Development Environment<a name="question-1-python3-development-environment"></a>
In this section, you will set up the Python3 development environment and process the MASSIVE Dataset:

**Task 1**: Set up a Python3 development environment and install necessary dependencies.
**Task 2**: Create a project structure similar to PyCharm and import the dataset.
**Task 3**: Generate "en-xx.xlxs" files for all languages, using id, utt, and annot_utt fields.
**Task 4**: Avoid using recursive algorithms with high time complexity.
**Task 5**: Refer to Flags for running the solution on generator.sh files.

### Question 2 - Working with Files<a name="question-2-working-with-files"></a>
In this section, you will work with JSON files and manage your project:

**Task 1**: Generate separate JSONL files for English (en), Swahili (sw), and German (de) for test, train, and dev data sets.
**Task 2**: Create a large JSON file that includes all translations from English (en) to other languages (xx) for the train sets, including id and utt fields.
**Task 3**: Ensure the JSON file structure is pretty-printed.
**Task 4**: Upload all generated files to your Google Drive Backup Folder.

## Installation<a name="installation"></a>

### Pre-requisites<a name="pre-requisites"></a>

Before you begin, make sure you have the following pre-requisites installed on your system:

- [Python3 Development Environment](https://www.python.org/)

### Installation Instructions<a name="installation-instructions"></a>

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Arnie1x/massive-dataset-lab.git
   cd massive-dataset-lab
   ```
2. Setup a virtual environment
   ```bash
   virtualenv venv
   ```
3. Import the MASSive dataset to the dataset folder
   The MASSive dataset can be found [here](https://github.com/alexa/massive/) together with the installation instructions.

3. Install all the required dependencies needed to run the project
   ```bash
   python -r pip install requirements.txt
   ```


   
