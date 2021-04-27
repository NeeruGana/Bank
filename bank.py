print("WELCOME TO TECHNO WORLD BANK")
n=int(input("1.Create an Account in TWB\n2.Delete your existing Account\n(1)or(2):"))

def create_acc():
    user_name = input("Enter Your Name: ")
    name1 = "{:<20}".format(user_name[:20])
    print("1.Savings Account\n2.Current Account\n3.Fixed Deposite Account")
    Acc_Type_inp = int(input("Type of Account: "))
    if Acc_Type_inp==1:
        Acc_Type="Savings       "

    elif Acc_Type_inp==2:
        Acc_Type="Current       "
    elif Acc_Type_inp==3:
        Acc_Type="Fixed Deposite"

    phn_no_inp=input("Enter Your 10 digit phone Number: ")
    if len(phn_no_inp)==10:
        phn_no=phn_no_inp
    else:
        print("Invalid Phn.No")
        exit()
    aadhar_no_inp=input("Enter Your 12-digit Aadhar or UID number: ")
    if len(aadhar_no_inp)==12:
        aadhar_no=aadhar_no_inp
    else:
        print("Wrong Aadhar Number")
        exit()
    file1 = open("nani.txt", "r+")
    readfile = file1.read()
    for i in range(1001,9999):
        m1=str(i)
        m="1203000"+str(i)
        #create_acc.m2="1203000"+str(i)
        SNo=m1[-3:]
        m1=SNo+"    "+m+"      "+name1+"       "+Acc_Type+"       "+phn_no+"        "+aadhar_no
        if m in readfile:
            pass
        else:
            file1.write("\n"+m1)
            #file1.write(m)

            break
    print("Created Your Account Successfully")
    print("Your Account No. is "+m)
    file1.close()
def Find_index():
	string1 = m2

	file1 = open("nani.txt", "r")


	flag = 0
	Find_index.index = 0

	for line in file1:
		Find_index.index+= 1

		if string1 in line:
			flag = 1
			break

	if flag == 0:
		print("Account Not Found")
	else:
		print("User Had an Account DELETING IT")



	file1.close()


def delete_data():

    a_file = open("nani.txt", "r")
    lines = a_file.readlines()

    a_file.close()
    place=Find_index.index-1
    del lines[place]
    new_file = open("nani.txt", "w+")

    for line in lines:
        new_file.write(line)
    new_file.close()

if n==1:
    create_acc()
if n==2:
    m2=input("Enter Your Acc.No: ")

    Find_index()
    delete_data()
    print("Account Deleted Successfully")