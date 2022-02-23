#install all requirment
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://www.interviewbit.com/python-interview-questions/#python-pep8-and-its-importance"

#Step 1 : get html
r = requests.get(url)
htmlContent = r.content

#print(htmlContent)

#Step 2 : parse
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#Step 3 : tree formation 
#ques = soup.find_all("section" , class_ = "ibpage-article-header")
#print(soup.find(id="what-is-python-what-are-the-benefits-of-using-python").get_text())
print(soup.find(id = "freshers").get_text())