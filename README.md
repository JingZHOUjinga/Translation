# Translation

默认法语到中文翻译

```
python3 trans_baidu.py -s assidûment
```
输出结果　　　
```
Namespace(input_lang='fra', input_str='assidûment', output_lang='zh')
{'from': 'fra', 'to': 'zh', 'trans_result': [{'src': 'assidûment', 'dst': '勤奋地'}]}
勤奋地
```   


修改-il,-ol参数可实现中英法互译等　　

```
python3 trans_baidu.py -s 今天是个好 天气 -il auto -ol en　　　
``` 

输出结果　　

```
Namespace(input_lang='auto', input_str='今天是个好天气', output_lang='en')
{'from': 'zh', 'to': 'en', 'trans_result': [{'src': '今天是个好天气', 'dst': "It's a lovely day"}]}
It's a lovely day
```   




