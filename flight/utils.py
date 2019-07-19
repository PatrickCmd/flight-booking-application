letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Seat:
    def __init__(self, letter, row_number):
        self.letter = letter
        self.row_number = row_number

    def __str__(self):
        return f"{self.letter}{self.row_number}"

def generate_seats(seat_model, flight_instance, start_row, row_count, seats_per_row):
    for row_number in range(start_row, row_count + start_row):
        for seat_number in range(seats_per_row):
            new_seat = Seat(letters[seat_number], row_number)
            seat_model.objects.create(seat_number=new_seat, flight=flight_instance)
