# -*- coding: utf-8 -*-
def input_celsius_value():
    print("변환하고 싶은 섭씨 온도를 입력해주세요 :")
    n=float(input())
    return n

def convert_celsius_fahrenheit(n):
    f=((9/5)*n)+32
    return f

def print_fahrenheit_value(c,f):
    print("섭씨온도 :",c)
    print("화씨온도 :",f)


def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================
    n=input_celsius_value()
    c=convert_celsius_fahrenheit(n)
    print_fahrenheit_value(n,c)

    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    main()
