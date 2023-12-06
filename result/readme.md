# result文件夹说明

**result文件夹主要用于存放项目运行后的结果**。 
![image](https://github.com/coder-xinxiaohai/AffectNet_Processing/assets/73678229/28932810-36a3-43d1-9ed2-9d50d5134da4)

**aligned_crop_affectnet_imgs**：用于存放经裁剪和对齐后的287401张面部表情图像，其283901张用于训练，3500张用于验证。 

**data_affectnet.pkl**：用于存放AffectNet的划分信息，包括训练图像和测试图像的对象信息。 

**train_label**：用于存放训练图像的路径信息和情绪标签。

<img width="353" alt="image" src="https://github.com/coder-xinxiaohai/AffectNet-Processing/assets/73678229/351b28b6-d400-405b-b548-de29caa07fd6">

**val_label**：用于存放验证图像的路径信息和情绪标签。

<img width="346" alt="image" src="https://github.com/coder-xinxiaohai/AffectNet-Processing/assets/73678229/a7e805e9-a136-4f17-a67d-9776276a2320">


**0.1noise_train.txt**：用于存放给训练标签加10%噪声后的结果。

**0.2noise_train.txt**：用于存放给训练标签加20%噪声后的结果。

**0.3noise_train.txt**：用于存放给训练标签加30%噪声后的结果。

