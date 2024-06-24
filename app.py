from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

@app.route('/track')
def track():
    # Get user information
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the information
    with open('scan_log.txt', 'a') as log_file:
        log_file.write(f'{timestamp} - {user_ip} - {user_agent}\n')

    # Redirect to the actual URL
    return redirect('https://lucky0-6.github.io/photo/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
