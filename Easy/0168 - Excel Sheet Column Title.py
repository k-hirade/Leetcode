class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''  # 結果を保存するための文字列

        while columnNumber > 0:
            columnNumber -= 1
            # ASCIIコード
            # chr関数は、与えられた整数値に対応するASCII文字を返す
            # 26で割った余りを計算し、それを文字に変換して結果の文字列に追加
            result = chr((columnNumber % 26) + 65) + result
            # 26で割ることで、次のループのためのcolumnNumberを更新
            columnNumber //= 26

        return result
