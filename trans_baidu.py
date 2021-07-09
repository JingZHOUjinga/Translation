
from urllib import request
from urllib import parse
import json
import hashlib
import random
import argparse   


def baidu_translate(input_str,input_lang,output_lang):
    baidu_url='http://api.fanyi.baidu.com/api/trans/vip/translate'
    trans_info={}
    #trans_info['from']值为'auto'表示自动识别源语言语种，'fra'表示源语言为法语
    trans_info['from']=input_lang
    #trans_info['from']='auto'

    #trans_info['to']为'zh'表示目标语言为中文
    trans_info['to']=output_lang

    #输入想翻译的内容
    trans_info['q']=input_str
    trans_info['transtype']='hash'
    trans_info['appid']='20190511000296411'
    trans_info['salt']=str(random.randint(32768, 65536))

    #秘钥key_str
    key_str="5cz9CWGLquZwuxHdMbUr"
    trans_data=trans_info['appid']+input_str+trans_info['salt']+key_str
    trans_data_MD5=hashlib.md5(trans_data.encode('utf8'))
    trans_info['sign']=trans_data_MD5.hexdigest()
    
    data_url=parse.urlencode(trans_info).encode('utf-8')
    response=request.urlopen(baidu_url, data_url)
    html_data=response.read().decode('utf-8')
    trans_result=json.loads(html_data)

    print(trans_result)
    trans_result = trans_result['trans_result'][0]['dst']
    print(trans_result)
    
    return trans_result



    
def main():

    #创建
    parser = argparse.ArgumentParser(description='translation select tool, source language code, target language code,input sentence ')
	

    #--sent\-s 均可使用，metavar用来生成帮助信息，required表明这个参数是必须有的，dest指参数的名称，action指执行的逻辑,help是帮助信息,type是指参数类型
    parser.add_argument("--sent","-s",metavar='input_str',required=True, dest='input_str', action='store',help='input sentence',type=str)

	#--inlan 或-il，默认是fra，可选择范围是auto、fra,en等，类型是str
    parser.add_argument("--inlan","-il",metavar='input_lang',required=False, dest='input_lang', action='store',choices={"fra","auto","en"}, default="fra", type=str)
    
    #--outlan 或-ol，默认是zh，可选择范围是en、zh等，类型是str
    parser.add_argument("--outlan","-ol",metavar='output_lang',required=False, dest='output_lang', action='store',choices={"zh","en","fra"}, default="zh", type=str)
    args = parser.parse_args()
    print(args)
    if args.input_str:
        input_str = args.input_str
    if args.input_lang:
        input_lang = args.input_lang

    if args.output_lang:
        output_lang = args.output_lang
    
    return baidu_translate(input_str,input_lang,output_lang)

if __name__ == "__main__":	
    
    main()
    
