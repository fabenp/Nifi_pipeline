import csv
import os

from flask import Flask, request

app = Flask(__name__)

def save_to_csv(data):
    try:
        file_exists = os.path.isfile('weather_data.csv')
        with open('weather_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['city', 'Temperature', 'Wind', 'Tempfeeling', 'Humidity', 'Pressure','Time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")



@app.route('/', methods=['POST'])
def handle_post_request():
    data = request.data.decode('utf-8').strip()  # Decode bytes data to UTF-8 string and remove trailing newline
 # Parse the received data
    parsed_data = {}
    parts = data.split(',')
    for part in parts:
        key_value = part.split('=')
        key = key_value[0].strip()
        value = key_value[1].strip() if len(key_value) > 1 else ""
        parsed_data[key] = value




    # Save the parsed data to a CSV file
    save_to_csv(parsed_data)

    return 'Data received and saved successfully'

if __name__ == '__main__':
    app.run(debug=True,port=5000)






