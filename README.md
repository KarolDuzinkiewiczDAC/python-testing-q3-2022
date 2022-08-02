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
5. Download necessary test data:
   1. Make the download script executable:
   ```
   $ chmod +x data/download_test_data.sh
   ```
   2. Download test data (uses **gdown**):
   ```
   ./data/download_test_data.sh
   ```

Great! You are ready to start testing.
