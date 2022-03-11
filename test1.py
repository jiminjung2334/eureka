n=input()             # n을 문자열로 입력받음

reverse_num=n[::-1]             #슬라이싱을 이용해 n을 거꾸로 바꿔준다

remove_num=reverse_num.lstrip("0")      #선행하는 0들을 제거하는 lstrip함수를 이용해 선행하는 0제거



print(remove_num)     #출력
