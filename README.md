# Overview

This repository holds example source code for Python unit testing using **pytest**.

## Bring-Up
1. Open terminal & navigate to the top-level folder of the repo
2. Create a virtual environment (aka venv):
   ```
   $ python -m venv .venv-python-testing
   ```
3. Activate venv:
   ```
   $ source .venv-python-testing/bin/activate
   ```
4. Install necessary modules:
   ```
   pip install -r requirements.txt
   ```
5. Navigate to the *code* folder
6. Execute the following command:
   ```
   $ pip install -e .
   ```
7. Download necessary test data:
   1. Make the download script executable:
   ```
   $ chmod +x data/download_test_data.sh
   ```
   1. Download test data (uses **gdown**):
   ```
   ./data/download_test_data.sh
   ```

Great! You are ready to start testing.

## Repository Overview
The repository is partitioned into 2 main folders:
* code
* data

### Code Folder
**code** folder stores all the actual source code (classes and corresponding tests).
**code/modules** stores classes' code.
**code/tests** stores tests for the classes.

### Data Folder
**data** folder stores all data necessary for running the tests. The moment you clone the repo it holds only the download script.
It's good practice not to store data in the repo, since it can will increase the repository size, especially if you use binary files.

## Running All Tests
If you want to run all tests that are present in the *code* folder you simply run:
```
$ pytest code
```

If you want pytest to be a little more verbose you can use the *-v* switch:
```
$ pytest code -v
```

## Selecting Test By Node ID
You can specify which tests to run based on their location withing Python modules.

Example #1 (selecting just one test):
```
pytest code/tests/test_basics.py::test_simple_assertions
```

Example #2 (selecting more tests)
```
pytest code/tests/test_basics.py::test_simple_assertions code/tests/test_basics.py::test_advanced_assertions
```

## Selecting Tests By Keyword
You can select which tests get executed using a keyword in their names by using the *-k* flag and providing a part or entire name of the test function:
```
$ pytest code -k 'init'
```

or

```
$ pytest code -k 'test_class1_init'
```

## Selecting Tests By Mark
Pytest has a neat feature of marking tests. You can use some built-in markers, but it's best to define your own custom markers in the **pytest.ini** file.
If you have tests marked with various markers you can execute only those, which have a specific mark.

Example:
```
$ pytest code -m 'mark1'
```

You can also select more than one marker or mix and match them using 'or', 'and' and 'not' keywords.

Example #1:
```
$ pytest code -m 'mark1 or mark2'
```

Example #2:
```
$ pytest code -m 'mark1 and mark2'
```

Example #3:
```
$ pytest code -m 'mark1 and not mark2'
```
