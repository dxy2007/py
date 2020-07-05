from selenium import webdriver
c = webdriver.PhantomJS(executable_path='H:\py\phantomjs-2.1.1-windows')
c.get('https://www.hetao101.com')
print(c.page_cource)
c.close()