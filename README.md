# auto_poem
A auto poem machine drived by keras

演示视频百度云地址：


链接：https://pan.baidu.com/s/11JxFzSGrTtIagk-hLvyRnw 
提取码：jfxv 

运行方法：启动flask，app.py 点击http://127.0.0.1:5000/

运行截图：poem_1.png文件

基于keras RNN 构建

模型训练 4000 epoch，在大数据班机器上训练较慢

没有上传模型文件，模型文件名为  poetry_model.h5

功能：1.给定第一个字，能够自动写五言绝句。2.自动写五言绝句藏头诗

环境配置：python3，keras，flask，tensorflow



# 示例：



```python
def auto_write_hide(input_word,model):
    return model.predict_hide(input_word)
```





输入：风花雪月

输出：风北延空华，花来应能翠。雪横气一日，月影桂臣无。



示例图片见example.npg



# 代码文件内容

poetryWeb:

数据集 dataset/poetry.txt

代码文件：

my_function

app.py

test.py(无代码)

static文件夹：存放静态文件

templates：存放主界面index.html

