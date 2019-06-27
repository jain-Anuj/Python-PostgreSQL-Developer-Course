from user import User
from database import Database

Database.intiallize(user = 'postgres',
password = '123456' ,
database = 'learning' ,
host = 'localhost')

my_user = User('jaindolly2016@gmail.com', 'Dolly', 'Jain', 'None')

my_user.save_to_db()

print(User.load_from_db_by_email('jaindolly2016@gmail.com'))

my_user.save_to_db()

print(User.load_from_db_by_email('jainanuj9415@gmal.com'))
