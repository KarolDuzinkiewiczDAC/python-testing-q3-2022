#!/bin/bash

# stop on first error from executed commands
set -e

echo ""
echo "Extracting tests folder path..."

# get the abolute path of the folder in which the script is located to make the script work when executed from any location (e.g. ./tests/run_unit_tests.sh or ./run_unit_tests.sh)
DATA_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Tests folder path: ${DATA_DIR}"
echo "Extracting tests folder path DONE."

echo "Cleaning up data folder..."
find ${DATA_DIR} -name "*.yaml" -type f -delete
echo "Cleaning up data folder DONE"

echo ""
echo "Downloading test data..."

gdown 1PYHvZa2vFrjl22bBS7TPRprpe28WGnHF -O ${DATA_DIR}/config.yaml

echo ""
echo "Downloading test data DONE"
