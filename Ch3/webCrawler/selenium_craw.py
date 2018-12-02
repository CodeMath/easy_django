from selenium import webdriver
import time
import requests

# 크롬 드라이버 절대경로
chrome_driver = "/Users/codeblock/PycharmProjects/easy_dajgno/Ch3/webCrawler/chromedriver"

# webdriver 에서 크롬 브라우저 사용
driver = webdriver.Chrome(chrome_driver)

# driver.get("https://www.google.com")
#
# # xpath 기준으로 검색창 선택
# search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
#
# # 검색어 입력
# search.send_keys("django")
#
# # Google검색 버튼 클릭
# driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()

#URL 접속
driver.get('https://www.hbg.com/ko-kr/eth_usdt/depth/?trade=exchange')

# 웹 페이지가 로드되기 까지, 3초 정도 기다리기
driver.implicitly_wait(3)

while True:
    asks = driver.find_element_by_id("market_depth_asks")
    bids = driver.find_element_by_id("market_depth_bids")

    asksChild = asks.find_elements_by_tag_name('dd')
    bidsChild = bids.find_elements_by_tag_name('dd')
    try:
        b = bidsChild[0].text
        a = asksChild[0].text
        print(b)
        print(a)
        requests.get('http://127.0.0.1:8000/data/?asks='+a+'&bids='+b+"&name=이더리움")
        print("=====================")
    except:
        pass

    time.sleep(5)


