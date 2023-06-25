from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def get_hitokoto():
    # 在这里编写获取一言的逻辑
    hitokoto = "你好，世界！"  # 这里仅作示例，你可以替换成你自己的逻辑
    return jsonify(hitokoto=hitokoto)

if __name__ == '__main__':
    app.run()
