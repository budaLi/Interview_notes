# 2022-3-29

  基于深度学习的目标检测总结
  
  参考学习: 
      https://zhuanlan.zhihu.com/p/354060133
      https://zhuanlan.zhihu.com/p/34142321
  
  好像除了知道目标检测分为单阶段和多阶段，以及听说了RCNN,FAST-RCNN,FASTER-RCNN,YOLO系列等名词外，并不太清楚到底是做了什么。
  于是下面的总结基本是照着知乎的学习资料完全重新学习。
  
  ## 导言 目标检测的任务表述
  
  计算机理解的图像信息，根据后续任务的需要，有三个主要的层次。
  
  ![image](https://user-images.githubusercontent.com/31475416/160522491-699a6706-0970-47cb-8b0f-cfdb06c69722.png)

    一是分类（Classification），即是将图像结构化为某一类别的信息，用事先确定好的类别(string)或实例ID来描述图片。
    这一任务是最简单、最基础的图像理解任务，也是深度学习模型最先取得突破和实现大规模应用的任务

    二是检测（Detection）。分类任务关心整体，给出的是整张图片的内容描述，而检测则关注特定的物体目标，要求同时获得这一目标的类别信息和位置信息。
 
    三是分割（Segmentation）。分割包括语义分割（semantic segmentation）和实例分割（instance segmentation），前者是对前背景分离的拓展，
    要求分离开具有不同语义的图像部分，而后者是检测任务的拓展，要求描述出目标的轮廓（相比检测框更为精细）。
    
 ## 目标检测经典工作回顾
 
  目标检测单阶段算法代表：SSD,YOLO, 多阶段算法代表：RCNN,FAST-RCNN,FASTER-RCNN.
  
  ### 1. RCNN
  
   全称:Rich feature hierarchies for accurate object detection and semantic segmentation 
        丰富的特征层次结构 用于准确的对象检测和语义分割
        
   传统的计算机视觉方法常用精心设计的手工特征（如SIFT,HOG)描述图像。从图像分类领域的经验来看，CNN网络自动学习特征的效果已经超过了手工设计的特征。
   RCNN在局部区域应用卷积网络，以发挥卷积网络学习高质量特征的能力。
   
   ![image](https://user-images.githubusercontent.com/31475416/160523875-559186f8-8ca1-4c2c-b717-c9a0fd5e5167.png)

   RCNN将检测抽象为两个过程，一是基于图片提出若干个可能包含物体的区域(即图片的局部裁剪，被称为Region Proposal),文中使用的是Selective Search算法。
   二是在这些区域上运行当时表现最好的分类网络（AlexNet),得到每个区域内的物体的类别。
   
   另外，文章中的两个做法值得注意：
   
   1. 数据的准备。输入CNN之前，我们需要根据Ground Truth对提出的Region Proposal进行标记，这里用的是IOU.IOU计算了两个区域的交并比，描述了两个区域的重合程度。
        
      本文中特别提到，IOU的选择对于结果影响显著，这里要谈两个threshold，一个用来识别正样本（如跟ground truth的IOU大于0.5)，另一个用来标记负样本(即背景类，如IOU小于0.1)。
      而介于两者之前的为难例(HARD NEGATIVES),若将其标记为正类，则包含了过多的背景信息，反之又包含了要检测物体的特征，因此这些Proposal便被忽略掉。
      
   2. 位置坐标的回归 (Bounding Box Regression),这一过程是Region Proposal向Ground Truth调整，实现时加入了log/exp 变换使得损失保持在合理的量级，可是看作是标准化操作。

  本文的两大贡献。
  
  1. CNN可用于基于区域的分割和定位物体。
 
  2. 监督训练样本数量紧缺时，在额外的数据上预训练的模型经过fine-tuning 可以取得很好的效果。

  第一个贡献影响了之后几乎所有的two-stage方法，而第二个贡献用分类任务(imgnet)中训练好的模型作为基网络，在检测问题上fine-tuning的方法也在之后的工作中继续沿用。


 小结：
    
    RCNN的想法直接明了，即将检测任务转化为区域上的分类任务，是深度学习方法在检测任务上的试水。
    模型本身的问题也很多，比如要训练三个不同的模型（proposal,classifiction,regression),重复计算导致的性能问题。 
    尽管如此，论文的很多做法仍然广泛的影响着检测任务。
    

### Fast RCNN 共享卷积运算

 
        
  
  
  