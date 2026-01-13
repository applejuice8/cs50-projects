
# YouTube Scraper using Flask & Selenium
#### Video Demo: https://youtu.be/CEibfnDyYTk
#### Description:
A simple web application built using **Flask**, **Selenium**, **HTML**, **CSS** and **JavaScript** that scrapes videos from a YouTube channel (e.g. `https://www.youtube.com/@channel/videos`) and displays them in a table. Users can also export them to a CSV file.

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Web Scraping**: Selenium (Python)

---

## Project Structure

```
project/
│
├── templates/
│   └── base.html
│   └── index.html
│   └── loading.html
│   └── results.html
│
├── static/
│   └── script.js
│   └── styles.css
│   └── youtube.svg
│   └── favicon.ico
│
├── app.py
├── scraper.py
└── requirements.txt
```

---

## Files
### app.py
- Manages the routing of the web application
- Renders the appropriate HTML templates accordingly
- Uses the `Scraper` class from `scraper.py` to extract data

### scraper.py
- Contains the code for all scraping logic behind this web application
- Defines the `Scraper` class that automates Chrome with Selenium
- Extract video details and export them into `youtube.csv`
- Exported and used in `app.py`

### requirements.txt
- Lists down all Python packages required to run this program
- Install all dependencies using the `pip install -r requirements.txt` command

### templates/
#### base.html
- Elements shared across all templates, including the head tag, CSS file and JavaScript file

#### index.html
- Contains code for the home page of the web application

#### loading.html
- A minimalistic loading page displayed to users when the scraping process is in progress

#### results.html
- Used Jinja templates (Loops and if statements) to display the scraped data

### static/
#### script.js
- Used to validate the URL entered by users to ensure the URL is supported
- Prevents form submission if the URL entered by users is invalid

#### styles.css
- Applied styles to all elements in this project
- Imported the Open Sans font-family from Google Fonts
- Utilize the :root selector to store colours in variables
- Utilize the ::-webkit-scrollbar and ::-webkit-scrollbar-thumb selectors to style the scrollbar

#### youtube.svg
- Used as the logo of the project

#### favicon.ico
- Icon displayed in the browser tab

## Design Choices
- Used the svg format of YouTube logo, due to the scalable nature of svg files
- Remove the head tags from individual files and placed them into a centralized `base.html` file
- Created a separate template `loading.html` to notify users that the scraping process is in progress
- Display the extracted information in a table, for clear readability
- Added the option to receive the extracted data in the form of csv file, for easier data management
- Utilized Object-Oriented Programming principles by creating a `Scraper` class to group scraping-related functions together
- Separated the `Scraper` class into a separate Python file, to enhance clarity and facilitate the debugging process
- Utilized color variables in CSS to improve reusability
- Validate the form using JavaScript for server-side validation, on top of the client-side validation in HTML
