import requests
import mysql.connector
import time

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Wtfandrew123!',
    'database': 'final'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

insert_query = "INSERT INTO api_data (factor, pi, time) VALUES (%s, %s, %s)"


def fetch_data():
    """Fetch data from the API and store in the database."""
    url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json() 
            data_tuple = (data['factor'], data['pi'], data['time'])
            cursor.execute(insert_query, data_tuple)
            db.commit()
            print("Data inserted successfully")
        else:
            print("Failed to fetch data: HTTP", response.status_code)
    except requests.RequestException as e:
        print("Request failed:", e)

def main():
    for _ in range(60):
        fetch_data()
        time.sleep(60)
        
    with open('myfile.txt', 'r') as file:
        content = file.read()
    print(content)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
