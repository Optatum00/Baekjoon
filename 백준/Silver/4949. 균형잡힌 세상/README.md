# [Silver IV] 균형잡힌 세상 - 4949 

[문제 링크](https://www.acmicpc.net/problem/4949) 

### 성능 요약

메모리: 32412 KB, 시간: 92 ms

### 분류

자료 구조, 스택, 문자열

### 제출 일자

2025년 1월 27일 04:16:52

### 내 풀이의 큰틀
<p>문자를 입력받고, 만약 입력받은값이 '.'이면 종료한다.</p>
<p>문자의 길이만큼 반복하며, 한글자씩 다 검토한다.</p>
<p>만약 알바벳이라면 바로 건너뛴다. 그리고 알바벳이 아니라면 ()[]중 어떤 건지 검사한다.</p>
<p>([이라면 stack에 쌓고, )]이면 추가 검토를 진행한다.</p>
<p>)]가 여는 괄호 없이 나왔다면 바로 no를 출력하고, 아니라면 stack[-1]을 확인하여 맞는 짝인지 확인한다.</p>
<p>맞는 짝이면 stack에서 pop해주고, 틀린짝이면 no를 출력한다. 한문장의 사이클이 돌았을때 stack이 비었다면 yes를 출력한다.</p>

### 문제 설명

<p>세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.</p>

<p>정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.</p>

<p>문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.</p>

<ul>
	<li>모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.</li>
	<li>모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.</li>
	<li>모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.</li>
	<li>모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.</li>
	<li>짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.</li>
</ul>

<p>정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.</p>

### 입력 

 <p>각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.</p>

<div>입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.</div>

### 출력 

 <p>각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.</p>

