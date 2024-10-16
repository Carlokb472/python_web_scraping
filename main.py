import requests as req
from openpyxl import Workbook


header = {
    "user-agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}

# Create a new Excel workbook
wb = Workbook()
ws = wb.active


ws.append(['Course Title', 'Course Owner','Price', 'Pre Ordered Price','Number of Sold'])

for page in range(3):

    url = f"https://api.hahow.in/api/products/search?category=COURSE&limit=24&page={page}&query=python&sort=RELEVANCE"
    response = req.get(url,headers = header)
    print(response)
    if response.status_code == 200:
        data = response.json()
        # Print the entire response to see its structure
        print(f"Response for page {page}: {data}")

        # Check if 'products' key exists in the response
        if 'products' in data['data']['courseData']:
            # Process course data
            for courseData in data['data']['courseData']['products']:
                course = []
                course.append(courseData.get('title', 'N/A'))
                course.append(courseData['owner'].get('name', 'N/A'))
                course.append(courseData.get('price', 'N/A'))
                course.append(courseData.get('preOrderedPrice', 'N/A'))
                course.append(courseData.get('numSoldTickets', 'N/A'))

                # Append course data to the Excel sheet
                ws.append(course)
        else:
            print(f"'products' key not found in the response for page {page}")
    else:
        print(f"Failed to retrieve data for page {page}: Status code {response.status_code}")

wb.save('python_courses.xlsx')