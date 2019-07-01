from user import User
from database import Database

Database.intiallize(user = 'postgres',
password = '123456' ,
database = 'learning' ,
host = 'localhost')


print(User.load_from_db_by_email('jaindolly@gmail.com'))
