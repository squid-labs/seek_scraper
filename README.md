## Job Scraper for Indeed

This project consists of two Python scripts designed to scrape job listings from Seek

## Files:
1. Main.py
2. scraper_utils.py

## Setup:
1. Install the required dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   
   ```
2. Ensure you have Chrome driver is installed on your system.

## Usage:

1. main.py:
   This is the main script that you'll run to scrape job listings.

   - It's currently set up to search for "Banker" jobs in "Melbourne", Australia.
   - The script will create a 'csv_files' directory in the same location as the script.
   - The scraped job data will be saved as a CSV file in this directory.

   To run:
   ```bash
   
   python main.py

   ```
   
   To modify the search parameters, edit the following variables in the main() function:
   - country = australia  (Choose from the list of country variables at the top of the script)
   - job_position = 'Banker'
   - job_location = 'Melbourne'
   - date_posted = 10  (Number of days to look back)

2. scraper_utils.py:
   This script contains utility functions used by main.py. It includes functions for:
   - Configuring the webdriver
   - Searching for jobs
   - Scraping job data
   - Cleaning and sorting the scraped data

   You don't need to run this script directly, but you can modify its functions to change how the scraping works.

Output:
The script will create a CSV file named in the format:
{job_position}_{job_location}_{current_date}.csv

This file will contain the following information for each job listing:
- Link
- Job Title
- Company
- Date Posted
- Location
- Job Description
- Salary
- Search Query

