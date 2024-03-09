import psycopg2
import cron_scan

cron_scan.scrapp()
current_total_data = cron_scan.get_total_data_live()
current_state_data = cron_scan.get_state_data_live()
# process.format(current_state_data, current_total_data)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="localhost",
                                  database="covid")

    cursor = connection.cursor()
    create_table_query = '''SELECT * FROM public.webscrapper_databasetotal; '''
    cursor.execute(create_table_query)
    ''' sql = "insert into public.webscrapper_databasetotal values(%date,%d,%d,%d,%d)" % current_total_data
    cursor.execute(sql)
    connection.commit()'''
    print("Table created successfully in PostgreSQL ")


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    print("done")
