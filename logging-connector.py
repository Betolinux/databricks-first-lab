from databricks import sql 
import os, logging 

logging.getLogger("databricks.sql").setLevel(logging.DEBUG) 
logging.basicConfig(filename = "results.log", level = logging.DEBUG) 

connection = sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"), http_path = os.getenv("DATABRICKS_HTTP_PATH"), access_token = os.getenv("DATABRICKS_TOKEN")) 
cursor = connection.cursor() 
cursor.execute("SELECT * from range(10)") 
result = cursor.fetchall() 

for row in result: 
    logging.debug(row) 

cursor.close() 
connection.close()
