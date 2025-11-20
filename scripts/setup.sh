#!/bin/bash

# Ensure uv is available
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed. Please install it first:"
    echo "pip install uv"
    exit 1
fi

# Create or update virtual environment
echo "Creating/updating virtual environment..."
uv venv .venv

# Activate virtual environment based on shell
if [[ "$SHELL" == */zsh ]]; then
    source .venv/bin/activate
elif [[ "$SHELL" == */bash ]]; then
    source .venv/bin/activate
else
    echo "Please activate the virtual environment manually:"
    echo "source .venv/bin/activate"
fi

# Install dependencies
echo "Installing dependencies with uv..."
uv pip install -e ".[dev]"

# Install pre-commit hooks
echo "Setting up pre-commit hooks..."
pre-commit install

echo "Setup complete! Virtual environment is ready." 