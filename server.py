from flask import Flask, render_template


app = Flask(__name__)
get_request_num = 0
post_request_num = 0


@app.route('/')
def route_main():

    return render_template('main.html')


@app.route('/request-counter')
def route_req_counter():

    return render_template('requests.html')


@app.route('/statistics')
def route_statistics():

    return render_template('statistics.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
