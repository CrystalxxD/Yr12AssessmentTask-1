import sqlite3

conn = sqlite3.connect("Resturant_Reservation.db")
cursor = conn.cursor()

print("Connected to database.\n")

# Query 1
cursor.execute("""
SELECT *
FROM RestaurantReservations
WHERE Time BETWEEN '19:00' AND '20:00';
""")
rows = cursor.fetchall()
print("Reservations between 19:00 and 20:00:")
for r in rows:
    print(r)

print("\n")

# Query 2
cursor.execute("""
SELECT SUM(NumberOfGuests) AS TotalGuests
FROM RestaurantReservations
WHERE ReservationDate BETWEEN '2024-09-13' AND '2024-09-25';
""")
total = cursor.fetchone()[0]
print("Total guests between 13–25 Sept:", total)

conn.close()
