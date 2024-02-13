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

    def __init__(self,dict):
        self.id = dict['_id']
        self.index = dict['index']
        self.date = dict['dataEMD']
        self.firstname = dict['nome/primeiro']
        self.lastname = dict['nome/último']
        self.age = int(dict['idade'])
        self.gender = dict['género'] == 'M'
        self.adress = dict['morada']
        self.sport = dict['modalidade']
        self.club = dict['clube']
        self.email = dict['email']
        self.federado = dict['federado'].lower() == 'true'
        self.result = dict['resultado'].lower() == 'true'



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

def parteIdade(idade,escalao = 5):
    # (20,5) -> 20-24, 22->20-24, (25)->25-29
    # (20,10) -> 20-29, (22,10)->20-29, (25,10)->20-29
    if escalao <= 1:
        return f"{idade}-{idade}"

    res = (idade // escalao) * escalao

    return f"{res}-{res+(escalao-1)}"

def distribuicaoIdades(athletes,step = 5):
    
    minAge = sys.maxsize
    maxAge = 0
    for athlete in athletes.values():
        if athlete.age > maxAge:
            maxAge = athlete.age
        if athlete.age < minAge:
            minAge = athlete.age
    
    dict = {}
    minAge = minAge - (minAge % step)
    while minAge <= maxAge:
        min
        code = parteIdade(minAge,escalao=step)
        dict[code] = 0
        minAge += step
    



    for athlete in athletes.values():
        code = parteIdade(athlete.age,escalao=step)
        dict[code] += 1

    for key,value in dict.items():
        if dict[key] == 0:
            del dict[key]


    return dict

def parseLine(line,headerdata):
    line = line.strip()
    data = line.split(',')
        
    dictLine = {}
    for i in range(len(headerdata)):
        dictLine[headerdata[i]] = data[i]
    
    return Atleta(dictLine)
        




def main():
    athletes = {}
    header = input().strip() # reads the header of csv file
    headerdata = header.split(',')

    
    # reading data from csv file
    for line in sys.stdin:
        atleta = parseLine(line,headerdata)
        athletes[atleta.id] = atleta



    sports = listSport(athletes)
    print("=== LISTA DE TODAS AS MODALIDADES ====")
    print(sports)

    aptos = percentagemAptos(athletes)
    naoAptos = 100 - aptos
    print("=== PERCENTAGEM DE ATLETAS APTOS ===")
    print("Aptos: {:.2f}%".format(aptos))
    print("Não Aptos: {:.2f}%".format(naoAptos))


    dist = distribuicaoIdades(athletes)
    x = len(dist)

    print("=== DISTRIBUIÇÃO DE IDADES (5 em 5 anos)===")
    for key, value in dist.items():
        print(f"{key}: {value} ({value/x})%")


    '''
    dist = distribuicaoIdades(athletes,2)

  
    print("=== DISTRIBUIÇÃO DE IDADES (2 em 2 anos)===")
    for key, value in dist.items():
        print(f"{key}: {value} ({value/x}%)")
    '''



if __name__ =="__main__":
    main()