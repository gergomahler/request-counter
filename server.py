from flask import Flask, render_template, request


app = Flask(__name__)
get_request_num = 0
post_request_num = 0
put_request_num = 0
delete_request_num = 0


@app.route('/')
def route_main():

    return render_template('main.html')


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_req_counter():
    if request.method == 'GET':
        global get_request_num
        get_request_num += 1

    elif request.method == 'POST':
        global post_request_num
        post_request_num +=1

    elif request.method == 'PUT':
        global put_request_num
        put_request_num += 1

    elif request.method == 'DELETE':
        global delete_request_num
        delete_request_num += 1

    return render_template('main.html')


@app.route('/statistics')
def route_statistics():
    requests = {}
    keys = ['GET', 'POST', 'PUT', 'DELETE']
    values = [get_request_num, post_request_num, put_request_num, delete_request_num]
    for item in range(len(keys)):
        requests[keys[item]] = values[item]
    with open('request_counts.txt', 'w') as txt_file:
        for key, value in requests.items():
            txt_file.write(str(key) + ':' + str(value) + '\n')

    txt_file.close()

    return render_template('statistics.html', get_requests=get_request_num, post_requests=post_request_num,
                           put_requests=put_request_num, delete_requests=delete_request_num)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5800
    )
