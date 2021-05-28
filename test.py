# page33
from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
    print("err")
    # null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용
else:
    print('x')
    # 프로그램을 계속 실행합니다. excep 절에서 return이나 break를 사용했다면
    # 이 else 절은 필요 없습니다.
