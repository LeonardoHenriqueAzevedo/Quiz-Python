score = 0

print("Seja bem Vindo Ao Quiz!")

answer = str(input("Você quer jogar?"))
answer_first = answer[0].upper()

while answer_first != "S":
    print("Seja bem Vindo Ao Quiz!")
    answer = str(
        input("Está afim agora de jogar?"))
    answer_first = answer[0].upper()

print("Ok, vamos jogar então!")
print("Você tem 1 tentativa para cada pergunta")

print("Qual o menor e o maior país do mundo?")
print("a) Vaticano e Rússia, b) Nauru e China, c) Mônaco e Canadá, d) Malta e Estados Unidos, e) São Marino e Índia")
first_question = str(input("Resposta: "))
first_question_corrected = first_question[0].upper()
if first_question_corrected != "A":
    print("Alternativa errada! Tente acertar a segunda questão.")
else:
    print("Alternativa correta, parabéns!")
    print("Vamos para a segunda questão")

print("Qual o livro mais vendido no mundo depois da Bíblia?")
print("a) O Senhor dos Anéis, b) Dom Quixote, c) O Pequeno Príncipe, d) Ela, a Feiticeira, e) Um Conto de Duas Cidades")
second_question = str(input("Resposta: "))
second_question_corrected = second_question[0].upper()
if second_question_corrected != "B":
    print("Alternativa errada! Tente acertar a terceira questão.")
else:
    print("Alternativa correta, parabéns!")
    print("Vamos para a terceira questão")

print("Quais os países que têm a maior e a menor expectativa de vida do mundo?")
print("a) Japão e Serra Leoa, b) Austrália e Afeganistão, c) Itália e Chade, d) Brasil e Congo, e) Estados Unidos e Angola")
third_question = str(input("Resposta: "))
third_question_corrected = third_question[0].upper()
if third_question_corrected != "A":
    print("Alternativa errada! Tente acertar a quarta questão.")
else:
    print("Alternativa correta, parabéns!")
    print("Vamos para a quarta questão")

print("Em que período da pré-história o fogo foi descoberto?")
print("a) Neolítico, b) Paleolítico, c) Idade dos Metais, d) Período da Pedra Polida, e) Idade Média")
fourth_question = str(input("Resposta: "))
fourth_question_corrected = fourth_question[0].upper()
if fourth_question_corrected != "B":
    print("Alternativa errada! Tente acertar a última.")
else:
    print("Alternativa correta, parabéns!")
    print("Vamos para a última questão")

print("Quem pintou o teto da capela sistina?")
print("a) Michelangelo, b) Leonardo da Vinci, c) Rafael, d) Sandro Botticelli, e) Donatello")
fifth_question = str(input("Resposta: "))
fifth_question_corrected = fifth_question[0].upper()
if fifth_question_corrected != "A":
    print("Alternativa errada!")
else:
    print("Alternativa correta, parabéns!")
