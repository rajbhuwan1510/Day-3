# Stack Overflow Scraper

#### Assignment Link : [https://github.com/rajbhuwan1510/Day-3/tree/main/homework](https://github.com/rajbhuwan1510/Day-3/tree/main/scrappingStackOverFlow)

## Problem Statement
#### "Utilize Beautiful Soup to scrape the provided Stack Overflow webpage and extract relevant information pertaining to the question: "How do I get the current time in Python?"

* This project utilizes Beautiful Soup to scrape a Stack Overflow webpage and extract relevant information pertaining to a specific question.
*   I have choose this link link for scrappring you can choose any other link of Stack   Overflow
* link: ( https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python )
## Requirements

- Python 3.0
- BeautifulSoup4 library
- Requests library

## Installation

    1. Clone this repository:
        git clone: "[https://github.com/your-username/stackoverflow-scraper.git](https://github.com/rajbhuwan1510/Day-3/tree/main/scrappingStackOverFlow)"

    2. Install the required libraries:
        - Requests
        - BeautifulSoup4
## CODE

    import requests
    from bs4 import BeautifulSoup

    url="https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
    data=requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')

    #print(soup.text)
    question=soup.find('a',class_="question-hyperlink")
    print('Question:',question.text)
    answer=soup.find_all('div',class_="answercell post-layout--right")
    count=1
    for ans in answer:
        print(count,"____________________________________")
        oneans=i.find('div',class_="s-prose js-post-body").text.strip()
        print(oneans)
        count+=1
## Usage

1. Run the script `scrape_stackoverflow.py`.
2. Enter the URL of the Stack Overflow webpage you want to scrape.
3. Enter the title of the question you want to extract information for.
4. The script will fetch the HTML content, parse it using Beautiful Soup, and display the question and its answers.

## Authors

- Rajbhuwan Jaitawat

## License
Its free Guysss :)
