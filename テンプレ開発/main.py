# coding: utf-8
import sys


"""Template"""


class IP:
    """
    入力を取得するクラス
    """
    def __init__(self):
        self.input = sys.stdin.readline

    def I(self):
        """
        1文字の取得に使います
        :return: 数
        """
        return int(input())

    def IL(self):
        """
        1行を空白で区切りリストにします(int
        :return: リスト
        """
        return list(map(int, self.input().split()))

    def SL(self):
        """
        1行の文字列を空白区切りでリストにします
        :return: リスト
        """
        return list(map(str, self.input().split()))

    def ILS(self, n):
        """
        1列丸々取得します(int
        :param n: 行数
        :return: リスト
        """
        return [int(self.input()) for _ in range(n)]

    def SLS(self, n):
        """
        1列丸々取得します（str
        :param n: 行数
        :return: リスト
        """
        return [self.input() for _ in range(n)]


"""ここからメインコード"""


def main():
    ip = IP()


main()
