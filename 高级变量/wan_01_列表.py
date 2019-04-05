name_list = ["万星明", "朱秀娟", "万星月"]

# 1、取值
print(name_list[2])

# 知道数据内容,确定索引位置
print(name_list.index("万星明"))

# 2、修改
# name_list[1] = "万玉琴"

# 3、增加
name_list.append("万玉琴")
name_list.insert(1, "朱秀媛")

temp_list = ["朱正"]
name_list.extend(temp_list)

# 4、删除
name_list.remove("万星月")
name_list.pop()
name_list.pop(1)
name_list.clear()

print(name_list)
