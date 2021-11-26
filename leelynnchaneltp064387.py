#Lee Lynn, Chanel
#TP064387
import os
import datetime
from datetime import date

def get_new_id(eid):
    with open("idgenerator.txt", "r") as f:
        line = f.readlines()  # reading one line
        rec = line[3].split("|")  # read one line in string form
    if eid == "AF":
        ind = 0
    elif eid == "BV":
        ind = 1
    elif eid == "CZ":
        ind = 2
    elif eid == "DM":
        ind = 3
    elif eid == "EC":
        ind = 4
    elif eid == "AV":
        ind = 5
    x = rec
    mylist = x
    nextid = mylist[ind].strip()
    newid = str(int(nextid[2:]) + 1)  # the 2nd index (3 character) + 1
    if len(newid) == 1:  # if the length of newid = 1
        nextid = nextid[:2] + "0000" + newid
    elif len(newid) == 2:
        nextid = nextid[:2] + "000" + newid
    elif len(newid) == 3:
        nextid = nextid[:2] + "00" + newid
    elif len(newid) == 4:
        nextid = nextid[:2] + "0" + newid
    elif len(newid) == 5:
        nextid = nextid[:2] + newid
    mylist[ind] = nextid.center(25) 
    rec = '|'.join(mylist)   # join can convert list back into string, joining new id with old record
    line[3] = rec
    with open("idgenerator.txt", "w") as fh:
        fh.writelines(line)
    return nextid

