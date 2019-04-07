# coding=utf-8
"""作者:万星明"""

wan = {"name": "万星明",
       "age": 24,
       "height": 1.79,
       "weight": 132.5,
       "gender": True}

# 1.取值,如果不存在键,则报错
print(wan["name"])

# 2.增加/修改,如果不存在键,则新增,否则修改
wan["age"] = 23
wan["sex"] = "男"

# 3.删除,如果不存在键,则报错
wan.pop("gender")

# 4.统计键值对数量
print("键值对数量为: %d" % len(wan))

# 5.合并字典,如果合并的字典中含有之前存在的,则覆盖
temp = {"money": 300, "age": 25}
wan.update(temp)

# 6.清空字典
# wan.clear()

# 7.循环遍历,获取key
for key in wan:
    print("%s===%s" % (key, wan[key]))

print(wan)
