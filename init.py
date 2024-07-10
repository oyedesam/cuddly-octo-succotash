import os
from dotenv import load_dotenv


load_dotenv()

connectionString = os.getenv('DATABASE_CONNECTION_STRING')
databaseName = os.getenv('DATABASE_NAME')

print(connectionString)
print(databaseName)