# auto_poem
A auto poem machine drived by keras

百度云地址：


链接：https://pan.baidu.com/s/11JxFzSGrTtIagk-hLvyRnw 
提取码：jfxv 

运行方法：启动flask，app.py 点击http://127.0.0.1:5000/

运行截图：poem_1.png文件

基于keras RNN 构建

模型训练 4000 epoch，在大数据班机器上训练较慢

数据集 poetry.txt

没有上传模型文件，模型文件名为  poetry_model.h5

功能：1.给定第一个字，能够自动写五言绝句。2.自动写五言绝句藏头诗

环境配置：python3，keras，flask，tensorflow



# 示例：

···

```python
def auto_write_hide(input_word,model):
    return model.predict_hide(input_word)
```

···

···

输入：风花雪月

输出![1556006513632](C:\Users\Steven\AppData\Roaming\Typora\typora-user-images\1556006513632.png)

···

