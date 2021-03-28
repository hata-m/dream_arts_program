from kanji2number import kanji2number 
from number2kanji import number2kanji

######テストする範囲を設定######

START = 0                   #開始値                  
END = 10000000000000000     #終了値
STEP = 10000000000                    #ステップ数

############################

#チェックフラグ
CHECK_FLAG = False

def main():
    print("start")
    try:
        for i in range(START,END,STEP):
            input = str(i)
            tmp = number2kanji(input)       #アラビア数字から大数表記の漢数字に変換
            output = kanji2number(tmp)      #大数表記の漢数字からアラビア数字に変換

            if CHECK_FLAG:
                print("input : " + input)
                print("tmp  : " + tmp)
                print("output: " + output)

            if input != output:             #変換前と変換後が一致しているかどうか
                error(input + ": NG")
            elif input == output and CHECK_FLAG:
                print(tmp　+ ": OK")
    print("finish")
    
    except Exception as e:
        print (e)

    


#エラー処理用の関数
def error(str):
    raise TestException(str)
    
class TestException(Exception):
    pass

if __name__ == "__main__":
    main()