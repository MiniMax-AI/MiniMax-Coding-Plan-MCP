#!/bin/bash

# Check if environment argument is provided
if [[ $# -lt 1 ]]; then
    echo "Usage: $0 [test|prod]"
    exit 1
fi

# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build the package
uv build

if [ "$1" = "test" ]; then
    uv run twine upload --repository testpypi dist/* --verbose
elif [ "$1" = "prod" ]; then
    uv run twine upload --repository pypi dist/*
else
    echo "Please specify 'test' or 'prod' as the argument"
    exit 1
fi