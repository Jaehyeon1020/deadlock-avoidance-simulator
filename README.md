# deadlock-avoidance-simulator
교착상태 회피 기법의 이해를 위한 프로그램

## 프로그램 개요
프로그램은 input.txt 파일의 내용을 바탕으로 Deadlock Avoidance를 수행한다. 
그 결과 현재 상태가 Safe인지 Unsafe인지를 판단하고, 현재 상태와 상태 판단의 이유를 출력한다.
input.txt 파일은 다음과 같은 내용을 담고 있다 :
1. 프로세스의 총 개수
2. 자원 종류의 총 개수
3. 종류별 자원의 unit 개수
4. Max-claim matrix(각 프로세스가 최대로 요구할 수 있는 자원 양에 대한 행렬)
5. Current-allocation matrix(각 프로세스에 현재 할당되어 있는 unit의 개수에 대한 행렬)

## 프로그램 동작 흐름
1. input.txt 파일을 열고 읽는다.
2. input.txt의 내용을 바탕으로 2차원 list로 구성되는 Max-claim matrix 행렬과 Current-allocation matrix 행렬을 생성한다.
3. is_safe() 함수에 input.txt로부터 추출한 프로세스의 총 개수, 자원 종류의 총 개수, 종류별 자원의 유닛 개수(list), Max-claim-matrix, Current-allocation matrix를 인자로 전달하고 호출한다.
4. is_safe() 함수 내부에서 주어진 인자들을 바탕으로 현재 상태가 Safe인지 Unsafe인지를 판단하고, 현재 상태와 상태 판단의 이유를 출력한다.
5. input.txt 파일을 닫고 프로그램을 종료한다.

## input.txt
* 1st line : ($프로세스의 총 개수) ($자원 종류의 총 개수) ($자원 R<sub>1</sub>의 unit 개수) ($자원 R<sub>2</sub>의 unit 개수) ... ($자원 R<sub>n</sub>의 unit 개수)
* < 2nd line : Max-claim matrix, Current allocation matrix(행은 프로세스, 열은 자원을 의미)

## 실행 결과의 예
### input.txt(입력)
```
3 3 9 5 7
7 5 3
3 2 2
4 3 3
0 1 0
2 0 0
0 0 2
```

### 실행 결과(출력)
```
State: SAFE
Safe sequence: Process 1 -> Process 2 -> Process 3
```
Remaining Unit은 (7개, 4개, 5개)이며, Remaining Unit을 할당하여 Process 1 -> Process 2 -> Process 3의 순서로 항상 실행가능하다.   

### input.txt(입력)
```
4 3 9 3 4
5 2 3
1 2 2
7 3 3
9 1 0
1 0 1
0 1 1
5 2 1
2 0 0
```

### 실행 결과(출력)
```
State: UNSAFE
Reason: Process 1, 2, 3, 4 can occur deadlock
```
Remaining Unit은 (1개, 0개, 1개)이며, Remaining Unit을 할당하여 어떤 프로세스도 실행가능하지 않다.

