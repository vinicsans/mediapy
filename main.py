registers = open("history.txt", "a+")
notas_finais = []
materias = []

def media_singular(): 
    materias.append(input('Digite o nome da matéria: '))

    notas_input = input('Digite suas notas, separando-as com espaço: ').split()
    notas = list(map(float, notas_input))
    notas_finais.append(round(sum(notas)) / len(notas))

    selection()
###
def media_final(notas, materias):
    index = 0
    area = input('Deseja adicionar um nome para a área de conhecimento? ')
    registers.write('\n{}'.format(area))
    for values in notas:
        registers.write("\n{}: {}".format(materias[index], values)) 
        index += 1
    registers.write("\nA nota final é: {}\n".format(round(sum(notas)) / len(notas)))
    print("\nA nota final é: {}\n".format(round(sum(notas)) / len(notas)))
###
def selection():
    nexts = int(input('Deseja adicionar alguma máteria? 1 - Sim | 2 - Não : '))
    if (nexts == 1):
        media_singular()
    elif (nexts == 2):
        media_final(notas_finais, materias)

media_singular()


