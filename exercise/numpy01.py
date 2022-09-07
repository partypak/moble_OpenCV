import numpy as np





print(np.arange(10))
print(np.arange(10).reshape(2,5))                      # 1차원 -> 2차원 배열로 변경
print(np.arange(10).reshape(2,5).transpose())          # 차원변형 가로 세로 변경
print(np.arange(10).reshape(2,5).T)                    # 축을 지정하지 않는 경우 약어로 다음과 같이 사용가능 ( = transpose())
print('-------------------------')
print(np.arange(27))
print(np.arange(27).reshape(3,3,3))                    # 1차원 -> 3차원 배열로 변경
print('-------------------------')
print(np.arange(27).reshape(3,3,3).transpose())        # 기본순서 (0,1,2)의 역순 (2,1,0)
print('-------------------------')
print(np.arange(27).reshape(3,3,3).transpose(1,0,2))   # 이해가 잘 되질 않지만 넘어간다.
#  np.save('shape_array',np.arange(27).reshape(3,3,3).transpose(1,0,2))  # shape_array.npy 파일명으로 저장
print('-------------------------')
print(np.load('shape_array.npy'))