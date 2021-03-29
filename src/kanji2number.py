import json
import urllib.parse


def lambda_handler(event, context):
    # TODO implement
    input = event["input"]
    input = urllib.parse.unquote(input)
    try:
        result = kanji2number(input)
        output = result
        object ={   
                    'statusCode': 200,
                    'headers': {
                        'Content-type': 'application/json;charset=UTF-8'
                    },
                    'body': output
                }
        return json.dumps(object,indent=4,ensure_ascii=False).encode('utf8')
    except Exception as e:
        #raise Exception('Malformed input ...')
        # result = str(e)
        # output = result
        # object ={
        #             'statusCode': 204,
        #             'headers': {
        #                 'Content-type': ' text/plain;charset=UTF-8'
        #             },
        #             'body': output
        #         }
        # return json.dumps(object,indent=4,ensure_ascii=False).encode('utf8')
        raise ExtendException(204, "Bad Request")
        
#関数で使用する辞書型の定義
kanji = {
    "壱": "1",
    "弐": "2",
    "参": "3",
    "四": "4",
    "五": "5",
    "六": "6",
    "七": "7",
    "八": "8",
    "九": "9"
}

number = {
    0: "零",
    1: "壱",
    2: "弐",
    3: "参",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九"
}

#中数
mediumNum = {
    0 : "千",
    1 : "百",
    2 : "拾"
}

#下数
lowerNum = {
    0: "兆",
    1: "億",
    2: "万"
}

#下数がない場合に使用する変数
allZero = "0000" 

#大数表記の漢数字からアラビア数字に変換する関数
#入力：文字列
#出力：数値
def kanji2number(str):
    n = len(str)        #入力文字列の長さ
    isFirst = True      #先頭の"0"を消すためのフラグ
    result = ""         #出力用の変数
    cut = 0             #切り分け用の変数

    if not checkNum(str):
        error( str + " is not support!")

    #零のときの処理
    if str == "零" and n == 1:
        return "0" 

    #兆，億，万の位の処理
    for i in range(0,3):
        if lowerNum[i] in str:
            s = str[cut : str.find(lowerNum[i])]        #先頭から文字（lowerNum[i]）の手前までの文字列を取得（7文字以下になる）
            if len(s) <= 7:                             #文字数チェック
                result = result + convert(s, isFirst)   #漢数字からアラビア数字へ変換
                cut = str.find(lowerNum[i]) + 1         #切り分け用の変数を更新
                isFirst = False                         #フラグの変更
            else:
                error("syntax error")                   #エラー処理
        elif (not isFirst):                             #先頭に数値がある場合は"0000"で埋める
            result = result + allZero
    
    #千の位以下の処理
    if cut < n:                                     #千の位以下があるとき
        s = str[cut :]                              #切り分けから文字列の最後までを取得(7文字以下)
        if len(s) <= 7:                             #文字数チェック
            result = result + convert(s, isFirst)   #漢数字からアラビア数字へ変換
        else:
            error("syntax error")                   #エラー処理
    elif (not isFirst):                             #先頭に数値がある場合は"0000"で埋める
        result = result + allZero                   

    if result.isdigit():                            #文字列を数値に変換できるか判別
        return result
    else:
        error("syntax error")                       #エラー処理


#大数表記の漢数字から4桁のアラビア数字に変換する関数
#入力：漢数字を表す文字列，上位の下数があるかを表すフラグ
#出力：4桁のアラビア数字を表す文字列
def convert(str, isFirst):
    n = len(str)                                    #入力文字列の長さ
    result = ""                                     #出力用の変数
    cut = 0                                         #切り分け用の変数

    #千，百，拾の位の処理
    for i in range(0,3):
        if mediumNum[i] in str:
            s = str[cut : str.find(mediumNum[i])]   #先頭から文字（mediumNum[i]）の手前までの文字列を取得（1文字になる）
            if len(s) == 1:                         #文字数チェック
                result = result + kanji[s]           #漢数字からアラビア数字へ変換
                cut = str.find(mediumNum[i]) + 1    #切り分け用の変数を更新
            else:
               error("syntax error")                #エラー処理
        else:                       
            result = result + "0"                   #数値がない場合"0"で埋める
    
    #壱の位の処理
    if cut < n :
        s = str[cut:]                               #切り分けから文字列の最後までを取得(1文字)
        if len(s) == 1:
            result = result + kanji[s]               #漢数字からアラビア数字へ変換
        else:
            error("syntax error")                   #エラー処理
    else:
        result = result + "0"                       #数値がない場合"0"で埋める
    
    if isFirst:                                     
        result = removeZero(result)                 #下数の上位に値がないときは先頭から"0"を取り除く

    return result

#先頭から"0"を取り除く関数
#入力：アラビア数字を表す文字列
#出力：入力の文字列の先頭から0をを取り除いた文字列
def removeZero(str):
    n = len(str)                                    #入力文字列の長さ        
    for i in range(0,n):
        if(str[0] == "0"):                          #文字列の先頭が"0"の時
            str = str[1:]                           #先頭を取り除く
        else:                                       #文字列の先頭が"0"以外の時
            break
    return str

#指定文字列以外が含まれるか判別する関数
#入力：文字列
#出力：指定文字列以外が含まれるかを示すBool値
def checkNum(str):
    uniqeNum = set(str)                             #重複要素を削除
    uniqeStr = list(uniqeNum)                       #set型のオブジェクトを配列に変換

    for i in range(0,10):                           #含まれる数値を削除
        if number[i] in uniqeStr:
            uniqeStr.remove(number[i])
            
    for i in range(0,3):                            #含まれる下数と中数の削除
        if lowerNum[i] in uniqeStr:
            uniqeStr.remove(lowerNum[i])
        if mediumNum[i] in uniqeStr:
            uniqeStr.remove(mediumNum[i])

    if len(uniqeStr) == 0:                          #配列の残りをチェック
        return True                                 #解析できる文字列のみ
    else:
        return False                                #解析できない文字列が含まれる

#エラー処理用の関数
def error(str):
    print (str)
    raise TestException(str)
    
class TestException(Exception):
    pass

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