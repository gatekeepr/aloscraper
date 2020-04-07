# Aloscraper
Download courses from alomoves.com automatically.

## Installation

1. ```pip3 install selenium tqdm```
2. Download Chrome Webdriver according to your Version (probably 80) [HERE](https://chromedriver.chromium.org/downloads) and place into your working folder next to the .py (or add it to your PATH)
3. Make sure you have a valid alomoves account on hand (2 week test accounts are fine).
4. Place the links of courses you want to download in **downloadlinks.txt**, one per line.
    - Example: https://www.alomoves.com/series/COURSENAME/workouts
    - You find these links by navigating to the course page and find the one where all the individual videos are shown with thumbnails.

## Usage
1. ```python3 downloader.py```
2. Enter your credentials in the terminal when asked.
3. After login just wait and the downloads will begin automatically.
4. You can minimize the browser and watch the console for progress.

              __
          ___( o)>
          \ <_. )
           `---'  for s