train_file = open('./result/train_label.txt')
val_file = open('./result/val_label.txt')

train_label_info = []
for line in train_file:
    train_label_info.append(line.strip().split(' '))

train_each_category_img_num = [0, 0, 0, 0, 0, 0, 0]
for sample in train_label_info:
    train_each_category_img_num[int(sample[1])] += 1
print(train_each_category_img_num)
# [74874, 134415, 25459, 14090, 6378, 3803, 24882]
# 0:中性  1:开心  2:悲伤  3:惊讶 4:恐惧 5:厌恶 6:生气

val_label_info = []
for line in val_file:
    val_label_info.append(line.strip().split(' '))
val_each_category_img_num = [0, 0, 0, 0, 0, 0, 0]
for sample in val_label_info:
    val_each_category_img_num[int(sample[1])] += 1
print(val_each_category_img_num)
# [500, 500, 500, 500, 500, 500, 500]
# 0:中性  1:开心  2:悲伤  3:惊讶 4:恐惧 5:厌恶 6:生气
