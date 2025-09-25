This is a small Python project where I scrape news headlines from The Hindu website and save them into a text file. It’s basically a way to grab the latest headlines without manually opening the site every time.

   What it does

Connects to The Hindu homepage.

Collects the headlines shown there.

Saves them neatly in a file called Headlines.txt.

  What you need

Before running the script, you’ll need:

Python 3 installed on your system

A couple of libraries:

pip install requests beautifulsoup4


That’s all.

  How to run it

Download or clone this project.

Open a terminal in the project folder.

Run:

web_scrapper.py


After it runs, open the output.txt file — your headlines will be waiting there.

  Things to keep in mind

Sometimes the website changes its structure, and then the code might return 0 headlines. In that case, just update the BeautifulSoup tag/class selectors in the script.

Be mindful that scraping too often or too heavily isn’t polite — this script just does a light scrape for learning purposes.
