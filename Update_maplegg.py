
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import time


Member = (("권강현","밍먕의",0),("김대성","머성머",0),("김민섭","모법또비",6)
        ,("★김민식★","SiGy",3),("김민주","헬로후닝",1),("김상완","얼렁",1),("김성원","fims13",6),
        ("김성은","민들레u",6),("김재홍","JH메신",3),("김정현","뚠두붕",1),("김준수","죽염과송염",1),
        ("김준엽","엽쭌이",4),("김지호","별빛사서",1),("류한일","죤방",6),("문기봉","춤추는이병",1),
        ("박선호","슈리언즈",0),("박정혁","그러죠뭐",5),("박정환","하늘다람쥐다",1),("박지호","SHERO",1),
        ("박진제","뿌쟝",4),("변형각","맹구포드",1),("빈석현","너와함께랄라",6),
        ("서동진","땡진7번",0),("서효빈","음악한모금",4),("손민재","신징",2),("손정수","얍힝",0),
        ("신제철","박사할걸",1),("안성현","배틀메이지",2),("양수정","권투초보",3),("윤주희","계란탕라면",1),("원동연","도치츄",2),
        ("이누리","아힌느",7),("이재복","꽃촬",2),("이철희","YYeah",0),
        ("이현식","이현식",1),("임승혁","존예여신연희",0),("장요셉","장요셉",1),("전일우","쿠키선비",0),
        ("전채연","석사낙지",1),("정종한","온pv",3),("조인수","토스트나로오",1),
        ("최민호","쪼꼬",1),("최재원","하늘뱀장어",1),("최준용","람검",4),("한민욱","쓸윈부쓸윈브",1),
        ("한승수","티모선",0))



for Name,Nickname,Server in Member:
        Convert_Nick=urllib.parse.quote(Nickname) #닉네임 url 인코딩

        driver=webdriver.Chrome()
        driver.get(f"https://maple.gg/u/{Convert_Nick}") 

        Last_Update=driver.find_element(By.XPATH,"//*[@id='user-profile']/section/div[2]/div[2]/div[5]/div[1]/span").text #마지막 업데이트 부분 크롤링

        #최신갱신 정보가 아니라면, 최신 정보가 될때까지 while문 (차례차례 넘어가면서 갱신할경우, '잠시후 다시 갱신해주세요' 오류 문구발생 방지)
        if Last_Update != "마지막 업데이트: 오늘":
                while Last_Update!="마지막 업데이트: 오늘":
                        driver.find_element(By.XPATH,"//*[@id='btn-sync']").click()
                        driver.close()
                        driver=webdriver.Chrome()
                        driver.get(f"https://maple.gg/u/{Convert_Nick}")
                        Last_Update=driver.find_element(By.XPATH,"//*[@id='user-profile']/section/div[2]/div[2]/div[5]/div[1]/span").text



print("완료")

