from flask import Flask, render_template, jsonify, request, url_for
from sudoku_utils import Sudoku

app = Flask(__name__)
su = Sudoku()


@app.route('/board')
def board():
    su.set_problem()
    return render_template('boards.html', boards=su.base_board)


@app.route('/solve', methods=["GET"])
def solve_sudoku():
    if request.method == 'GET':
        su.solve()
        resjson = {'result': su.res}
        return jsonify(resjson), 200


@app.route('/validate', methods=['POST'])
def validate():
    if request.method == 'POST':
        data = request.get_json()
        res = {'result': su.isValidSudoku(data['data'])}
        return jsonify(res)
    return None, 200


if __name__ == '__main__':
    app.run(debug=True)