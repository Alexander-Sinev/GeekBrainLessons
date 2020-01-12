season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}

month = int(input('Enter the month: '))

if(month == 12 or month == 1 or month == 2):
    print(season_list[0])
    print(season_dict.get(1))
elif(month == 3 or month == 4 or month == 5):
    print(season_list[1])
    print(season_dict.get(2))
elif(month == 6 or month == 7 or month == 8):
    print(season_list[2])
    print(season_dict.get(3))
elif(month == 9 or month == 10 or month == 11):
    print(season_list[3])
    print(season_dict.get(4))
