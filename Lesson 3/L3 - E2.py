def human(Name, Surname, Patronymic, BornYear, Email, Tel_number):
    return f"{Surname} {Name} {Patronymic}, {BornYear} year born, Email: {Email}, Telephone number: {Tel_number}"

print(human(Name = input("Enter your name: "), Surname = input("Enter your surname: "),
            Patronymic = input("Enter your patronymic: "), BornYear = input("Enter your born year: "),
            Email = input("Enter your Email: "), Tel_number = input("Enter your telephone number: ")))
