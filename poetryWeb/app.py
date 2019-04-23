from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import json
from keras.models import load_model
import tensorflow as tf
from my_function.config import Config
from my_function.write_poem import auto_write_first
from my_function.write_poem import auto_write_sen
from my_function.write_poem import auto_write_hide
from my_function.poetry import PoetryModel
app = Flask(__name__)

global graph
graph = tf.get_default_graph()
model = PoetryModel(Config)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/flask/')
def hello_flask():
    return 'flask'

# model = load_model('poetry_model.h5')

@app.route('/fir/',methods=['GET'])
def fir():
    with graph.as_default():
        test_flask = request.values.get("usr")
        # print(test_flask)

        result = auto_write_first(test_flask,model)
        return json.dumps(result)


@app.route('/hide/', methods=['GET'])
def hide():
    with graph.as_default():
        test_flask = request.values.get("usr")
        # print(test_flask)

        result = auto_write_hide(test_flask,model)
        return json.dumps(result)


@app.route('/sen/', methods=['GET'])
def sen():
    with graph.as_default():
        test_flask = request.values.get("usr")
        # print(test_flask)

        result = auto_write_sen(test_flask,model)
        return json.dumps(result)


if __name__ == '__main__':
    app.run()
