nota_par = 0.0
nota_impar = 0.0

cont = 51
x = 1

total_par = 0.0
total_impar = 0.0

for x in range(x, cont):
    if x % 2 == 0:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
        nota_par = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}: "))
        total_par = total_par + nota_par
    else:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
        nota_impar = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}: "))
        total_impar = total_impar + nota_impar

if total_impar < total_par:
    print(f"Média de notas alunos pares é {total_par/25:,.2f} e a média de notas dos alunos ímpares é {total_impar/25:,.2f}")
    print("Os alunos PARES tiveram a melhor média de notas!")
elif total_par < total_impar:
    print(f"Média de notas alunos pares é {total_par/25:,.2f} e a média de notas dos alunos ímpares é {total_impar/25:,.2f}")
    print("Os alunos ÍMPARES tiveram a melhor média de notas!")
else:
    print(f"Média de notas alunos pares é {total_par/25:,.2f} e a média de notas dos alunos ímpares é {total_impar/25:,.2f}")
    print("Os alunos PARES e os alunos ÍMPARES tiveram a mesma média de notas!")


