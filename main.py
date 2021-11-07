import psycopg2

try:
    con = psycopg2.connect(dbname = 'hotel', host = 'localhost', port = '5432', user = 'postgres', password = 'k1')

    cur = con.cursor()

    def guests():
        guest_id=int(input("guest id: "))
        hotel_id=int(input("hotel id: "))
        guest_name=str(input("Name: "))
        guest_surname=str(input("Surname: "))
        guest_phoneNumber=str(input("Phone number: "))
        guest_email=str(input("email: "))
        guest_address=str(input("address: "))
        guest_country=str(input("country: "))
        guest_creditcard = str(input("creditcard: "))
        return guest_id, hotel_id, guest_name, guest_surname, guest_phoneNumber, guest_email, guest_address, guest_country, guest_creditcard
        quit()

    def hotels():
        hotel_id=int(input("hotel id :"))
        hotel_name=str(input("hotel name: "))
        hotel_address=str(input("hotel address: "))
        room_capacity=int(input("room capacity: "))
        num_of_floorsofFloors=int(input("number of floors: "))
        star_rating=int(input("number of stars: "))
        hotel_email=str(input("email: "))
        return hotel_id, hotel_name, hotel_address, room_capacity, num_of_floorsofFloors,star_rating, hotel_email
        quit()

    def booking():
        booking_id=int(input("booking id: "))
        num_rooms_booked=int(input("number of rooms booked: "))
        booking_cost= int(input("booking cost: "))
        check_in=str(input("check in time (enter date in YYYY-MM-DD hh:mm:ss format): "))
        check_out=str(input("check out time(enter date in YYYY-MM-DD hh:mm:ss format): "))
        booking_date = str(input("booking date(enter date in MM/DD/YYYY format): "))
        duration_of_stay=int(input("duration of stay: "))
        paid=bool(input("Have they paid:"))
        hotel_id = int(input("hotel id :"))
        employees_id = int(input("employees id: "))
        guest_id = int(input("guest id: "))
        return booking_id, num_rooms_booked, booking_cost, check_in, check_out, booking_date, duration_of_stay, paid, hotel_id, employees_id, guest_id
        quit()

    def employees():
        employees_id=int(input("employees id: "))
        employees_name=str(input("employees name: "))
        employees_surname=str(input("employees surname: "))
        employees_email=str(input("employee email: "))
        employees_address=str(input("employee address: "))
        employees_job=str(input("employees job: "))
        employees_phoneNumber = str(input("employee phone number: "))
        employees_salary=int(input("employee salary: "))
        hotel_id = int(input("hotel id :"))
        department_id = int(input("department id: "))
        return employees_id, employees_name, employees_surname, employees_email, employees_address, employees_job, employees_phoneNumber,  employees_salary, hotel_id, department_id
        quit()

    def menu():
        op = 1
        while op != 0:
            print("Choose an option")
            print("1.Add guest")
            print("2.Add hotel")
            print("3.Add booking")
            print("4.Add employee")
            print("5.Search how many booked rooms in specific hotel")
            print("6.Search number of workers in specific hotel")
            print("7.Search the sum of the employees salary in specific hotel")
            print("8.Earnings from booked rooms in specific hotel")
            print("9.Information about employees working in specific hotel and department")
            print("10.Information about hotels with specific star rating")
            print("11. Exit program")

            option = int(input("Enter your choice: "))
            if option == 1:
                guest_id, hotel_id, guest_name, guest_surname, guest_phoneNumber, guest_email, guest_address, guest_country, guest_creditcard = guests()
                postgres_insert_query = """ INSERT INTO guests (guest_id, hotel_id, guest_name, guest_surname, guest_phoneNumber, guest_email, guest_address, guest_country, guest_creditcard) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                record_to_insert = (
                guest_id, hotel_id, guest_name, guest_surname, guest_phoneNumber, guest_email, guest_address,
                guest_country, guest_creditcard)
                cur.execute(postgres_insert_query, record_to_insert)
                con.commit()
                print("Guest added succesfully")
            elif option == 2:
                hotel_id, hotel_name, hotel_address, room_capacity, num_of_floors, star_rating, hotel_email = hotels()
                postgres_insert_query = """ INSERT INTO hotels (hotel_id, hotel_name, hotel_address, room_capacity , num_of_floors, star_rating, hotel_email ) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                record_to_insert = (
                hotel_id, hotel_name, hotel_address, room_capacity, num_of_floors, star_rating, hotel_email)
                cur.execute(postgres_insert_query, record_to_insert)
                con.commit()
                print("Hotel added succesfully")
            elif option == 3:
                booking_id, num_rooms_booked, booking_cost, check_in, check_out, booking_date, duration_of_stay, paid, hotel_id, employees_id, guest_id = booking()
                postgres_insert_query = """ INSERT INTO booking (booking_id, num_rooms_booked, booking_cost,check_in, check_out, booking_date, duration_of_stay, paid, hotel_id, employees_id, guest_id ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                record_to_insert = (
                booking_id, num_rooms_booked, booking_cost, check_in, check_out, booking_date, duration_of_stay, paid,
                hotel_id, employees_id, guest_id)
                cur.execute(postgres_insert_query, record_to_insert)
                con.commit()
                print("Booking added succesfully")
            elif option == 4:
                employees_id, employees_name, employees_surname, employees_email, employees_address, employees_job, employees_phoneNumber, employees_salary, hotel_id, department_id = employees()
                postgres_insert_query = """ INSERT INTO employees (employees_id, employees_name, employees_surname, employees_email, employees_address, employees_job, employees_phoneNumber,  employees_salary, hotel_id, department_id  ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                record_to_insert = (
                employees_id, employees_name, employees_surname, employees_email, employees_address, employees_job,
                employees_phoneNumber, employees_salary, hotel_id, department_id)
                cur.execute(postgres_insert_query, record_to_insert)
                con.commit()
                print("Employee added succesfully")
            elif option == 5:
                var1 = str(input("enter date in YYYY-MM-DD format: "))
                var2 = int(input("enter hotel id: "))
                cur.execute(
                    '''select (sum(booking.num_rooms_booked)) from booking where %s between booking.check_in and booking.check_out AND booking.hotel_id=%s ''',
                    [var1, var2])
               # Selecting rows from hotel table using cursor.fetchall
                records = cur.fetchall()
                for row in records:
                    print(" sum of booked rooms in this hotel: ", row[0], '\n')
            elif option == 6:
                var1 = int(input("enter hotel id: "))
                cur.execute('''select Count(employees_id) from employees where employees.hotel_id=%s''', [var1])
                # Selecting rows from employees table using cursor.fetchall
                records = cur.fetchall()
                for row in records:
                    print(" sum of workers: ", row[0], '\n')
            elif option == 7:
                var1 = int(input("enter hotel id: "))
                cur.execute('''select sum(employees_salary) from employees where employees.hotel_id=%s''', [var1])
                # Selecting rows from employees table using cursor.fetchall
                records = cur.fetchall()
                for row in records:
                    print(" sum of workers salary: ", row[0], '\n')
            elif option == 8:
                var1 = int(input("enter hotel id: "))
                cur.execute('''select sum(booking_cost) from booking where hotel_id=%s''', [var1])
                # Selecting rows from booking table using cursor.fetchall
                records = cur.fetchall()
                for row in records:
                    print(" earnings ", row[0], '\n')

            elif option == 9:
                var1 = int(input("enter hotel id: "))
                var2 = int(input("enter department of hotel: "))
                cur.execute( '''select *  from employees, departments where employees.hotel_id=%s AND departments.department_id=%s ''',
                    [var1, var2])
                # print("\nSelecting rows from employees table using cursor.fetchall
                records = cur.fetchall()
                for row in records:
                    print(" employee id: ", row[0], )
                    print(" employee name: ", row[1], )
                    print(" employee surname: ", row[2], )
                    print(" employee job: ", row[5], )
                    print(" employee salary: ", row[7], )
                    print("---------------------")
            elif option == 10:
                var1 = int(input("enter star rating: "))
                cur.execute('''select * from hotels where star_rating=%s''', [var1])
                # print("\nSelecting rows from booking table using cursor.fetchall
                records = cur.fetchall()
                for row in records:
                    print(" hotel id: ", row[0], )
                    print(" hotel name: ", row[1], )
                    print(" hotel address: ", row[2], )
                    print(" room capacity: ", row[3], )
                    print(" number of floors: ", row[4], )
                    print("hotel email: ", row[6], )
                    print("---------------------")
            elif option == 11:
                op=0
                break

    menu()



except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    if(con):
        cur.close()
        con.close()
        print("PostgreSQL connection is closed\n")