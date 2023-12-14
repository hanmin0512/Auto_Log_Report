# 프로젝트 명 : Ip_detector 

# 주제
- 파일 검수 웹 서비스

# 타겟
- 보안 회사에서 웹 로그파일 분석하는 보고서를 작성하는 직책
# 내용
> 이메일 서비스
-  회사에서 파일을 공유 및 전송 할 때 주석 등이 있으면 이메일을 전송하여 알려준다.

> 고객사 로그파일 분석 및 보고서 작성 자동화
- 고객사의 로그 파일을 보고 분 단위를 기준으로 몇번 접속을 시도 했는지 확인한다.
- 가장 많이 접속한 IP는 CIRIMAL API를 사용해서 IP정보를 가져온다.
- 이를 결합해서 보고서 템플릿을 활용하여 보고서를 자동화 작성한다.
- 작성된 보고서를 PDF로 사용자가 다운로드 할 수 있게 한다.

# 수정 할 부분
- Merger.py Criminal함수  API KEY 기입
``` 
class Criminal:
    def __init__(self, ip_address):
        
        self.url = f"https://api.criminalip.io/v1/asset/ip/summary?ip={ip_address}"

        self.payload={}
        self.headers = {
            "x-api-key": "<본인의 CRIMINAL API KEY를 기입>"
        }
```

- Merger.py 메인 함수 부분
```
if __name__ == "__main__":
    received_email = "<본인 네이버이메일 주소 기입>@naver.com"
    path = 'uploads'
    MT = Monitering(path,received_email)
    MT.inspect_annotation("#")
```

- .env 파일을 만들어 자신의 이메일 아이디 비밀 번호를 작성한다.
```
SECRET_ID = "이메일 아이디"
SECRET_PASS = "이메일 비밀번호"
```


## 로그 기록 보고서 자동화 기능 시행
- 보고서 template 제작
> ![templates](https://github.com/hanmin0512/share_app/assets/37041208/35c90e67-d722-4643-819f-0e9bce34a4c5)


- 메인페이지
> ![page](https://github.com/hanmin0512/share_app/assets/37041208/c989862b-3483-4877-ae7e-853bd4e38bb2)

-  로그파일 웹 페이지에 업로드
> ![upload_log](https://github.com/hanmin0512/share_app/assets/37041208/878728dc-1e0a-4c70-a7f6-d869c7134813)

- 업로드 후 자동으로 만들어진 보고서 다운로드
> ![report_download_page](https://github.com/hanmin0512/share_app/assets/37041208/3e98a333-3d72-45e0-9712-a6d22ed01ba9)
> ![report](https://github.com/hanmin0512/share_app/assets/37041208/392ffc8b-700b-4c57-8a51-b02c9275e177)

- 다운로드 된 보고서 pdf 파일 확인
> ![report_pdf](https://github.com/hanmin0512/share_app/assets/37041208/ce221d58-2e86-4d69-a681-27b654659cba)



