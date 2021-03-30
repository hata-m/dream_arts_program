import json
import urllib.parse

def lambda_handler(event, context):
    # TODO implement
    input = event["input"]
    input = urllib.parse.unquote(input)
    try:
        result = number2kanji(input)
        output = result
        object = {
            'statusCode': 200,
            'headers': {
                'Content-type': 'application/json;charset=UTF-8'
            },
            'body': output
        }
        return object
        
    except Exception as e:
        raise ExtendException(204, str(e))
    

#関数で使用する辞書型の定義
number = {
    "0": "",
    "1": "壱",
    "2": "弐",
    "3": "参",
    "4": "四",
    "5": "五",
    "6": "六",
    "7": "七",
    "8": "八",
    "9": "九"
}
#中数
mediumNum = {
    0 : "",
    1 : "拾",
    2 : "百",
    3 : "千"
}
#下数
lowerNum = {
    0: "",
    1: "万",
    2: "億",
    3: "兆"
}

#上限と下限の定義
MAX_NUMBER = 9999999999999999
MIN_NUMBER = 0


#アラビア数字から大数表記の漢数字に変換する関数
#入力：数値
#出力：文字列
def number2kanji(base):
    num = int(base)                                    #入力をString型に変換
    n = len(base)                                       #入力の文字数
    result = ""                                         #出力用の変数
    if n%4 == 0:                                        #4桁区切りの個数
        part = int(n/4)
    else: 
        part = int(n/4)+1                                                                     

    if not (MIN_NUMBER <= num <= MAX_NUMBER):           #範囲内の数値か判別
        error( str(num) + " is not support!")

    if base == "0" and n == 1:                          #入力が0の時
        result = "零"
    else:                                               #後方から4桁ずつ，大数表記の漢数字に変換                                            
        cut = -4
        for i in range(0,part):
            if (i == 0):
                result = convert(base[cut:]) + result
            else:
                #兆，億，万の桁を付ける場合
                tmp = base[cut-4:cut]
                if tmp != "0000":
                    result = convert(tmp) + lowerNum[i] + result  
                cut = cut - 4

    return result

#4桁のアラビア数字を大数表記の漢数字に変換する関数
#入力：文字列に変換した4桁数値
#出力：4桁数値を大数表記の漢数字に変換した文字列
def convert(str):
    n = len(str)        #入力文字列の桁数
    result = ""         #戻り値用の変数

    for i in range(0, n) :
        c = str[-(i+1)]     #文字列の後ろから順に文字を取り出す
        if c != "0":        #"0"は変換しない(辞書ではなくても可)
            result =  number[c] + mediumNum[i] + result 

    return result

#エラー処理用の関数
def error(str):
    raise TestException(str)
    
class ExtendException(Exception):
    def __init__(self, statusCode, description):
        self.statusCode = statusCode
        self.description = description

    def __str__(self):
        obj = {
            "statusCode": self.statusCode,
            "description": self.description
        }
        return json.dumps(obj)