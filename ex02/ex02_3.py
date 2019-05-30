#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
#1.파일읽기 ->한줄씩
f = open("도별미세먼지.csv", "r")
items = f.readlines()
f.close()


dic = {}
for item in items:
    item = item.replace("\n", "")
    line = item.split(",")
    dic[line[0]] = int(line[1])


print(round(sum(dic.values())/len(dic.values()), 2))

#2.부산, 20 \n ->"\n"을""변경->replace()
#3.,기준으로 분리
#4.딕션너리에 추가->키는 분리된 첫번째항목, 값은 두번째항목
#5.합계, 개수, 평균
#6.최대값인 지역