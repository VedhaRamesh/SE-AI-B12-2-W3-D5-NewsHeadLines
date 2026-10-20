import sys

import requests
from bs4 import BeautifulSoup


URL = "https://www.bbc.com/news"
HEADLINE_SELECTOR = "h2[class*=IndexCardHeading-styles__CardHeadlineStyled]"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; HeadlinesBot/1.0)"}


def main():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Could not fetch headlines: {error}", file=sys.stderr)
        return 1

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    seen = set()

    for item in soup.select(HEADLINE_SELECTOR):
        headline = item.get_text(" ", strip=True)
        if headline and headline not in seen:
            headlines.append(headline)
            seen.add(headline)
        if len(headlines) == 5:
            break

    for number, headline in enumerate(headlines, start=1):
        print(f"{number}. {headline}")

    if len(headlines) < 5:
        print(f"Only found {len(headlines)} unique headlines.", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())