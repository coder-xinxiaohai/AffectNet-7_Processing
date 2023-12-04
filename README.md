![image](https://github.com/coder-xinxiaohai/AffectNet-Processing/assets/73678229/e839a757-020c-42f8-9972-d6fdffce2f34)# AffectNet-Processing
本项目完成了对AffectNet数据集中，手动标注且为中性、开心、悲伤、惊讶、恐惧、厌恶和生气，7种表情的图像的裁剪、对齐及数据划分任务，具体地，筛选并划分出**283901张图像用于训练**，**3500张图像用于验证**，其中训练图像包括74874张中性表情，134415张开心表情，25459张悲伤表情，14090惊讶表情，6378张恐惧表情，3803张厌恶表情，24882张生气表情，验证图像各个表情类别均为500张。

本项目适用于**AffectNet-7**分类任务的数据集处理，**仅限于裁剪、对齐和数据划分**，并未将所有图像全部缩放至指定大小，须注意。

本项目的代码参考：https://github.com/PanosAntoniadis/emotion-gcn，**十分感谢前辈们的工作**！

由于AffectNet数据集并未开源，需要自行申请，具体链接为http://mohammadmahoor.com/affectnet/，申请并下载成功后，须将AffectNet数据集手动标注的图像及标签，放在Manually_Annotated文件下，如下图所示：
![image](https://github.com/coder-xinxiaohai/AffectNet-Processing/assets/73678229/c25be5b0-8fee-4cb9-90e3-841f63f09f91)
