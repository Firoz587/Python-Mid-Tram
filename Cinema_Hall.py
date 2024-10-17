class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def view_halls(cls):
        for hall in cls.__hall_list:
            print(f"Hall No: {hall.get_hall_no()}, Rows: {hall.get_rows()}, Columns: {hall.get_cols()}")


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}  
        self.__show_list = []  
        self.__rows = rows  
        self.__cols = cols 
        self.__hall_no = hall_no 
        Star_Cinema.entry_hall(self) 

    def entry_show(self, show_id, movie_name, time):
        self.__show_list.append((show_id, movie_name, time))
        self.__seats[show_id] = [['O' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            raise ValueError(f"Show ID {show_id} not found.")
        
        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                raise ValueError(f"Invalid seat position ({row}, {col}).")
            if self.__seats[show_id][row] == 'X' and self.__seats[show_id][col] == 'X':
                raise ValueError(f"Seat ({row}, {col}) is already booked.")
            self.__seats[show_id][row][col] = 'X'


    def view_show_list(self):
        print("Running Shows:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            raise ValueError(f"Show ID {show_id} not found.")
        
        print(f"Available seats for show {show_id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                seat_status = 'Available' if self.__seats[show_id][row][col] == 'O' else 'Booked'
                print(f"Seat ({row}, {col}): {seat_status}")

    def get_hall_no(self):
        return self.__hall_no

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols


def cinema_system():
    hall_101 = Hall(5, 5, 101)

    hall_101.entry_show('S1', 'Avengers: Endgame', '18:00')
    hall_101.entry_show('S2', 'Spider-Man: No Way Home', '20:00')
    hall_101.entry_show('S3', 'Tufaan', '20:30')
    hall_101.entry_show('S4', 'Bahubali-1', '12:00')
    hall_101.view_halls()

    while True:
        print('\nWelcome to Star Cinemas!\n')
        print('1 -> View Hall List Today')
        print('2 -> View Available Seats')
        print('3 -> Book Ticket')
        print('4 -> Exit')
        
        x=int(input("Enter Your Choice: "))
        if x==1:
            hall_101.view_show_list()
        elif x==2:
            show_id = input('Enter Show ID: ')
            hall_101.view_available_seats(show_id)
        elif x==3:
            show_id = input('Enter Show ID: ')
            num_seats = int(input('Enter Number of Seats: '))
            seat_list = []
            for _ in range(num_seats):
                row = int(input('Enter Row: '))
                col = int(input('Enter Column: '))
                seat_list.append((row,col))
                hall_101.book_seats(show_id, seat_list)
            print('Tickets Booked Successfully!')
        elif x==4:
            break;


cinema_system()
