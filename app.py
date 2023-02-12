from flask import Flask
import requests

app = Flask(__name__)

def get_weather_results(zip_code, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={},AU&appid={}".format(zip_code, api_key)
    print(api_url)

get_weather_results("3144", "885d7114d1101e5a04be8067a4d3a8c5")
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
