name_list = ["万星明", "万星月", "朱秀娟", "万星明"]

# len
list_len = len(name_list)
print("列表中包含 %d个元素" % list_len)

# count
count = name_list.count("万星明")
print("万星明出现了 %d次" % count)

name_list.remove("万星明")

print(name_list)
