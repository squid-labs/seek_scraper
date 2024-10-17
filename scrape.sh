#!/bin/bash

# Execute all Python scripts except *_scraper_utils.py
for file in *.py; do
    if [[ "$file" != *_scraper_utils.py ]]; then
        echo "Executing: $file"
        python "$file"

        # Calculate a random delay between 1 and 5 seconds
        delay=$((1 + RANDOM % 5))
        echo "Waiting for $delay seconds..."
        sleep $delay
    fi
done

# Change directory to csv_files
cd csv_files || exit

# Get the current date and time
dtg=$(date +"%Y-%m-%d_%H-%M-%S")

# Merge all CSV files into one with date and time appended
cat *.csv > "merge_JOB_$dtg.csv"

# Print completion message
echo "All CSV files have been merged into merge_JOB_$dtg.csv"
