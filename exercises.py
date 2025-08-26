"""Aprendendo Python exercicios Curso em  Video"""

# introdução python hello
print('olá Luan')
first_name = 'luan'
last_name = 'tonetto'
full_name = first_name + '' + last_name
print(full_name)
message = 'Hello,' + full_name.title() + '!'
print(message)

# calculo soma 2 numeros
n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
s = n1+n2
print('a soma vale', s)
print('A soma vale ()'.format(s))

n = float(input('digite um valor'))
print(n)
n = str(input('digite um valor'))
n = bool(input('digite um valor'))

n1 = int(input('digite um valor'))
n2 = int(input('digite um valor:'))
s = n1+n2

# Soma, numero, alfabeto, verdadeiro falso
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))
a = input('digite algo')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços?', a.isspace())
print('é um numero?', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumerico?', a.isalnum())
print('Esta em maisculo?', a.isupper())
print('Esta em minusculo?', a.islower())
print('Esta cpaitalizada?', a.istitle())

# msg prazer em conhecer
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {}!'.format(nome))

# antecessor e sucessor
n = int(input('digite um numero: '))
a = n-1
s = n+1
print('analisando o Valor {}, seu antecessor é {}, e o sucessor é {}'.format(n, a, s))
print('analisando o Valor {}, seu antecessor é {}, e o sucessor é {}'.format(
    n, (n-1), (n+1)))

# medidas
medida = float(input('Qual a distancia em metros?'))
cm = medida*100
mm = medida*1000
print('A medida de {} corresponde a{}cm e {}mm '.format(medida, cm, mm))

# tabuada
num = int(input('Qual o numero?'))
print('{}x{}={}'.format(num, 1, num*1))
print('{}x{}={}'.format(num, 2, num*2))
print('{}x{}={}'.format(num, 3, num*3))
print('{}x{}={}'.format(num, 4, num*4))
print('{}x{}={}'.format(num, 5, num*5))
print('{}x{}={}'.format(num, 6, num*6))
print('{}x{}={}'.format(num, 7, num*7))
print('{}x{}={}'.format(num, 8, num*8))
print('{}x{}={}'.format(num, 9, num*9))
print('{}x{}={}'.format(num, 10, num*10))

# calculo dinheiro conversao em dolar
real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real/3.27
print('com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))

# calculo area de parede
larg = float(input('Qual a largura da parede?'))
alt = float(input('altura da parede'))
area = larg*alt
print("sua parede tem a dimensao de {}x{} e sua area é de {}".format(larg, alt, area))
tinta = area/2
print('para pintar essa parede voce precisara de {}l de tinta'.format(tinta))

# calculo produto
preço = float(input('qual é o preço do produto?R$'))
novo = preço-(preço*5/100)
print('O produto com 5% de desconto vai custar R${}'.format(novo))

# calculo salario
salario = float(input('qual é o seu salario R$?'))
novo = salario+(salario*15/100)
print('Seu salario é R${} com 15% de aumento ele fica R${:.2f}'.format(salario, novo))

# Calculo temperatura
c = float(input('Informe a temperatura em C:'))
f = ((9*c)/5)+32
print('A temperatura de {}C corresponde a {}*F'.format(c, f))

# calculo aluguel de carro
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos KM rodados?'))
pago = (dias*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

# importando biblioteca math
import math
num = int(input('Digite um numero'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil))
print('A raiz de {} é igual a {}'.format(num, math.floor))
num = int(input('Digite um numero'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# gerar numero aleatorio
num = random.randint(1, 100)
print(num)

# importando biblioteca do site python
import time
time.sleep(1)

#quebrando numero com import
import math 
from math import trunc
num = float(input('Digite um valor:'))
print('O valor digitado foi {}e a sua porção inteira é {}'.format(num,math.trunc(num)))
#sem import
num=float(input('digite um valor:'))
print('O valor digitado foi{}sua porção inteira é{}'.format(num,int(num)))

#calculando hipotenusa (sem import)
co=float(input('Qual é o comprimento do cateto oposto:'))
ca= float(input('Qual é o comprimento do cateto adjacente:'))
soma=(co**2+ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(soma))
#com import
import math
co=float(input('Qual é o comprimento do cateto oposto:'))
ca= float(input('Qual é o comprimento do cateto adjacente:'))
soma=math.hypot(co,ca)
print('A hipotenusa é:{:.2f}'.format(soma))

#seno cosseno e tangente
import math
angulo = float(input('Digite o Angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de{} tem o SENO de {:.2f}'.format(angulo,seno))
print('O angulo de{} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
print('O angulo de{} tem a TANGENTE de {:.2f}'.format(angulo,tangente))

#sorteando nomes 
import random
aluno1=input('primeiro aluno? ')
aluno2=input('segundo aluno? ')
aluno3=input('terceiro aluno? ')
aluno4=input('quarto aluno? ')
alunos=[aluno1,aluno2,aluno3,aluno4]
msg=random.choice(alunos)
print('O aluno escolhido foi {}'.format(msg))

#sorteando nomes em ordem
import random
aluno1=input('primeiro aluno? ')
aluno2=input('segundo aluno? ')
aluno3=input('terceiro aluno? ')
aluno4=input('quarto aluno? ')
lista=[aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print('A ordem escolhida foi')
print(lista)
 
 #tocando mp3 
import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/Luan/Desktop/ex021.mp3') #caminho onde tem a msc
pygame.mixer.music.play()
input()
pygame.event.wait()

#fatiando frases
frase = 'curso em video python'
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[13])
print(frase[3:13:1])
print("""Uma frase muito grande """ )

#nome em maisculo e minusculo e contador
nome = str(input('Qual Seu Nome?')).strip()
print ('Analisando seu nome...')
print ('Seu nome em maiusculas é {}'.format(nome.upper()))
print ('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras '.format(len(nome)))
print('Seu primeiro nome tem {} letras ' .format(nome.find(' ')))

#unidade,dezena,centena,milhar
numero = int(input('Informe um numero ' ))
n = str(numero)
print('Analisando o numero {} '.format(numero))
print('Unidade {} '.format(n[3]))
print('Dezena {} '.format(n[2]))
print('Centena {} '.format(n[1]))
print('Milhar {} '.format(n[0]))
#jeito 2 sem 3 numeros para ler
numero = int(input('Informe um numero ' ))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o numero {} '.format(numero))
print('Unidade {} '.format(u))
print('Dezena {} '.format(d))
print('Centena {} '.format(c))
print('Milhar {} '.format(m))

#verificando as letra de um texto
cid= str(input('Qual o nome da sua cidade?'))
print(cid[:5] == 'Santo')
#(retirando espaço)
cid= str(input('Qual o nome da sua cidade?')).strip()
print(cid[:5].upper == 'Santo')

#procurando uma palavra dentro de uma spring
nome=str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva?{}'.format('SILVA'in nome.upper()))

#lendo uma frase e mostrando quantas vezes uma letra aparece
frase=str(input('Digite uma frase: ')).upper().strip()
print('Analisando Frase')
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} .'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {} .'.format(frase.rfind('A')+1))

#nome completo fatiando
n=str(input('Digite seu nome completo: ')).strip()
nome=n.split()
print('Muito prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é {}'.format(nome[0] ))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))

#tempo do seu carro com condição
tempo=int(input('Quantos anos tem seu carro ? '))
print('Carro novo'if tempo<3 else'carro velho')
print('--FIM--')

#EXEMPLO
nome= str(input('Qual seu nome? ')).strip()
if nome == 'Luan':
    print('Que nome bonito voce tem!')

else: 
    print('Bom dia, {}'.format(nome))

#jogo de advinhação
from random import randint
computador = randint(0,10)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar ... ')
jogador = int(input('Em que numero eu pensei? '))
print('Processando...')
print('-=-'*100)
msg="O numero escolhido foi {} ".format(computador)
print(msg)
if jogador == computador:      
    print('Voce Acertou')
else:
    print('Voce errou')

#radar eletronico
velocidade = float(input('Qual a velocidade do Carro? '))
multa = (velocidade-80) * 7

if velocidade > 80:
    print('Voce Foi multado em R${:.2f} '.format(multa))

if velocidade < 80: 
    print('Voce esta dentro do limite permitido boa viagem')  

#par ou impar
numero = (int(input('Me diga um numero ')))
resultado = numero % 2 
if resultado == 0:
    print('par')
else:
    print('Impar')

#calculando passagem de uma viagem 
distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a Viajar {}km'.format(distancia))

preço = distancia *0.50 if distancia < 200 else distancia *0.45

'''if distancia < 200 :
    preço = distancia * 0.50
else:  
    preço = distancia * 0.45'''

print('O preço da sua passagem será de R${:.2f}'.format(preço))

#calculo de ano bissexto
ano = int(input('Que ano quer analisar?'))

if ano == 0 :
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))

else:
    print('O ano de {} Não é bissexto'.format(ano))

#calculo menor valor
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))

