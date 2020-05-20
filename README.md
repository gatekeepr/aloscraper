# Aloscraper

Download courses from <https://ww.alomoves.com> automatically.

## Installation

1. `pip3 install -r requirements.txt`
2. Download Chrome Webdriver according to your Version (probably 80) [HERE](https://chromedriver.chromium.org/downloads) and place into your working folder next to the .py (or add it to your PATH)
3. Make sure you have a valid alomoves account on hand (2 week test accounts are fine).
4. Place the links of courses you want to download in **downloadlinks.txt**, one per line.
   - Example: <https://www.alomoves.com/series/COURSENAME/workouts>
   - You find these links by navigating to the course page and find the one where all the individual videos are shown with thumbnails.

## Variables to set in sourcecode

- REDOWNLOAD: Set to true if you want to skip the check for existing paths to redownload courses (corrupt/missing files).
- BASEPATH: Where you want to store your downloads, usually just the current working directory + subfolder "content" but some of you might want to directly download to their media server.

## Usage

1.  `python3 downloader.py`
2.  Enter your credentials in the terminal when asked.
3.  After login just wait and the downloads will begin automatically.
4.  There will be a progress bar in the console window.
5.  If you encounter any issues please report them to my github.

              __
          ___( o)>
          \ <_. )
           `---'  for s
