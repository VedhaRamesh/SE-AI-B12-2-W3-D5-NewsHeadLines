# SE-AI-B12-2-W3-D5-NewsHeadLines

Fetches and prints the five top headlines currently available on [BBC News](https://www.bbc.com/news). The script uses `requests` to download the page and Beautiful Soup to parse its HTML.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

## Setup and run

Open a terminal in this project directory, then create and activate a virtual environment.

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies and run the script:

```bash
python -m pip install requests beautifulsoup4
python headlines.py
```

The script prints up to five unique, non-empty headlines, numbered one per line. If the request fails, it prints an error and exits. If fewer than five headlines are found, it prints the available headlines and reports how many were found.

## How headline extraction works

The script selects BBC headline `<h2>` elements using the `HEADLINE_SELECTOR` in `headlines.py`. The selector is based on the BBC page's current HTML and may need updating if the site changes its markup. To investigate, inspect a headline in your browser's developer tools and try the selector in the console.

`requests` downloads HTML but does not run JavaScript. If a different news site inserts its headlines only after the page loads in a browser, the response may not contain them; use a site that serves headlines in its HTML or a browser automation tool such as Selenium or Playwright.