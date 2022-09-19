import os
from datetime import datetime
from pytz import timezone
from flask import Flask, render_template

FILE_NAME = "./files/time.txt"

def create_app():
    app = Flask(__name__, template_folder='./templates')
    timezone_name = os.environ.get('TIMEZONE', 'Europe/Moscow')
    time_format = os.environ.get('TIME_FORMAT', '%H:%M:%S')
    zone = timezone(timezone_name)

    @app.route("/")
    def index():
        time = datetime.now(zone).strftime(time_format)
        directory = os.path.dirname(FILE_NAME)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(FILE_NAME, "a", encoding='utf-8') as file:
            file.write(str(datetime.now(zone)) + '</br>')
        return render_template('index.html', timezone_name=timezone_name, time=time)
    return app


if __name__ == "__main__":
    app=create_app()
    app.run(port=8080, host="0.0.0.0", debug=True)
