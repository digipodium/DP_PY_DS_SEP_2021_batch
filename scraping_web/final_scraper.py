from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_fkrt_addr(query = 'bags',start_pos = 1):
    url = 'https://www.flipkart.com/search'
    param1 = f'q={query}'                       # item to be search
    param2 = f'page={start_pos}'                # starting page
    return f'{url}?{param1}&{param2}'

def extract_page_data(driver):
    data = []
    cards = driver.find_elements_by_css_selector('div._1xHGtK._373qXS')
    if len(cards)> 0:
        for item in cards:
            data.append(dict(
                brand = item.find_element_by_css_selector('div._2WkVRV').text,
                title = item.find_element_by_css_selector('a.IRpwTa').get_attribute('title'),
                price = item.find_element_by_css_selector('div._30jeq3').text,
            ))
    return data

def get_flipkart_data(search = 'bags',pos = 1,):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    all_data= [] 
    while True:
        addr = get_fkrt_addr(search, pos)
        driver.get(addr)
        data = extract_page_data(driver)
        if len(data):
            all_data.extend(data)
            pos += 1
        else:
            driver.close()
            break
    return all_data


content = get_flipkart_data('bags')