if primeiro<segundo and primeiro<terceiro:
    menor = primeiro 

if segundo<primeiro and segundo<terceiro:
    menor = segundo

if terceiro<primeiro and terceiro<segundo:
    menor = terceiro


print('O menor valor digitado foi {} '.format(menor))

#aumento de multiplos
salario = float(input('Qual o Seu salario ?'))

if salario < 1250:
    novo = salario + (salario * 15/100)
else :
    novo = salario + (salario * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))

#analisando triangulo
print('-='*50)
print('Analisador de Triangulos ')
print('-='*50)
r1 = float(input('Primeiro seguimento '))
r2 = float(input('Segundo seguimento '))
r3 = float(input('Terceiro seguimento '))

if r1 < r2 +r3 and r2 <r1 +r3 and r3 < r1 +r2 :
    print('Os segmentos acima PODEM FORMAR o triangulo')
else :
    print('Os seguementos aciman nao podem formar o triangulo')


#usando elif
nome = str(input('Qual é o seu nome ? '))
if nome == 'Gustavo' :
        print('que nome bonito')
elif nome == 'Luan' or nome == 'Paulo':
    print('Seu nome é popular')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que nome bonito')
else: 
    print('Seu nome é bem normal ')
print ('Tenha um bom dia {}'.format(nome))

