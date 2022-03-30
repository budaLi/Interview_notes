### 2022-3-30 

Mobilenet V1:
  Mobilenet V1就是把Vgg中的标准卷积换成了深度可分离卷积。

可分离卷积啊主要有两种类型：空间可分离卷积和深度可分离卷积。

1. 空间可分离卷积： 把一个大的卷积核变成两个小的卷积核，比如将一个3x3的核分为一个3x1的和一个1x3的核。
  
    ![image](https://user-images.githubusercontent.com/31475416/160773808-f6cda77d-0cc6-4ade-a96d-8a7246cb6bb7.png)

2. 深度可分离卷积

    ![image](https://user-images.githubusercontent.com/31475416/160773862-80ad0c33-3191-497a-be04-3f5fa8bfa4d6.png)

  深度可分离卷积就是将普通卷积拆分成一个深度卷积和一个逐点卷积。
  
  ![image](https://user-images.githubusercontent.com/31475416/160774679-674ecd35-21d2-4c0e-b1e8-2bbce7bfb840.png)


为什么要用深度可分离卷积： 在效果相差不多的情况下，深度可分离卷积的参数量和计算量为普通卷积的九分之一到八分之一： 

![image](https://user-images.githubusercontent.com/31475416/160776365-9fb692b4-dfb4-43b6-a1ab-eb4137ff7e20.png)


Mobilenet V2: 

深度卷积并没有改变通道的能力，来的是多少通道输出就是多少通道。
PW 卷积也就是逐点卷积可以用来升维或者降维，那就可以在DW深度卷积之前先用PW卷积进行升维，再在一个更高维度的空间中进行卷积操作提取特征。

![image](https://user-images.githubusercontent.com/31475416/160778059-62004003-292e-408c-8dc3-6ec92b607052.png)

![image](https://user-images.githubusercontent.com/31475416/160778494-e296b829-4c07-490c-8ad5-69c46663d65a.png)

Resnet先降维(0.25倍),卷积，再升维。
Mobilenetv2则是先升维(6倍),卷积，再降维。称为 inverted residuals 。倒残差结构。


Mobilenet V3:

引入Mb V1的深度可分离卷积以及Mb V2的倒残差结构。
引入基于squeeze and excitation的轻量级注意模型(SE).
使用了新的激活函数 h-swish(x).
