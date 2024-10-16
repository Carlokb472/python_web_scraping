# python_web_scraping
Python Web Scraping: Fetching Course Data and Exporting to Excel
This project demonstrates a Python web scraping script that fetches course data from an API and exports it to an Excel file. The data includes course titles, owners, prices, pre-order prices, and the number of units sold. The script retrieves data from multiple pages and stores it in an Excel file using the openpyxl library.

Requirements
Python 3.x
requests library for making HTTP requests
openpyxl library for handling Excel files
# Setup
# 1. Install the required libraries
Before running the script, make sure you have the required libraries installed. You can install them using pip:
# pip install requests openpyxl

# pip install requests openpyxl
# 2. Clone or Download the Project
You can clone the project using the following command or download it from the repository:
# git clone <repository-url>

# 3. Running the Script
The script fetches course data from a public API and saves it into an Excel file named python_courses.xlsx. Each page of data is fetched in the loop, and the resulting data is appended to the Excel sheet.

To run the script, execute the following command:
# python main.py

# python main.py
#4. Expected Output
The output of the script will be an Excel file named python_courses.xlsx. The file will contain the following data columns for each course:

Course Title
Course Owner
Price
Pre-Ordered Price
Number of Sold Units
# 5. API Used
The script uses the following API endpoint to retrieve course data related to Python:

https://api.hahow.in/api/products/search?category=COURSE&limit=24&page={page}&query=python&sort=RELEVANCE
The script queries 3 pages of data, with each page containing 24 courses.

# 6. Handling Errors
If the API request fails, an error message will be printed to the console, specifying the status code.
If the expected data (products key) is missing from the API response, an error message will be logged, indicating the issue.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code.
