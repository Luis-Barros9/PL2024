import os
import sys

class Atleta:
    def __init__(self, id, index, date, firstname, lastname, age, gender, adress, sport, club, email, federado, result):
        self.id = id
        self.index = index
        self.date = date
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.adress = adress
        self.sport = sport
        self.club = club
        self.email = email
        self.federado = federado
        self.result = result


def listSport(athletes):
    sports =set()
    for athlete in athletes.values():
        sports.add(athlete.sport)
    
    
    return sorted(list(sports),key=str.lower)


def percentagemAptos(athletes):
    if len(athletes) == 0:
        return 0
    aptos = 0
    for athlete in athletes.values():
        if athlete.result:
            aptos += 1
    

    return (aptos / len(athletes)) * 100

def parteIdade(idade):
    # 20 -> 20-24, 22->20-24, 25->25-29
    res = idade // 5
    return f"{res*5}-{res*5+4}"

def distribuicaoIdades(athletes):
    
    minAge = sys.maxsize
    maxAge = 0
    for athlete in athletes.values():
        if athlete.age > maxAge:
            maxAge = athlete.age
        if athlete.age < minAge:
            minAge = athlete.age
    
    dict = {}

    while minAge <= maxAge:
        code = parteIdade(minAge)
        dict[code] = 0
        minAge += 5
    
    code = parteIdade(maxAge)
    dict[code] = 0

    
    for athlete in athletes.values():
        code = parteIdade(athlete.age)
        dict[code] += 1



    return dict

def main():
    athletes = {}
    header = input() # reads the header of csv file
    print(header)


    # reading data from csv file
    for line in sys.stdin:
        line = line.strip()
        data = line.split(',')
        id = data[0]
        index = data[1]
        date = data[2]
        firstname = data[3]
        lastname = data[4]

        age = int(data[5])

        gender = data[6] == 'M'

        adress = data[7]
        sport = data[8]
        club = data[9]
        email = data[10]
        federado = data[11].lower() == 'true'
    
        result = data[12].lower() == 'true'


        athletes[id] = Atleta(id, index, date, firstname, lastname, age, gender, adress, sport, club, email, federado, result)   

    sports = listSport(athletes)
    print("=== LISTA DE TODAS AS MODALIDADES ====")
    print(sports)

    aptos = percentagemAptos(athletes)
    naoAptos = 100 - aptos
    print("=== PERCENTAGEM DE ATLETAS APTOS ===")
    print("Aptos: {:.2f}%".format(aptos))
    print("Não Aptos: {:.2f}%".format(naoAptos))

    dist = distribuicaoIdades(athletes)
    print("=== DISTRIBUIÇÃO DE IDADES ===")
    for key, value in dist.items():
        print(f"{key}: {value}")



if __name__ =="__main__":
    main()