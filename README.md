# Python Web Scraping with BeautifulSoup

## 📌 Overview
This project demonstrates web scraping using Python and the BeautifulSoup (bs4) library. It shows how to fetch web pages, parse HTML, extract useful information, and save the scraped data.

## 🚀 Features
- Fetch web pages using the `requests` library
- Parse HTML using BeautifulSoup
- Extract:
  - Titles
  - Headings
  - Paragraphs
  - Links
  - Images
  - Tables
- Find elements by tag, class, and id
- Use CSS selectors
- Save scraped data to a CSV file

## 🛠 Technologies Used
- Python 3
- BeautifulSoup4
- Requests
- CSV

## 📂 Project Structure

```
Web-Scraping/
│── scraping.py
│── requirements.txt
│── README.md
```

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Web-Scraping.git
```

Move into the project directory

```bash
cd Web-Scraping
```

Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install beautifulsoup4 requests
```

## ▶️ Run the Program

```bash
python scraping.py
```

## 📖 Example

Input

```
https://quotes.toscrape.com/
```

Output

```
"The world as we have created it..."
Author: Albert Einstein

"It is our choices..."
Author: J.K. Rowling
```

## 📚 Concepts Covered

- HTTP Requests
- HTML Parsing
- BeautifulSoup
- find()
- find_all()
- CSS Selectors
- Attribute Extraction
- CSV File Handling

## 📄 License

This project is for educational purposes.
