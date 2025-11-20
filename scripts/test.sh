#!/bin/bash

# Set default variables
COVERAGE=true
VERBOSE=false
FAIL_FAST=false

# Process command-line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --no-coverage)
      COVERAGE=false
      shift
      ;;
    --verbose|-v)
      VERBOSE=true
      shift
      ;;
    --fail-fast|-f)
      FAIL_FAST=true
      shift
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: ./test.sh [--no-coverage] [--verbose|-v] [--fail-fast|-f]"
      exit 1
      ;;
  esac
done

# Build the command
CMD="python -m pytest"

if [ "$COVERAGE" = true ]; then
  CMD="$CMD --cov=minimax_mcp"
fi

if [ "$VERBOSE" = true ]; then
  CMD="$CMD -v"
fi

if [ "$FAIL_FAST" = true ]; then
  CMD="$CMD -x"
fi

# Run the tests
echo "Running tests with command: $CMD"
$CMD 