#aprovando emprestimo
casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salario? '))
anos = int(input('Quantos anos pretende pagar? '))
minimo = salario * 30 / 100 
prestação = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa,anos),end='')
print ('a prestação será de R${:.2f}'.format(prestação))
if prestação < minimo:
    print('emprestimo pode ser CONCEDIDO!')
else:
    print('emprestimo NEGADO')

#conversor de bases numericas
numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1]converter para BINARIO
[2]converter para OCTAL
[3]converter para HEXADECIMAL''')
opçao = int(input('Qual sua opção ? '))
if opçao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero,bin(numero)))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)))
else:
    print('Opção invalida. Tente novamente ')

#comparando numeros 
numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))

if numero1 > numero2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
    
#Alistamento Militar
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento : '))
idade = atual - nascimento
alistamento = 18
print('Quem nasceu em {} tem {} anos em {} '.format(nascimento,idade,atual))
if idade == 18:
    print('Voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 -  idade 
    print('Voce ainda nao pode se alistar seu alistamento deve ser em {} anos '.format (saldo))
elif idade > 18:
    saldo = idade - 18 
    print('Voce ja concluiu seu alistamento em {} anos '.format(saldo))

# Calculo classico de media 
nota1 = float(input('Qual a sua primeira nota ? '))
nota2 = float(input('Qual a sua segunda nota ? ' ))

media = (nota1+nota2) / 2


print('Sua media foi de {:.1f}'.format(media))

if media >= 7 :
    print('Aluno APROVADO')

elif media <5:
    print('Aluno REPROVADO')

elif media >=5 and media <7:
    print('Voce esta em recuperação ')

#calculando fatorial 
def fatorial (num):
    fat = 1
    if num == 0:
        return fat 
    

    for i in range(1, num + 1 ,1):
        fat *= i
    return fat

x = int(input('Digite um numero: '))

print(f'{x}! = {fatorial(x)}')

#exemplo de criação de arquivo 
def valida_int(pergunta,min,max):
    x  = int(input(pergunta))
    while((x < min) or (x > max )):
        x  = int(input(pergunta))
    return x

def existeArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
        a.close()

    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo{nomeArquivo} criado com sucesso\n')
    
def cadastarJogo (nomeArquivo,nomejogo,nomevideogame):
    try:
        a = open(nomeArquivo,'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write(f'{nomejogo};{nomevideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
       a = open(arquivo,'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado')
else:
    print('Arquivo inexistente')
criarArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar Cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada',1,3)
    if(op == 1): 
        print('Opção de cadastrar novo item selecionada')
        nomejogo = input('qual é o nome do jogo: ')
        nomevideogame = input('Qual nome do videogame: ')
        cadastrarjogo =(arquivo,nomejogo,nomevideogame)
    elif(op==2):
        print('Opção de listar selecionada ...')
        listarArquivo(arquivo)
    elif(op==3):
        print('Encerrando...')
        break   

#formando triangulo
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 =float(input('Terceiro segmento: '))

if r1< r2 +r3 and r2 < r1+ r3 and r3 <  r1+ r2:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    
    elif r1!=r2!=r3!=r1:
        print('ESCALENO')
    else :
        print('ISOCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR UM TRIANGULO !!!')

#calculo IMC
peso = float(input('Qual é o seu peso? (KG) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2) 

print('O IMC dessa pessoa é {:.1f} '.format(imc))

if imc < 18.5:
    print('Voce esta abaixo do PESO')
elif imc >= 18.5 and imc < 25:
        print('Voce esta no PESO IDEAL')
elif imc > 25 and imc < 30:
      print('Voce esta em SOBREPESO')
elif imc > 30 and imc < 40:
      print('Voce está com OBESIDADE')
elif imc > 40:
      print('Voce está com OBESIDADE MORBIDA')

#gerenciador de pagamento
print('{:=^40}'.format(' loja '))
preco = float(input('Preço das compras : R$ '))
print('''Formas de pagamento
      [1] A VISTA
      [2] A VISTA CARTAO
      [3] 2X NO CARTAO 
      [4] 3X OU MAIS NO CARTAO ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preco - (preco * 10/100)
    print('Sua compra foi a Vista')
