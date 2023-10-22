dataset = list()


with open("C:/Users/MARTIM/Desktop/Dados/diabetes_prediction_dataset.csv","r") as csv:
    csv.readline()
    for line in csv:
        dataset.append(line.split(","))



def Destribution_gender(lista):
    female = 0
    male = 0
    for i in lista:
        if i[3]:
            if i[0] == "Female":
                female = female + 1
            else:
                male = male + 1
    print(female)
    print(male)
    sum = male + female
    male = (male/sum)*100
    female = (female/sum)*100

    print(f"Male: {"male:.0f}%,Female: {female:.0f}%")


def Destribution_age(lista):
    ages = list()
    for i in lista:
         if i[3]:
             ages.append(int(float(i[1])))

    age_ranges = [[0,10],[11,24]]

    i = 25
    while i <= 80:
          age_ranges.append([i, i+4])
          i = i + 5
    distribution = dict()
    for j in range(len(age_ranges)):
          distribution[j] = 0

    for j in ages:
          for l in age_ranges:
                if j in range(l[0],l[1]+1):
                      distribution[age_ranges.index(l)] = distribution[age_ranges.index(l)] + 1
                      break


    print("Age distribution\n")

    for j,k in zip(age_ranges,distribution.values()):
          print(f"{j} : {(k/len(ages))*100:.2f}%\n")


def Destribution_glucose(lista):
    glucose_levels = list()
    for i in lista:
        glucose_levels.append(int(i[7]))

    print(max(glucose_levels))

    glucose_destribution = dict()
    i = 0
    while(i <= max(glucose_levels)):
        glucose_destribution[i] = 0
        i = i + 10

    for i in glucose_levels:
        for j in glucose_destribution.keys():
            if i > j:
                continue
            else:
                glucose_destribution[j] = glucose_destribution[j] + 1
                break

    print(f"Blood glucose level\n")

    for i in glucose_destribution.keys():
        print(f"{i} :{(glucose_destribution[i]/len(glucose_levels))*100:.2f}%\n")
                 

    