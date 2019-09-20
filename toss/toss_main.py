
import random 

def choose_option(toss,weather,day):
    toss = toss.upper()
    weather = weather.upper()
    day = day.upper()
    
    if toss == 'LENGABURU':
        if weather == 'CLEAR' or day == 'DAY':
            return 'bats'
    elif toss == 'ENCHAI':
         if weather == 'CLOUDY' or day == 'NIGHT':
            return 'bats'
    return 'bowls'
        

if __name__ == '__main__':
    weather = input("Weather clear/cloudy: ")
    day = input("Day/Night: ")

    toss = random.choice(['Lengaburu','Enchai'])

    choice = choose_option(toss,weather,day)

    print('{} wins toss and {}'.format(toss,choice))