elif opção ==2 :
    total = preco - (preco * 5/100)
    print('Sua compra foi no cartao a vista')
elif opção == 3:
    total = preco 
    parcela = total /2 
    print(f'Sua compra vai ser parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    total = preco + (preco * 20 /100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra sera parcelada em {totalparc}X de R${parcela:.2f} COM JUROS')
    print(f'sua compra de R${preco:.2f} vai custar R${total:.2f}')
else:
    total = 0
    print('opção invalida')

#contagem regressiva
from time import sleep
for cont in range(10,-1,-1):
    print(cont)
    sleep (1)
print('BUM! BUM! P00OW!')

#contagem de pares
import numbers  

for c in range(1,51):
    if c % 2 == 0:
     print(c,end=' ')
print('Acabou')

#soma impares multiplos de 3
soma = 0 
cont = 0 
for c in range (1,501,2):
    if c % 3==0:
        cont = cont + 1
        soma = soma + c 
print('A soma de todos os {} valores solicitados é {} '.format(cont,soma))

#tabuada 2.0
num = int(input('Digite um numero para ver a sua tabuada : '))
for i in range(1,11):
    print('{} x {:2} = {}'.format(num,i,num*i))

#soma dos pares 
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format (c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print('Voce informou {} numeros PARES e a soma foi {}'.format(cont,soma))

#Progressao aritmetica
primeiro=int(input('Digite o Primeiro termo : '))
razao=int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for i in range (primeiro,decimo,razao):
    print('{}'.format(i),end=' > ')
print('ACABOU')

#Numeros primos 
numero = int(input('Digite um numero: '))
tot = 0
for i in range (1,numero + 1):
    if numero % i == 0:
        print('\033[33m',end='')
        tot += 1 
    else:
        print('\033[31m',end='')
    print('{} '.format(i),end='')
print('\no Numero {} foi divisivel {} vezes'.format(numero,tot))
if tot == 2 :
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele não É PRIMO')

#Detector de Palindromo
frase=str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
for letra in range (len(junto)-1,-1,-1):
    invertido += junto[letra]
print('O inverso de {} é {} '.format(junto,invertido))
if invertido == junto :
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')

#Calculando maioridade 
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input('Em que ano a {}  pessoa nasceu?   '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
       totmenor += 1

print('Ao Todo Tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao Todo Tivemos {} pessoas menores de idade'.format(totmenor))

#Analisador completo
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho =''
totmulher20 = 0
for i in range (1,5):
    print('---{} Pessoa ---'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
        if sexo in 'Mm' and idade > maioridadehomem:
            nomevelho = nome
            if sexo in 'Ff' and idade > 20 :
                totmulher20 +=1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print(' Ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))

#Validção de dados
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))

#Variação Validação de dados
masc = fem = cont = 0 
while True : 
    sexo=str(input('Digite o sexo [M/F]:  ')).upper().strip()
    if sexo in'mM':
        masc += 1
        cont += 1
        print('Computado')
    elif sexo in 'fF':
        fem += 1
        cont += 1
        print('Computado') 
    else:
        print('Voce digitou errado, tente novamente')
        
    resp =str(input('Deseja continuar? [S/N]')).upper().strip()
    if resp in 'nN':
        print('saindo')
        break
    
print(f'Voce digitou {masc} masculinos e {fem} femininos com total de {cont} digitações')

#Jogo da advinhação 2.0 exemplo1
from random import randint
print('Vou pensar em um numero entre 0 e 10. tente advinhar...')
contador = 0
numero = randint(0,10)
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite?  '))
    contador += 1
    if jogador == numero:
        acertou=True
    else:
        if jogador < numero:
            print('Mais... tente mais uma vez')
        elif jogador > numero:
            print('Menos... tente mais uma vez')
print('Acertou com {} tentativas.'.format(contador))

#exemplo 2 
from random import randint
palpites = 0
computador = randint(0,10)
print('PC: Estou pensando em um numero de 0 a 10 qual é???')
while True:
    resposta=int(input('Digite um numero de 0 a 10: '))
    if resposta > computador:
        palpites +=1
        print('Voce chutou um valor maior')
    elif resposta < computador:
        palpites +=1
        print('Voce chutou um valor menor')
    elif resposta == computador:
        print(f'Voce acertou com {palpites} palpites')
        break

#Criando menu com opções
n1=int(input('Primeiro Valor:   '))
n2=int(input('Primeiro Valor:   '))
opção=0
while opção != 5:
    print('''    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opção=int(input('Qual é a sua opção?    '))
    if opção == 1:
        soma = n1+n2
        print('A soma ente {} + {} é {}'.format(n1,n2,soma))
    elif opção == 2:
        produto = n1*n2
        print('O resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opção == 3:
        if n1>n2:
            maior=n1
        else:
            maior = n2
        print('Entre o valor {} e {} o maior é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Informe os numeros novamente.')
        n1=int(input('Primeiro Valor:   '))
        n2=int(input('Primeiro Valor:   '))
    elif opção == 5:
        print('Finalizando')
    else:
        print('Opção invalida. tente novamente.')

print('Fim do programa.')

#Calculo Fatorial
#modo1 
import math
n = int(input('Digite um numero para calcular fatorial: '))
f = math.factorial(n)
print('O fatorial de {} é {}'.format(n,f))

#modo2
n = int(input('Digite um numero para calcular fatorial: '))
c = n
f = 1
while c > 0 :
    print('{}   '.format(c),end ='')
    print('x 'if c > 1 else ' = ', end='')
    f *=c
    c -= 1  
print('{}'.format(f))

#Progressao aritmetica 2.0
primeiro = int(input('Primeiro Termo:   '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1 
while cont <= 10:
    print('{}->'.format(termo), end="")
    termo += razao
    cont += 1 
print('FIM')

#Progressao aritmetica melhorada
primeiro = int(input('Primeiro Termo:   '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1 
total = 0 
mais = 10
while mais != 0:
    total=total+mais
    while cont <= total:
        print('{}->'.format(termo), end="")
        termo += razao
        cont += 1 
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais?  '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

#sequencia fibonacci
print('-'*30)
print('Sequencia de fibonacci')
print('-'*30)
n = int(input('Quantos termos voce quer mostrar? '))
t1=0
t2=1
print('~'*30)
print('{} -> {}'.format(t1,t2),end='')
cont = 3
while cont <=n :
    t3= t1+t2
    print(' -> {}'.format(t3),end='')
    t1=t2
    t2=t3
    cont +=1 
print('-> FIM')

#Tratando varios valores v1.0
num = cont = soma = 0 
num = int(input('Digite um numero (999 para parar): '))
while num != 999:
    soma += num 
    cont += 1
    num = int(input('Digite um numero (999 para parar): '))
print('Voce digitou {} numeros.'.format(cont,soma))

#Maior e menor valores
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1 
    if quant == 1:
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor:
            menor = num
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} e a media foi {} '.format(quant,media))
print('O maior valor foi {} e o menor foi {} '.format(maior,menor))

# numeros com flag
cont=soma=0
while True:
    num=int(input('Digite um numero ou 999 para sair:  '))
    if num == 999 :
        break
    soma+= num
    cont += 1 
print(f'Voce digitou {cont} numeros e a soma foi {soma}')

#tabuada com while true
while True:
    tab=int(input('Digite a tabuada que deseja consultar ou valor negativo para sair: '))
    if tab <=-1:
        break
    for cont in range (1,11):
        mult= tab*cont
        print(f'{tab} x {cont} = {mult}')  
    
#jogo do par ou impar
from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
print(f'Game over! Você venceu {vitorias} vezes.')

#analise de dados de grupo
tot18=totH=totM20=0
while True:
    idade= int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    while sexo not in 'MF':
        sexo= str(input('sexo: [M/F]')).strip().upper()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'M':
        totH+=1
    if sexo =='F' and idade <20:
        totM20+=1
    resp=' '
    while resp not in 'SN':
        resp= str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos:{tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'e Temos {totM20} Mulheres com menos de 20 anos ')

#Estatisticas em produtos
total=totmil=menor=cont=0
barato=' '
while True:
    nome = str(input('Qual o nome do produto: '))
    preco= float(input('Qual o preço do produto R$: '))
    cont+=1
    total+=preco
    if preco > 1000:
        totmil +=1
    if cont ==1:
        menor==preco
        barato=nome
    else:
        if preco < menor:
            menor = preco
            barato=nome
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} item custando mais de R$1000,00 R$')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

#simulador de caixa eletronico
print('='*30)
print('BANCO CENTRAL')
print('='*30)
valor=int(input('Qual valor quer sacar R$: '))
total= valor
ced=50
totced=0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced >0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced==50:
            ced = 20
        elif ced == 20:
            ced=10
        elif ced ==10:
            ced=1
        totced=0
        if total==0:
            break
print('='*30)
print('Volte sempre ao BANCO CENTRAL!')
print('='*30)

#Fim do Mundo 2
