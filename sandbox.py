# import psycopg2
# from django.conf import settings

# try:
#     connection = psycopg2.connect(
#         dbname=settings.DATABASES['default']['NAME'],
#         user=settings.DATABASES['default']['USER'],
#         password=settings.DATABASES['default']['PASSWORD'],
#         host=settings.DATABASES['default']['HOST'],
#         port=settings.DATABASES['default']['PORT'],
#     )
#     cursor = connection.cursor()
#     cursor.execute("SELECT 1;")
#     print("Database connection successful!")
# except Exception as e:
#     print(f"Error connecting to the database: {e}")
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
