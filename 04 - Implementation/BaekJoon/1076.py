'''
리스트에 모든 색깔을 다 넣는다
3개의 색깔을 입력 받는다
각 색깔에 대한 인덱스를 저장한다
맨 앞 두자리를 바로 문자열로 받아서 그걸 다시 정수로 바꾸고 맨마지막 인덱스로 지수승 계산을 한다
'''
#!/usr/bin/env python3
color=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
col1 = input()
col2 = input()
col3 = input()
index1= color.index(col1)
index2= color.index(col2)
index3= color.index(col3)

result = int(str(index1)+str(index2))*(10**index3)
print(result)