import csv


class Student(object):
    course = "Software Engineer"
    deposit_amount = 0
    remaining_payment = 20000 - deposit_amount

    def __int__(self, s_name):
        self.student_name = s_name

    def update(self):
        csv_writer.writerow([self.name, self.deposit_amount, self.remaining_payment])

    def payment(self, amount):
        self.deposit_amount -= amount


if __name__ == '__main__':
    csv_file = open("Student_information.csv", "a+")
    fields = ['name', 'amount_paid', 'amount_rem']
    csv_writer = csv.writer(csv_file)
    if csv_file.empty:
        csv_writer.writerow(fields)
    while True:
        print("\t1. Enter data of new student\n\t2.Show student data\n\t3. Record payment\n\t4. Main menu\n\t5.Exit")
        ch = int(input("Your Choice"))
        if ch == 1:
            stu_name = input("Enter full name of student: ")
            obj = Student(stu_name)
            amt_paid = int(input("Enter amount paid: "))
            obj.payment(amt_paid)
            obj.update()
        elif ch == 2:
            csv_reader = csv.reader(csv_file)
            print(csv_reader)
        elif ch == 3:
            name = input("Enter full name of student: ")
            amt_paid = int(input("Enter amount paid: "))
            for lines in csv_reader:
                reader = csv.DictReader(csv_file, fieldnames=fields)
                writer = csv.DictWriter(csv_file, fieldnames=fields)
                if lines[0] == name:
                    lines['name'], lines['amount_paid'], lines['amount_rem'] = name, amt_paid, 20000 - amt_paid
                lines = {'name': lines['name'], 'amount_paid': lines['amount_paid'], 'amount_rem': lines['amount_rem']}
                writer.writerow(lines)
        elif ch == 4:
            continue
        else:
            break

