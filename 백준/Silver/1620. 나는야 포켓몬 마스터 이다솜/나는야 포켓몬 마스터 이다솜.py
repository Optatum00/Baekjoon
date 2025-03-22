import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())

pokemon = {}
for i in range(N):
    pokemon[input().strip()] = i+1
    
reverse_pokemon= dict(map(reversed,pokemon.items()))

for i in range(M):
    quiz = input().strip()
    if (quiz.isdigit()):
        print(reverse_pokemon.get(int(quiz)))
    else:
        print(pokemon.get(quiz))