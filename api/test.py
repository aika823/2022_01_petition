import math
from konlpy.tag import Kkma
from konlpy.utils import pprint

def str_to_nouns_list(str):
    kkma = Kkma()
    return kkma.nouns(str)

def str_to_word_list(str):
    return str.split(' ')

petition_list = [
    "청와대의 직접 소통은 국민이 물으면 정부가 답한다 는 철학을 지향합니다.",
    "국정 현안 관련, 국민들 다수의 목소리가 모여 30일 동안 20만 이상 추천 청원에 대해서는",
    "정부 및 청와대 관계자(각 부처 장관, 대통령 수석·비서관, 특별보좌관 등)가 답하겠습니다.",
    "외국 국적 여중생을 묶고 6시간 가학적 집단폭행한 가해자4명 강력처벌.신상공개를촉구합니다.",
    "드라마 설** 방영중지 청원",
    "푸들만 19마리 입양 ! 온갖고문으로 잔혹학대 후 죽이고 불법매립한 범죄자의 강력한 처벌을 촉구하며, 신상공개 동의해주세요!!!!!",
    "청원 목록지금 청원하기 분류",
    "청원 만료일참여인원 ",
    "드라마 설** 방영중지 청원",
    "푸들만 19마리 입양 ! 온갖고문으로 잔혹학대 후 죽이고 불법매립한 범죄자의 강력한 처벌을…",
    "아이들까지 백신강요 하지 마세요!",
    "코로나 1차 접종 후 뇌사상태에 빠진 제 딸을 살려주세요!!!!!",
    "초등6학년 여자아이를 11명이 보복 폭행한 사건입니다 도와주세요",
    "반헌법적 드라마를 방영하는 JTBC의 폐국을 청원합니다.",
    "학원, 도서관, 독서실 백신패스 철회해라 !!!",
    "박근혜 사면을 반대합니다.",
    "청소년 백신패스 도입 철회해주세요.",
    "안하무인, 아전인수, 유체이탈 언행으로 가족 모두를 외상후 스트레스 장애에 빠뜨린 20대 …",
    "화이자백신 맞은 14살 제 딸이 심근염으로 생사를 오가고 있습니다!! 제발 도와주세요!!",
    "국내 SNS와 커뮤니티에 대한 검열을 남발하는 'n번방 방지법' 개정을 …",
    "코로나 백신 성분 검증 및 현미경으로 미생물 유무 공개 방송 합시다",
    "임산부와 난임치료자는 백신패스 면제해주십시오.",
    "초등학교 6학년 같은 반 남학생이 엘리베이터 안에서 저희 딸의 바지를 내리고 강제추행했습니다.",]

sample = str_to_word_list("김응민 탄핵해주세요 백신을 안맞고 사람들을 폭행해요 공개 합시다")
print(sample)
petition_nouns_list = [str_to_word_list(petition) for petition in petition_list]

for petition_nouns in petition_nouns_list:
    intersection = list(set(sample) & set(petition_nouns))
    match_percentage = (len(intersection) / (len(sample)+len(petition_nouns))) * 200
    print(round(match_percentage, 2))