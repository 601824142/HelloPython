# coding=utf-8
"""
  名称:JSON文件读取
  作者:万星明
  时间:2019/6/23 15:33
  注释:
    - dump - 将Python对象按照JSON格式序列化到文件中
    - dumps- 将Python对象处理成JSON格式的字符串
    - load - 将文件中的JSON数据反序列化成对象
    - loads- 将字符串的内容反序列化成Python对象
"""
import json


def main():
    mydict = {
        'name': '万星明',
        'age': 24,
        'sex': '男',
        'phone': 13097314214,
        'hobby': ['敲代码', '看小说'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('sources/mydict.json', 'w', encoding='utf-8') as file:
            json.dump(mydict, file)
    except IOError as e:
        print("IO异常:" + e)
    print("数据保存完毕!")


if __name__ == '__main__':
    main()
