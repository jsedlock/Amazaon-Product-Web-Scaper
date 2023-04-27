
![Amazon](https://cdn.osxdaily.com/wp-content/uploads/2022/10/apple-amazon-deals-610x341.jpg)

# Amazaon-Product-Web-Scaper
This repository is a personal project that scraps Amazon daily for the price of a Macbook Pro I am interested in buying. This script appends the price to a .csv file daily and emails me the link when the price drops below a specified limit. 

## Dependencies
```python
from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
import datetime
import csv
import smtplib
```
## Future Work
Since this script scrapes Amazon daily, and appends to a .csv file. After multiple weeks or months have passed, I plan on performing a time series analyis on the data to gleem additional insights for my purchasing decision
