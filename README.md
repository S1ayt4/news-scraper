# News Scraper 📰

A simple Python scraper that collects the latest headlines from Hacker News and saves them to a JSON file. This project is a great starting point for anyone learning web scraping and working with Python.

## Features ✨
- Scrapes titles from Hacker News (https://news.ycombinator.com)
- Saves the titles and URLs in a `output.json` file
- Runs entirely in Python with **requests** and **BeautifulSoup**

## Requirements 📋
- Python 3.x
- Internet connection (for scraping)
- [GitHub Codespaces](https://github.com/codespaces) (optional, for easy setup)

## Installation 🔧
To get started, clone this repository to your local machine or open it directly in GitHub Codespaces:

```bash
git clone https://github.com/YOUR_USERNAME/news-scraper.git
cd news-scraper
Install dependencies
In your terminal, install the required Python libraries with the following command:
pip install -r requirements.txt
Usage 🚀
Once you have the dependencies installed, you can run the scraper using Python:
python scraper.py
The scraper will:

Retrieve the latest headlines from Hacker News

Save them in a output.json file in the same directory

You should see an output like:
✅ Scraping complete. Results saved in output.json
Project Structure 🗂
scraper.py: The main Python script that does the scraping.

requirements.txt: Lists the dependencies required to run the scraper (requests, beautifulsoup4).

Dockerfile: If you want to run the scraper in a Docker container.

output.json: Where the scraped data is saved.

Contributing 🤝
Feel free to fork this repository, open an issue, or submit a pull request. Contributions are welcome!

License 📝
This project is licensed under the MIT License - see the LICENSE file for details.

Contact 📬
If you have any questions or feedback, feel free to contact me through GitHub
