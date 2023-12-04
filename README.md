# AffectNet-Processing
本项目完成了对AffectNet数据集中，手动标注且为中性、开心、悲伤、惊讶、恐惧、厌恶和生气，7种表情的图像的裁剪、对齐及数据划分任务，具体地，筛选并划分出**283901张图像用于训练**，**3500张图像用于验证**，其中训练图像包括74874张中性表情，134415张开心表情，25459张悲伤表情，14090惊讶表情，6378张恐惧表情，3803张厌恶表情，24882张生气表情，验证图像各个表情类别均为500张。

本项目适用于**AffectNet-7**分类任务的数据集处理，**仅限于裁剪、对齐和数据划分**，并未将所有图像全部缩放至指定大小，须注意。

本项目的代码分别参考[这里](https://github.com/PanosAntoniadis/emotion-gcn)（图像筛选、裁剪及对齐）和[这里](https://github.com/kaiwang960112/Self-Cure-Network)（训练标签加噪）**十分感谢前辈们的工作！** 另外，感谢我同门吴锐同学的帮助！

****
**1、数据准备工作**

由于AffectNet数据集并未开源，需要自行申请，具体可点[这里](http://mohammadmahoor.com/affectnet/)，申请并下载成功后，须将AffectNet数据集手动标注的图像及标签，放在Manually_Annotated文件下，如下图所示：
![image](https://github.com/coder-xinxiaohai/AffectNet-Processing/assets/73678229/c25be5b0-8fee-4cb9-90e3-841f63f09f91)


需要注意的是，截至目前，官方提供的train.csv中有一条记录存在问题，需要大家手动删除后，方可使用。
![image](https://github.com/coder-xinxiaohai/AffectNet-Processing/assets/73678229/180e31d0-648b-4606-827e-4440f8d324a4)

****
**2、数据处理部分**

(1) 首先运行pickle_annotations_affectnet.py文件，在result文件夹中生成data_affectnet.pkl文件。

(2) 接着运行sava_crop_imgs_affectnet.py文件，在result/aligned_crop_affectnet_imgs文件夹中生成经裁剪和对齐的AffectNet-7数据集，共287401张图像（283901张训练图像，3500张测试图像）。

(3) 最后运行save_annotatons_affectnet.py文件，在result文件夹中生成train_label.txt和val_label.txt文件。

至于dataloading.py、aligner.py和cal_each_category_img_nums.py文件分别用于数据加载、面部对齐和各表情类别的数量统计，如果大家只在意结果，暂时可不用管这几个文件，只需要记住**aligned_crop_affectnet_imgs文件夹中存放了处理后的AffectNet-7数据集，result文件夹中存放了划分好的训练集和验证集的标签信息，即train_label.txt和val_label.txt文件**。

****
**3、为训练标签加噪**

该部分代码在generate_noise_label.py中，运行本文件，即可完成对训练标签的加噪(10%、20%、30%)。


****
如果大家在运行本项目的过程中，遇到任何问题，欢迎留言~

