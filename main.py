import csv
from dotenv import load_dotenv
from scraper_utils import *
from datetime import datetime

load_dotenv()

"""
List of countries url.
"""

hong_kong = 'https://hk.jobsdb.com/'
indonesia = 'https://id.jobstreet.com/'
malaysia = 'https://my.jobstreet.com'
philippines = 'https://www.jobstreet.com.ph/'
singapore = 'https://sg.jobstreet.com/'
thailand = 'https://th.jobsdb.com/'

def main():
    driver = configure_webdriver()
    country = malaysia
    job_position = ['Software Engineer', 'Senior Software Engineer', 'Lead Developer', 'Solution Architect', 'Software Architect']
    job_location = 'Kuala Lumpur'
    date_posted = 7

    # Create a subdirectory named 'csv_files' if it doesn't exist
    csv_dir = os.path.join(os.path.dirname(__file__), 'csv_files')
    os.makedirs(csv_dir, exist_ok=True)

    sorted_df = None

    try:
        for element in job_position:
            element, total_jobs = search_jobs(driver, country, element, job_location, date_posted)
            df = scrape_job_data(driver, country, element, total_jobs)

            if df.empty or df.shape[0] == 1:
                print("No results found. Something went wrong.")
                subject = 'No Jobs Found on Indeed'
                body = """
                No jobs were found for the given search criteria.
                Please consider the following:
                1. Try adjusting your search criteria.
                2. If you used English search keywords for non-English speaking countries,
                it might return an empty result. Consider using keywords in the country's language.
                3. Try more general keyword(s), check your spelling or replace abbreviations with the entire word

                Feel free to try a manual search with this link and see for yourself:
                Link {}
                """.format(driver.current_url)

                # You might want to send an email here with the subject and body
                
            else:
                cleaned_df = clean_data(df)
                sorted_df = sort_data(cleaned_df)
                
                # Check if there are any jobs before saving the CSV
                if not sorted_df.empty:
                    # Get current date
                    current_date = datetime.now().strftime("%Y-%m-%d")
                    
                    # Create filename with date
                    filename = f"seek_{element}_{job_location}_{current_date}.csv"
                    
                    # Full path for the CSV file
                    csv_file = os.path.join(csv_dir, filename)
                    
                    # Save the CSV file with specific parameters to prevent URL truncation
                    sorted_df.to_csv(csv_file, index=False, quoting=csv.QUOTE_ALL, escapechar='\\', encoding='utf-8-sig')
                    print(f"CSV file saved as {csv_file}")
                else:
                    print("No valid data to save.")
    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error quitting the driver: {e}")

if __name__ == "__main__":
    main()
