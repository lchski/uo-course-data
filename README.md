# uOttawa Course Data Scraper

Downloads the HTML files for UO course calendars per department, and parses them into usable JSON.

## Downloader

Add the three-character code for each department you’re interested in. (Examples: History, "HIS"; Political Science, "POL".)

Run the downloader with Python 3:

```python
python3 downloader.py
```

The `pages/` directory should now contain the HTML file for each department’s course calendar.

## Parser

Run the parser with Python 3:

```python
python3 parser.py
```

That’s it!