def new_registration():
    def vac_option1():
        print("-"*40 + "You are in the teenagers 12 to 18 age group."+ "-"*40)
        while True:
            print("1 - AF\n2 - CZ\n3 - DM")
            vacoption = input( "Please choose your preferred Covid-19 vaccination:" )
            if vacoption == '1':
                return vac(int(vacoption))
            elif vacoption == '2':
                return vac(int(vacoption == 4))
            elif vacoption == '3':
                return vac(int(vacoption == 2))
            else:
                print("Wrong input. Please re-enter.")
                while True:
                    print("1. Re-enter vaccination option.\n2. Back to main menu.\n3. Exit")
                    choice = input("Enter a choice:")
                    if choice == '1':
                        break
                    elif choice == '2':
                        return menu()
                    elif choice == '3':
                        exit()
                    else:
                        print("Wrong input. Please try again.")
                        continue
                continue

    def vac_option2():
        print( "-"*40+ "You are in the adult aged 18 and below 45 age group." + "-"*40)
        while True:
            print("1 - AF\n2 - BV\n3 - DM\n4 - EC\n5 - CZ")
            vacoption = input("Please choose your preferred Covid-19 vaccination:")
            if vacoption == '1' or vacoption == '2' or vacoption == '3' or vacoption == '4' or vacoption == '5':
                return vac(int(vacoption))
            else:
                print("Wrong input. Please re-enter.")
                while True:
                    print("1. Re-enter vaccination option.\n2. Back to main menu.\n3. Exit")
                    choice = input("Enter a choice:")
                    if choice == '1':
                        break
                    elif choice == '2':
                        return menu()
                    elif choice == '3':
                        exit()
                    else:
                        print("Wrong input. Please try again.")
                        continue
                continue

    def vac_option3():
        print("-"*40 + "You are in the adult above 45 age group."+ "-"*40)
        while True:
            print("1 - AF\n2 - BV\n3 - DM\n4 - EC\n")
            vacoption = input("Please choose your preferred Covid-19 vaccination:")
            if vacoption == '1' or vacoption == '2' or vacoption == '3' or vacoption == '4':
                return vac(int(vacoption))
            else:
                print("Wrong input. Please re-enter.")
                while True:
                    print("1. Re-enter vaccination option.\n2. Back to main menu.\n3. Exit")
                    choice = input("Enter a choice:")
                    if choice == '1':
                        break
                    elif choice == '2':
                        return menu()
                    elif choice == '3':
                        exit()
                    else:
                        print("Wrong input. Please try again.")
                        continue
                continue

    def time_slot1(vaccinedate):
        timeslot = "1. 10.15-13.15\n2. 13.25-16.25\n3. 16.35-19.35\n4. 19.45-22.45"
        while True:
            patients = 0
            print(timeslot)
            date_slot = input("Please select an available time slot:")
            if date_slot == '1':
                x = "10.15-13.15"
            elif date_slot == '2':
                x = "13.25-16.25"
            elif date_slot == '3':
                x = "16.25-19.25"
            elif date_slot == '4':
                x = "19.45-22.45"
            else:
                print('Wrong input, please try again.')
                continue
            vacdate = str(vaccinedate) + " " + x # here i concacinate 2 strings
            with open("id.txt"), "r") as fh:
                storedate = []
                index = 3
                line = fh.readlines()
                try:
                    for i in line:
                        readline = line[index] #it first read the 3rd line, then index += 2
                        storedate.append(readline.split("|")[4].strip())  # appending the value of the 4th column of id.txt file
                        index += 2 #incrementing index by 2
                except:
                    pass
            for i in range(len(storedate)):
                if storedate[i] == vacdate:
                    patients += 1
                i += 1
            #print("patient:", patients)
            if patients == 10: #once patients at a particular date and time slot reach 10, user need to re-input time slot
                print("Vaccine time slot on ", vaccinedate, "at", x, "is no longer available. Please try another time slot.")
                continue
            else:
                break
        with open("id.txt", "r") as fh:
            readline = fh.readlines()
            infoline = readline[len(readline) - 2].rstrip().split(
                "|")  # reading 4th last line of text file and stripping whitespace from 3rd line of txt file
            date = vacdate.center(30)
            infoline[4] = date  # have to fill up the 5th columns of txt file
            joins = '|'.join(infoline) +('\n') # join everything together
            readline[len(readline) - 2] = joins
            with open("id.txt"), "w") as fh:
                fh.writelines(readline)
        print("Registration completed. Thank you for your patience and time.\n Please ensure that you will show up on", vaccinedate, "at", x,"for your first dosage of vaccination.")
        print("="*(140))
        while True:
            choice = input("1. Main menu\n2. Exit\n3. Please select an option:")
            if choice == "1":
                return menu()
            elif choice =="2":
                exit()
            else:
                print('Wrong input, please try again.')
                continue

    def day_changing(start_date):
        tdelta = datetime.timedelta(days=1)
        tdelta2 = datetime.timedelta(days=4)
        limit = start_date + tdelta2
        start_date += tdelta
        initialdate = start_date
        while True:#user can only change their appointment date 4 times max
            start_date = initialdate 
            print("Would you like to have your first dose on", start_date, "?")
            for index in range(3):
                print("1. Yes, I confirm.\n2. No, I would like to choose another date.")
                choice = input("Option:")
                if choice == '1':
                    return time_slot1(start_date)
                elif choice == '2':
                    start_date += tdelta
                    index += 1
                    print("Would you like to have your first dose on", start_date, "?")
                else:
                    print("Wrong input, please re-enter.")
                    continue
            print("Patients are only allowed to change their vaccination appointment up to 4 times. Please select a date from", initialdate, "till", limit)
            print("-"*140)
            index = 0
            continue
           
    def date_confirmation(response):
        tdelta = datetime.timedelta(days=14)
        available_vac = datetime.date.today()
        while True:
            userinput = input(response)
            if userinput == '1':
                pass
            elif  userinput == '2':
                available_vac = available_vac + tdelta
            else:
                print("Wrong input, please try again.")
                print("Would you like to have your vaccine within this week or after this week?")
                print("1. This week.\n2. After this week.")
                continue
            while True:
                print("Would you like to have your first dose on", available_vac, "?")
                print("1. Yes, I confirm.\n2. No, I would like to choose another date.")
                choice = input("Option:")
                if choice == '1':
                    return time_slot1(available_vac)
                elif choice == '2':
                    return day_changing(available_vac)
                else:
                    print("Wrong input, please try again.")
                    continue
            
    def vac(vacoption):
        if vacoption == 1:  #1 - AF\n2 - BV\n3 - DM\n4 - EC\n5 - CZ
            print("-"*60+ "AF vaccination appointment"+ "-"*60)
            vacid = get_new_id("AF")
            id = "AFVAC"
        elif vacoption == 2:
            print("-"*60+"BV vaccination appointment" +"-"*60)
            vacid = get_new_id("BV")
            id = "BVVAC"
        elif vacoption == 3:
            print("-"*60+"DM vaccination appointment"+ "-"*60)
            vacid = get_new_id("DM")
            id = "DMVAC"
        elif vacoption == 4:
            print("-"*60+"EC vaccination appointment"+ "-"*60)
            vacid = get_new_id("EC")
            id = "ECVAC"
        else:
            print("-"*60+ "CZ vaccination appointment"+ "-"*60)
            vacid = get_new_id("CZ")
            id = "CZVAC"
        print("Your patient ID is:", vacid)
        with open("vaccination.txt", "r") as fh, open("id.txt"), "r" )as f:
            readline = fh.readlines() # for vaccination.txt
            readline2 = f.readlines() # for id.txt
            seclastline = readline[len(readline)-2].rstrip().split("|") #reading 2nd last line of text file and stripping whitespace from 3rd line of txt file
            seclastline2 = readline2[len(readline2)-2].rstrip().split("|")
            patientid = vacid.center(20)
            vaccineid = id.center(20)
            seclastline[1] = patientid #have to fill up the 2nd columns of txt file
            join = '|'.join(seclastline) #join everything together
            readline[len(readline) - 2] = join
            seclastline[6] = vaccineid
            join = '|'.join(seclastline) +('\n')    # join everything together
            readline[len(readline) - 2] = join
            with open("vaccination.txt", "w") as fh, open("id.txt", "w") as f:
                fh.writelines(readline)
                seclastline2[2] = patientid.center(20)
                join = ('|').join(seclastline2) +('\n')
                readline2[len(readline) - 2] = join
                f.writelines(readline2)
        print("Would you like to have your vaccine within this week or after this week?")
        print("1. This week.\n2. After this week.")
        response = date_confirmation("Option:")

    def get_alpha(prompt, shortest=2, longest=20):
        while True:
            response = input(prompt)
            if shortest <= len(response) <= longest:
                if response.isalpha() and not response.isspace():
                    return response
                else:
                    print("Invalid characters, please enter alphabetic input only.")
            else:
                print(f'Name should be between {shortest} and {longest} characters long')

    def name():
        first_name = get_alpha("First name:")
        last_name = get_alpha("Last name:")
        username = first_name.upper() + " " + last_name.upper()
        print("Hello", username,", Welcome to Malaysia's official Vaccination Administartion Centre.")
        print("-"*90)
        
        return username

    def validcheck(userinput):
        valdigit = "0123456789-"
        for character in userinput:
            if character not in valdigit:
                return False
        return True

    def validNumber(prompt, shortest=13, longest=14):
        country_code = "601"
        country_code2 = "6011"
        while True:
            userinput = input(prompt)
            if len(userinput) == shortest and userinput[3] != '1':
                for index in range(13):
                    if index in [4, 8]:
                        if userinput[index] != '-':
                            print("Please enter valid input in accordance with the given format.")
                            return user_contact()
                    elif userinput[:3] != country_code:
                        print("Please enter the correct Malaysia's country code.")
                        return user_contact()
                    elif not validcheck(userinput):
                        print("Invalid characters, please enter numerical input only.")
                        return user_contact()
                print("Valid contact number")
                print("-"*90)
                return userinput
            elif len(userinput) == longest and userinput[:4] == country_code2:
                for index in range(14):
                    if index in [4, 9]:
                        if userinput[index] != '-':
                            print("Please enter valid input in accordance with the given format.")
                            return user_contact()
                    elif userinput[:4] != country_code2:
                        print("Please enter the correct Malaysia's country code.")
                        return user_contact()
                    elif not validcheck(userinput):
                        print("Invalid characters, please enter numerical input only.")
                        return user_contact()
                print("Valid contact number")
                print("-"*90)
                return userinput
            else:
                print(f'Must be either {shortest} or {longest} characters long')

    def user_contact():
        phone_number = validNumber('Please enter your phone number in the format of 601X-XXX-XXXX/ 6011-XXXX-XXXX: ')
        return phone_number

    def validBirthdate(prompt):
        birth_date = input(prompt)
        today = datetime.date.today()
        try:
            day, month, year = birth_date.split('/')
        except ValueError:
            print("Please enter valid input in accordance to the given format.")
            return userage()
        try:
            birthday = datetime.date(int(year), int(month), int(day))
            valid = True
        except ValueError:
            print("Invalid date, please try again.")
            return userage()
        while valid:
            age = today.year - birthday.year
            if age < 0 or age > 160:
                print("Invalid year, please try again")
                return userage()
            elif age < 12:
                print("No vaccination available for children below 12.")
                while True:
                    print("1. Re-enter age.\n2. Back to main menu.\n3. Exit")
                    choice = input("Enter a choice:")
                    if choice == '1':
                        return userage()
                    elif choice == '2':
                        return menu()
                    elif choice == '3':
                        exit()
                    else:
                        print("Wrong input. Please try again.")
                        continue
            else:
                print("Valid date of birth")
                print("-"*90)
                return birth_date

    def userage():
        birth_date = validBirthdate("Please enter your date of birth in the format of DD/MM/YYYY:")
        return birth_date

    def valid_ic(prompt):
        while True:
            input_ic = input(prompt)
            while len(input_ic) == 14:  # 990429-04-5224
                for index in range(14):
                    if index in [6, 9]:
                        if input_ic[index] != '-':
                            print("Please enter valid input in accordance to the given format.")
                            return user_ic()
                if not validcheck(input_ic):
                    print("Invalid characters, please enter numerical input only.")
                    return user_ic()
                else:
                    print("Valid IC")
                    print("-"*90)
                    return input_ic
            print("Identity card's number has to be 13 digits long. Please re-enter.")
            continue
    
    def user_ic():
        input_ic = valid_ic("Please enter your identity card's number the format of xxxxxx-xx-xxxx:")
        return input_ic
        
    def email_val():
        while True:
            email = input("Please enter your email address:")
            error = 0
            if email[0].isalpha():
                for index in range(1, len(email)):
                    if email[index].isalpha() or email[index].isalnum() or email[index] == '.':
                        #print(email[i])
                        continue
                    else:
                        if email[index] == '@':
                            error = 1
                            break
                        else:
                            error = -1
                            break
            else:
                error = -1
            if error == -1: #not valid
                print("Invalid email, please try again.")
                continue
            elif error == 1:
                substr = email[index:len(email)]
                if substr == '@gmail.com' or substr == '@hotmail.com' or substr == '@edu.my':
                    print("Valid email")
                    return email
                else:
                    print("Invalid email, please try again.")
                    continue
            else:
                print("Invalid email, please try again.")
                continue

    def storingdata():
        newpatient = name()
        newcontact = user_contact()
        newbirth = userage()
        newic = user_ic()
        newemail = email_val()
        patientid = " "
        currentyear = date.today().year
        useryear = int(newbirth[6:])
        currentdate = date.today()
        age = currentyear - useryear
        vaccinecode = " "
        status = "NEW"

        if age >= 12 and age <= 18:
            vccentre = "Putrajaya VC centre"
        elif age >= 18 and age <= 45:
            vccentre = "Putrajaya VC centre"
        elif age >= 45 and age <= 160:
            vccentre = "KL VC centre"

        with open("vaccination.txt", "a") as fh:
            rec = []
            rec.append([newpatient, patientid, newcontact, newbirth, newic, newemail, vaccinecode,  status, vccentre])
            for i in range(len(rec)):
                patientlist = str(rec[i][0].center(20) + "|" + rec[i][1].center(20) + "|" + rec[i][2].center(20) + "|"
                                  + rec[i][3].center(20) + "|" + rec[i][4].center(20) + "|" + rec[i][5].center(35) + "|"
                                  + rec[i][6].center(20) + "|" + rec[i][7].center(20) + "|" + rec[i][8].center(20) + "|")
            fh.write(patientlist + "\n" + "-" * 204 + "\n")

        with open("id.txt", "a") as fh:
            rec = []
            rec.append([newpatient, str(currentdate), patientid, status, " "*30, " "*30, vccentre])
            #print(rec)
            numberofrecord = len(rec)
            for i in range(numberofrecord):
                patientlist = str(rec[i][0].center(20) + "|" + rec[i][1].center(20) + "|" + rec[i][2].center(20) + "|"
                              + rec[i][3].center(20) + "|" + rec[i][4].center(30) + "|" + rec[i][5].center(30) + "|"
                              + rec[i][6].center(20) + "|")
            fh.write(patientlist + "\n" + "-" * 168 + "\n")

        if age >= 12 and age <= 18:
            vac_option1()
        elif age >= 18 and age <= 45:
            vac_option2()
        elif age >= 45 and age <= 160:
            vac_option3()

    # main logic of new registration starts here
    storingdata()

