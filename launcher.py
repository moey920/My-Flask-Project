from flask import Flask

app = Flask(__name__)
# 과제관련
db = {
    'boards' : []
}
count = 0

@app.route('/')
def hello() :
    return {'_result' : 'Hello!'}

# 과제관련
@app.route('/board/', method=['POST'])
def board_create() : # CRUD - create 는 항상 post로 옮겨준다
    _json = request.json
    board_name = _json['name']

    global count
    board_idx = count + 1
    count = board_idx
    # board_idx = count++ 과 같은 것.

    db['boards'].append({
        'id' : board_idx,
        'name' : board_name
    })

    print(db) # 디버깅용

    return jsonify(_result='ok', _data={'id': board_idx})

@app.route('/board/', methods=['GET'])
def board_get() : # CRUD - Read
    return jsonify(_result='ok', _data=db['boards']) #board를 전부 가져온다

@app.route('/board/<board_id>', methods=["GET"])
def board_get() : # CRUD - Read
    board_id = int(board_id)
    for board in db['boards'] :
        if board['id'] == board_id :
            return jsonify(_result='ok', _data = db['boards'][board_id-1])
    else : # for에 else로 쓰는 구문. else가 없이 그냥 return을 해도 된다. for문이 전부 돌았음에도 break나 return이 없으면 else문으로 간다.
        return jsonify(_result='error', reason='there is not data')

if __name__ == '__main__' :
    app.run('0.0.0.0', port=5000)

# "gunicorn" : 테스트용 서버가 아닌, 항시 작동하는 서버를 유지하기 위해 사용. gunicorn을 사용해서 플라스크 서버를 유지하면 다양한 옵션을 적용할 수 있다.