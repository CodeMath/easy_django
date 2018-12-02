import requests
from bs4 import BeautifulSoup

# HTTP GET 요청
req = requests.get("https://search.shopping.naver.com/search/all.nhn?query=%EC%B9%B4%EB%93%9C%EC%A7%80%EA%B0%91&frm=NVSCVUI")

# HTML 소스코드 가져오기
req_code = req.text

# HTTP Header 정보 가져오기
req_header = req.headers

# HTTP Status 코드 가져오기 ( 200인 경우, 정상 )
req_status = req.status_code

# HTTP 통신이 정상적으로 작동되었는지 체크 ( True/False 로 반환 )
req_ok = req.ok

# BeautifulSoup를 통해 HTML 소스코드를 python 객체로 변환 / parser 는 내장 html.parser 이용
soup = BeautifulSoup(req_code, 'html.parser')

# div 태그 중, class 이름이 info 인 모든 객체 조회
lists = soup.find_all('div', attrs={'class':"info"})

# lists 에 담긴 객체 리스트에서 첫 번째 객체 출력
print(lists[0].a.text)


# 전체 객체 중, 목록 뽑기 ( 줄바꿈 밑 탭해서 늘린 여백 등을 replace 함수를 이용해 없애기 )
for each in lists:
    print(each.a.text.replace("\n","").replace("\t","").replace("  ",""))