def vaccine_admin():
    def new_registration():
        def get_alpha(prompt, shortest=2, longest=20):
            while True:
                response = input(prompt)
                if shortest <= len(response) <= longest:
                    if response.isalpha() and not response.isspace():
                        return response
                    else:
                        print("Invalid characters, please enter alphabetic input only.")
                else:
                    print(f'Must be between {shortest} and {longest} characters long')

        def name():
            first_name = get_alpha("First name:")
            last_name = get_alpha("Last name:")
            print("Hello", first_name, last_name)
            username = first_name.upper() + " " + last_name.upper()
            return username

        def valid_password(prompt):
            specialchar = ['@', '#', '$', '%', '&', '*']
            while True:
                password = input(prompt)
                if len(password) < 8:
                    print("Password length should consist of at least 8 characters")
                    continue
                elif len(password) > 18:
                    print("Password length should consist of not more than 18 characters")
                    continue
                elif not any(char.isupper() for char in password):
                    print("Password  should consist of at least one uppercase letter.")
                    continue
                elif not any(char.islower() for char in password):
                    print("Password should consist of at least one lowercase letter.")
                    continue
                elif not any(char.isdigit() for char in password):
                    print("Password should contain at least one numerical characters. Please try again.")
                    continue
                elif not any(char in specialchar for char in password):
                    print("Password should contain  at least one special characters. Please try again.")
                    continue
                else:
                    return password

        def staff_password():
            print("--------Characteristics of a strong password.--------\n1. Consists of both uppercase and lowercse letters.\n2. Should consists of"
                  "at least one numerical number.\n3. At least more than "
                  "8 and not more than 18 characters.\n4. Inclusion of at least one special characters '@', '#', '$', '%', '&', '*'. \n"+ "-"*50)
            staffpass = valid_password("Please create a strong password for your staff account:")
            return staffpass

        def storing_data():
            newstaff = name()
            staffid = get_new_id("AV")
            currentdate = str(date.today())
            password = staff_password()
            print("Your staff ID:", staffid, "\nYour password is:", password, "\nYou will need your staff ID and password to login the adminsitration "
            "system.")
            with open("staffdata.txt", "a") as fh:
                rec = []
                rec.append([staffid, newstaff, currentdate, password])
                print(rec)
                numberofrecord = len(rec)
                for i in range(numberofrecord):
                    patientlist = str(
                        rec[i][0].center(25) + "|" + rec[i][1].center(25) + "|" + rec[i][2].center(25) + "|"
                        + rec[i][3].center(25) + "|")
                fh.write(patientlist + "\n" + "-" * 104 + "\n")
            return admin_menu()

        # main logic of new_registration() function
        storing_data()

    def login():
        def loginid():
            id = input("Please enter your staff ID:")
            with open("staffdata.txt", "r") as fh:
                store = []
                index = 3
                line = fh.readlines()
                try:
                    for i in line:
                        readline = line[index]  # it first read the 3rd line, then index += 2
                        store.append(
                            readline.split("|")[0].strip())  # appending the value of the 1st column of id.txt file
                        index += 2  # incrementing index by 2
                except:
                    pass
            val = 0
            for i in range(len(store)):
                if store[i] == id:
                    val += 1
                i += 1
            while True:
                if val == 0: #to check if the id is stored in staff data file
                    choice = input("ID is not registered. Would you like to register?\n1. Yes. \n2. No, I would like to re-enter my ID\nOption:")
                    if choice == '1':
                        return new_registration()
                    elif choice == '2':
                        return login()
                    else:
                        print("Wrong input. Please try again.")
                        continue
                else:
                    print("Valid ID")
                    return loginpass(id)

        def loginpass(id):
            while True:
                staffpass = input("Please enter your password:")
                validpass = id + staffpass
                with open("staffdata.txt", "r") as fh:
                    store = []
                    index = 3
                    line = fh.readlines()
                try:
                    for i in line:
                        readline = line[index]  # it first read the 3rd line, then index += 2
                        store.append(
                            readline.split("|")[0].strip() + readline.split("|")[3].strip())  # appending the value of the 1st column and 4th column of id.txt file, then concatenate them together
                        index += 2  # incrementing index by 2
                except:
                    pass
                val = 0
                for i in range(len(store)):
                    if store[i] == validpass:
                        val += 1
                    i += 1
                if val == 0:
                    print("Wrong password. Please try again.")
                    continue
                else:
                    print("Login successful.")
                    return admin_patientsmenu()

        # main logic of login() function
        loginid()

    def admin_patientsmenu():
        while True:
            print("1 - Administer patients vaccination record")
            print("2 - Search Patient Record and Vaccination Status")
            print("3 - Statistical Report of Vaccinated Patients")
            print("4 - Back")
            admin_option = input("Please select an option:")
            if admin_option == '1':
                return management()
            elif admin_option == '2':
                while True:
                    choice = input("1. Show all patients vaccination record.\n2. Search patient's vaccine infomation.\nPlease select an option:")
                    if choice == '1':
                        return all_patients()
                    elif choice == '2':
                        return search_patient()
                    else:
                        print("Wrong input. Please try again.")
                        continue
            elif admin_option == '3':
                return statistic()
            elif admin_option == '4':
                return admin_menu()
            else:
                print('Wrong input. Please try again.')
                continue
    
    def change_field(line):
        column = 0
        while True:
            print("Which field would you like to modify?")
            field = input("1. Name\n2. Status\n3. First dose date\n4. Second dose date\n5. Vaccination Centre\nSelect a field:")
            if field == '1':
                column = 0
                column2 = 0
                while True:
                    new_value = input("Please enter new value:").center(20).upper()
                    if not any(char.isalpha() for char in new_value):
                        print("Please enter alphabetic characters only.")
                        continue
                    else:
                        break
                break
            elif field == '2':
                column = 3
                column2 = 7
                while True:
                    choice = input("1. New\n2. Completed-D1\n3. Completed-D2\nChoose an option:")
                    if choice == '1':
                        new_value = 'NEW'.center(20)
                    elif choice == '2':
                        new_value = 'COMPLETED-D1'.center(20)
                    elif choice == '3':
                        new_value = 'COMPLETED-D2'.center(20)
                    else:
                        print("Wrong input, please try again.")
                        continue
                    break
                break
            elif field == '3' or field == '4':
                if field == '3':
                    column = 4 #only for id.txt file
                else:
                    column = 5
                while True:
                    new_value = input("Please enter a new value in the format of DD/MM/YYYY:")
                    try:
                        day, month, year = new_value.split('/')
                    except ValueError:
                        print("Please enter valid input in accordance to the given format.")
                        continue
                    try:
                        value = str(datetime.date(int(year), int(month), int(day)))
                        break
                    except ValueError:
                        print("Invalid date, please try again.")
                        continue
                while True:
                    date_slot = input("1. 10.15-1.15\n2. 13.25-16.25\n3. 16.25-19.25\n4. 19.45-22.45\nPlease select a time slot:")
                    if date_slot == '1':
                        time = " 10.15-13.15"
                    elif date_slot == '2':
                        time = " 13.25-16.25"
                    elif date_slot == '3':
                        time = " 16.25-19.25"
                    elif date_slot == '4':
                        time = " 19.45-22.45"
                    else:
                        print('Wrong input, please try again.')
                        continue
                    break
                new_value = (value + time).center(30)
                break
            elif field == '5':
                column = 6
                column2 = 8
                while True:
                    choice = input("1. KL vaccination centre\n2. Putrajaya vaccination centre\nPlease select an option:")
                    if choice == '1':
                        new_value = "KL VC centre".center(20)
                        break
                    elif choice == '2':
                        new_value = "Putrajaya VC centre".center(20)
                        break
                    else:
                        print("Wrong input, please try again.")
                        continue
                break
            else:
                print("Wrong input, please try again.")
                continue
        with open("id.txt", "r") as fh:
            readline = fh.readlines()
            linenum = readline[line].rstrip().split('|') #specific line of the textfile
            linenum[column] = new_value #replace specific column in a line with 'new_value' variable
            join = '|'.join(linenum)+'\n' #joining | 
            readline[line] = join #specific line in a text file
            with open("id.txt", "w") as fh:
                fh.writelines((readline))
        if field == '3' or field == '4':
             admin_patientsmenu()
        else:
            with open("vaccination.txt", "r") as f:
                readline = f.readlines()
                linenum = readline[line].rstrip().split('|') #specific line of the textfile
                new_value = new_value
                linenum[column2] = new_value #replace specific column in a line with 'new_value' variable
                join = '|'.join(linenum)+'\n' #joining | 
                readline[line] = join #specific line in a text file
                with open("vaccination.txt", "w") as fh:
                    fh.writelines((readline))
        admin_patientsmenu()

    def admin_vaccine(linenum):
        currentday = date.today()
        delta = datetime.timedelta(days=14) 
        delta2 = datetime.timedelta(days=21) 
        delta3 = datetime.timedelta(days=28) 
        with open("id.txt", "r") as fh:
            rec = []
            readline = fh.readlines()
            rec.append(readline[linenum].strip().split('|'))
        patientvac = rec[0][2].strip()  #rec save 2 arrays 
        d1 = rec[0][3].strip()
        while True:
            print("Which dosage would you like to administer?")
            dose = input("1. First dose\n2. Second dose\nSelect a field:")
            if dose == '1':
                if d1 == 'NEW':
                    while True:
                        if str(patientvac[:2]) != "EC":
                            print("Patient completed first dose of vaccination.")
                            date_slot = input("1. 10.15-1.15\n2. 13.25-16.25\n3. 16.25-19.25\n4. 19.45-22.45\nPlease select an available second doze time slot for patient:")
                            if date_slot == '1':
                                time = " 10.15-13.15"
                            elif date_slot == '2':
                                time = " 13.25-16.25"
                            elif date_slot == '3':
                                time = " 16.25-19.25"
                            elif date_slot == '4':
                                time = " 19.45-22.45"
                            else:
                                print('Wrong input, please try again.')
                                continue
                        else: 
                            break
                        break
                elif d1 == 'COMPLETED-D1':
                    print("Patient has received first dose of vaccination.")
                    continue
                else:
                    print("Patient is fully vaccinated.")
                    print("-"*60)
                    return admin_patientsmenu()
            elif dose == '2':
                if d1 == 'NEW':
                    print('First dose is required to be administered before the second dose.')
                    continue
                elif str(patientvac[:2]) == "EC" and d1 == 'COMPLETED':
                    print('EC Vaccination will only need one dose.')
                    continue
                else:
                    print("Second doze completed.")
                    break
            else:
                print('Wrong input, please try again.')
                continue
            break
                    
        if dose == '1':
            with open("id.txt", "r") as f:
                readline = f.readlines()
                line = readline[linenum].rstrip().split('|') #specific line of the textfile in accordance with the patient id given
                status = "COMPLETED-D1".center(20)
                if str(patientvac[:2]) != "EC":
                    if str(patientvac[:2]) == "AF":
                        dose2 = currentday + delta
                    elif str(patientvac[:2]) == "BV" or str(patientvac[:2]) == "CZ":
                        dose2 = currentday + delta2
                    elif str(patientvac[:2]) == "DM":
                        dose2 = currentday + delta3
                    dose2date = str(dose2) + time
                else:
                    dose2date = '1 DOSE ONLY'
                    status = "COMPLETED".center(20)
                line[3] = status #replace 4th column in a line with 'status' variable
                line[5] = str(dose2date).center(30) #replace 6th column in a line with 'dose2date' variable
                join = '|'.join(line)+'\n' #joining | 
                readline[linenum] = join #specific line in a text file
                with open("id.txt", "w") as f:
                    f.writelines((readline))
            with open("vaccination.txt", "r") as fh:
                readline = fh.readlines()
                line = readline[linenum].rstrip().split('|') #specific line of the textfile in accordance with the patient id given
                line[7] = status.center(20)
                join = '|'.join(line)+'\n' #joining | 
                readline[linenum] = join #specific line in a text file
                with open("vaccination.txt", "w") as fh:
                    fh.writelines((readline))
            return admin_patientsmenu()
        elif dose == '2':
            with open(id.txt", "r") as f, open("vaccination.txt", "r") as fh:
                readline = f.readlines()
                readline2 = fh.readlines()
                line = readline[linenum].rstrip().split('|') #specific line of the textfile in accordance with the patient id given
                line2 = readline2[linenum].rstrip().split('|') 
                status = "COMPLETED".center(20)
                line[3] = status
                line2[7] = status
                join = '|'.join(line)+'\n' #joining | 
                join2 = '|'.join(line2)+'\n' #joining | 
                readline[linenum] = join #specific line in a text file
                readline2[linenum] = join2
                with open("id.txt", "w") as f:
                    f.writelines((readline))
                with open("vaccination.txt", "w") as fh:
                    fh.writelines((readline2))
            return admin_patientsmenu()

    def management():
        while True:
            search = input("Please enter patient ID:")
            with open("id.txt", "r") as fh:
                line = fh.readlines()
                store = []
                index = 3
                try:
                    for i in line:
                        readline = line[index]  # it first read the 3rd line, then index += 2
                        store.append(
                        readline.split("|")[2].strip())  # appending the value of the 1st column of id.txt file
                        index += 2  # incrementing index by 2
                except:
                    pass   
            read = 3 #3rd line
            found = 0
            for i in range(len(store)):
                if store[i] == search:
                    found = 1
                    print(store[i])
                    break
                else:
                    read += 2
                i += 1     
            if found == 0:
                print("Patient ID not found. Please try again.")
                continue
            else:
                print("Valid ID")
                for i in line[:3]: #to display the 1st 3 lines of text
                    print(i)
                print(line[read])
                while True:
                    option = input("Would you like to administer patient vaccination dosage or modify patient's information?\n1. Administer patient vaccination dosage.\n2. Modify Patient Information\nEnter an option:")
                    if option == '1':
                        return admin_vaccine(read)
                    elif option == '2':
                        return change_field(read)
                    else:
                        print('Wrong input, please try again.')
                        continue
                    
    def all_patients():
        with open("id.txt", "r") as fh:
            line = fh.readlines()
            for index in line:
                print(index)
            return admin_patientsmenu()

    def search_patient():
        search = id_check("Please enter patient ID:")
        return admin_patientsmenu()

    def statistic():
        with open("idgenerator.txt", "r") as fh:
            rec = []
            line = fh.readlines()
            rec.append(line[3].rstrip().split('|'))
            af = rec[0][0].strip()
            bv = rec[0][1].strip()
            cz = rec[0][2].strip()
            dm = rec[0][3].strip()
            ec = rec[0][4].strip()
            statistic = "Number of patients with AV vaccination:" + str(int(af[2:])) + "\nNumber of patients with BV vaccination:" + str(int(bv[2:]))  + "\nNumber of patients with CZ vaccination:" + str(int(cz[2:]))  + "\nNumber of patients with DM vaccination:" + str(int(dm[2:]))  + "\nNumber of patients with EC vaccination:" + str(int(ec[2:]))
            print(statistic)
        with open("id.txt", "r") as fh:
            line = fh.readlines()
            list = []
            index = 3
            new = 0
            d1 = 0
            d2 = 0
            try:
                for i in line:
                    readline = line[index]  # it first read the 3rd line, then index += 2
                    list.append(readline.split("|")[3].strip())  # appending the value of the 1st column of id.txt file
                    index += 2  # incrementing index by 2
            except:
                pass   
            #print(list)
            for i in range(len(list)):
                if list[i] == 'NEW':
                    new +=1 
                elif list[i] == 'COMPLETED-D1':
                    d1 +=1 
                else:
                    d2 +=1
            print("Numbers of new patient:", new)
            print("Numbers of patient waiting for second dose:", d1)
            print("Numbers of fully vaccinated patient:", d2)
            return admin_patientsmenu()

    def admin_menu():
        while True:
            print("-"*15 + "Covid-19 vaccine administration" + "-"*15)
            print("1 - Login")
            print("2 - New administration staff registration")
            print("3 - Back")
            admin_option = input("Please select an option:")
            if admin_option == '1':
                return login()
            elif admin_option == '2':
                return new_registration()
            elif admin_option == '3':
                return menu()
            else:
                print("Wrong input. Please try again.")
                continue

    admin_menu()

def id_check(id):
    while True:
            search = input(id)
            with open("id.txt", "r") as fh:
                line = fh.readlines()
                store = []
                index = 3
                try:
                    for i in line:
                        readline = line[index]  # it first read the 3rd line, then index += 2
                        store.append(
                        readline.split("|")[2].strip())  # appending the value of the 1st column of id.txt file
                        index += 2  # incrementing index by 2
                except:
                    pass   
            read = 3 #3rd line
            found = 0
            for i in range(len(store)):
                if store[i] == search:
                    #print("STORE:",store)
                    found = 1
                    break
                else:
                    read += 2
                i += 1     
            if found == 0:
                print("Patient ID not found. Please try again.")
                continue
            else:
                print("Valid ID")
                for i in line[:3]:
                    print(i)
                print(line[read])
                return read

def record():
    search = id_check("Please enter patient ID:")
    with open("id.txt", "r") as fh:
        line = fh.readlines()
        store = []
        store.append(line[int(search)].split("|"))
    status = store[0][3].strip()
    d1 = store[0][4].strip()
    d2 = store[0][5].strip()
    if status != 'NEW' and status != "COMPLETED-D2":
        print("Your second dose date is on", d2, ". Please ensure to show up on that day.")
    elif status == 'NEW':
        print("Your first dose date is on", d1, "\nPlease ensure to show up on that day.")
    else:
        print("You are fully vaccinated.")
    return menu()

def menu():
    while True:
        print("-"*40+ "Welcome to Malaysia's official Covid-19 Vaccination Administration Centre"+ "-"*40)
        print("1 - New Patient Registration")
        print("2 - Vaccine Administration")
        print("3 - Search Patient Record and Vaccination Status")
        print("4 - Quit")
        option = input("Please select an option:")
        if option == '1':
            print("-"*46+"New patient registration for Covid 19 vaccination"+ "-"*46)
            new_registration()
        elif option == '2':
            vaccine_admin()
        elif option == '3':
            while True:
                choice = input("1. Patient\n2. Administrative staff\nPlease select an option")
                if choice == '1':
                    return record()
                elif choice == '2':
                    print("Please log in to the system.")
                    return vaccine_admin()
                else:
                    print("Wrong input, please try again.")
                    continue
        elif option == '4':
            exit()
        else:
            print("Wrong input. Please try again.")
            continue

def write_txtfile():
    with open("vaccination.txt", "w") as fh:
        intro = str(
            "=" * 204 + "\n" + "Name".center(20) + "|" + "Patient ID".center(20) + "|" + "Contact Number".center(20) +
            "|" + "Date of birth".center(20) + "|" + "IC number".center(20) + "|"
            + "Email".center(35) + "|" + "Vaccine code".center(20) +
            "|" + "Status".center(20) + "|" + "VC Centre".center(20) + "|"+ "\n" + "=" * 204)
        fh.write(intro + "\n")

    with open("id.txt", "w") as fh:
        intro = str(
            "=" * 168 + "\n" + "Name".center(20) + "|" + "Registration date".center(20) + "|" + "Patient ID".center(
                20) + "|" + "Status".center(
                20) + "|" + "First Doze Date and time".center(30) + "|" + "Second Doze Date and time".center(30) + "|" + "VC Centre".center(20) + "|" + "\n" + "=" * 168)
        fh.write(intro + "\n")

    with open("idgenerator.txt", "w") as fh:
        intro = str(
            "=" * 156 + "\n" + "AF vaccine".center(25) + "|" + "BV vaccine".center(25) + "|" + "CZ vaccine".center(
                25) + "|" + "DM vaccine".center(
                25) + "|" + "EC vaccine".center(25) + "|" + "Staff ID".center(25) + "|" + "\n" + "=" * 156)
        fh.write(intro + "\n")
        slot1 = str("AF0000".center(25) + "|" + "BV0000".center(25) + "|" + "CZ0000".center(25)
                    + "|" + "DM0000".center(25) + "|" + "EC0000".center(25) + "|" + "AV0000".center(25) + "|" + "\n" +
                    "-" * 156)
        fh.write(slot1 + "\n")

    with open("staffdata.txt", "w") as fh:
        intro = str(
            "=" * 104 + "\n" + "Staff ID".center(25) + "|" + "Name".center(25) + "|" + "Registration date".center(
                25) + "|" + "Password".center(25) + "|" + "\n" + "=" * 104)
        fh.write(intro + "\n")

#main logic starts here
write_txtfile()
menu()


