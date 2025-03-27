import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_data(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

# Example usage:
if __name__ == "__main__":
    # Connection details
    host = "localhost"
    user = "root"
    password = "yourpassword"
    database = "yourdatabase"
    
    # Create a connection
    conn = create_connection(host, user, password, database)
    
    # Example query to create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        gender VARCHAR(50),
        nationality VARCHAR(50)
    );
    """
    execute_query(conn, create_table_query)
    
    # Insert data
    insert_query = """
    INSERT INTO users (name, age, gender, nationality)
    VALUES ('John Doe', 28, 'Male', 'USA');
    """
    execute_query(conn, insert_query)
    
    # Fetch data
    select_query = "SELECT * FROM users;"
    users = fetch_data(conn, select_query)
    
    for user in users:
        print(user)

    # Close the connection
    if conn.is_connected():
        conn.close()
