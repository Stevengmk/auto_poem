from my_function.poetry import PoetryModel
from my_function.config import Config

def auto_write_hide(input_word,model):
    # model = PoetryModel(Config)
    # print(input_word+",")
    return model.predict_hide(input_word)

def auto_write_sen(input_word,model):
    # model = PoetryModel(Config)
    # print(input_word+",")
    return model.predict_sen(input_word)
    # return model.predict_sen(input_word+", ")


def auto_write_first(input_word,model):
    # model = PoetryModel(Config)
    # print(input_word+",")
    return model.predict_first(input_word)

# for i in range(3):
#     # 给出第一句话进行预测
#     sen = model.predict_sen('山为斜好几，')
#     print(sen)
#
# for i in range(3):
#     #给出第一个字进行预测
#     sen = model.predict_first('山')
#     print(sen)
#
# for temp in [0.5,1,1.5]:
#     #随机抽取第一句话进行预测
#     sen = model.predict_random(temperature=temp)
#     print(sen)