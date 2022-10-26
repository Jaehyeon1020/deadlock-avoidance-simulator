
# 남은 자원으로 실행 가능한지 여부를 확인
# process number : process의 번호(0~ )
def check_executable(resource_num, additional_need_matrix, remaining_unit, process_number):
    check = True
    
    for i in range(resource_num):
        if additional_need_matrix[process_number][i] > remaining_unit[i]:
            check = False
    
    return check
        

# safe 상태 판단, Safe sequence or unsafe state인 이유 출력
def is_safe(process_num: int, resource_num: int, unit_num: list,
            max_claim_matrix: list, current_alloc_matrix: list):
    remaining_unit = [i for i in unit_num]
    additional_need_matrix = [[0 for i in range(resource_num)] for j in range(process_num)]
    executed = [False for i in range(process_num)] # 프로세스가 실행가능했는지 여부를 저장하는 리스트
    safe_sequence = [] # safe sequence 저장
    
    # 남아있는 자원 유닛 개수 계산 / 저장
    # 추가 필요량 계산 / 테이블에 저장
    for i in range(process_num):
        for j in range(resource_num):
            remaining_unit[j] -= current_alloc_matrix[i][j]
            additional_need_matrix[i][j] = max_claim_matrix[i][j] - current_alloc_matrix[i][j]
            
    # 실행 가능한지 확인하고 safe sequence대로 동작(실행 후 자원 반납)
    for _ in range(process_num):
        for i in range(process_num):
            if check_executable(resource_num, additional_need_matrix, remaining_unit, i) == True and executed[i] == False:
                executed[i] = True
                safe_sequence.append(i)
                for j in range(resource_num):
                    remaining_unit[j] += current_alloc_matrix[i][j]
    
    # 실행불가능한 process가 남아있었다면 : all_executed <- False(deadlock)
    all_executed = True
    for i in range(process_num):
        if executed[i] == False:
            all_executed = False
    
    # 모든 process가 실행가능했다면 : 상태 출력, safe sequence 출력
    if(all_executed == True):
        print("State: SAFE")
        print("Safe sequence: ", end='')
        #print(safe_sequence) # test
        
        for i in range(len(safe_sequence)):
            if(i != 0):
                print("-> ",end='')
            print("Process %d "%(safe_sequence[i] + 1), end='')
        
        print('')
    
    # 모든 process가 실행가능하지 않았다면 : 상태 출력, unsafe state인 이유 출력
    elif(all_executed == False):
        print("State: UNSAFE")
        print("Reason: process", end='')
        
        for i in range(process_num):
            if(executed[i] == False):
                if(i != 0):
                    print(",", end='')
                print(" %d"%(i+1), end='')
        
        print(" can occur deadlock")
            
    

file = open("./input.txt", 'rt')
input = file.readlines()
# 문자열로 들어온 input file 공백 구분으로 자르고 int로 형변환
for i in range(len(input)):
    input[i] = input[i].split(' ')
    input[i] = list(map(int,input[i]))

process_num = 0 # 프로세스 개수
resource_num = 0 # 자원 개수
unit_num = [] # 유닛 개수(자원별로 저장)

process_num = input[0][0]
resource_num = input[0][1]

for i in range(2, len(input[0])):
    unit_num.append(input[0][i])

# 할당 테이블 초기화
max_claim_matrix = []
current_alloc_matrix = []

# 각 행렬에 요소들 삽입
for i in range(1, 1 + process_num):
    max_claim_matrix.append(input[i])
    current_alloc_matrix.append(input[i + process_num])
    
# safe 상태 판단, Safe sequence or unsafe state인 이유 출력
is_safe(process_num, resource_num, unit_num, max_claim_matrix, current_alloc_matrix)

file.close()