
* ["서울시 자치구 목적별 CCTV 설치 수량"](http://data.seoul.go.kr/dataList/OA-2722/F/1/datasetView.do)

* ["서울시 자치구 년도별 CCTV 설치 현황"](http://data.seoul.go.kr/dataList/OA-2734/F/1/datasetView.do;jsessionid=A36B54AF679B582B475FE3796D32C1B6.new_portal-svr-21)

`서울시CCTV설치운영현황(자치구)_년도별_211231기준.csv` 본문 첫째줄

```
※ 2021.12.31. 현황을 기준으로 각 연도별 설치된 CCTV 수량. 교체(저화질교체, 성능개선)는 최초설치연도가 아닌 교체년도 수량에 포함
```

```python
>>> with open(
        "서울시CCTV설치운영현황(자치구)_년도별_211231기준.csv", 
        "r",   
        encoding="cp949") as f:
        meta_data = f.readlines(1)
>>> meta_data

# ['"※ 2021.12.31. 현황을 기준으로 각 연도별 설치된 CCTV 수량. 교체(저화질교체, 성능개선)는 최초설치연도가 아닌 교체년도 수량에 포함",,,,,,,,,,,,\n']
```
