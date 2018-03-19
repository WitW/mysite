from selenium import webdriver
url = "http://www.dytt8.net/html/gndy/rihan/list_6_3.html"
broswer = webdriver.Firefox()
broswer.get(url)
page = broswer.page_source
print(page)
css_selector = broswer.find_elements_by_tag_name("a")
for i in css_selector:
    print(i)

