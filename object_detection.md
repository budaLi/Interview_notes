  基于深度学习的目标检测总结
  
  参考学习: 
  
      https://zhuanlan.zhihu.com/p/354060133 (基于深度学习的目标检测算法面试必备（RCNN~YOLOv5）
      
      https://zhuanlan.zhihu.com/p/34142321  (干货 | 目标检测入门)
      
      https://zhuanlan.zhihu.com/p/297965943 （YOLO算法最全综述：从YOLOv1到YOLOv5）
      
  好像除了知道目标检测分为单阶段和多阶段，以及听说了RCNN,FAST-RCNN,FASTER-RCNN,YOLO系列等名词外，并不太清楚到底是做了什么。
  于是下面的总结基本是照着知乎的学习资料完全重新学习。
  
  
# 2022-3-29

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
    

### 2. Fast RCNN 共享卷积运算

 文章指出RCNN耗时的原因是RCNN在selective search生成近2k个 region proposal后，通过cnn在每一个region proposal上单独进行提取特征，没有共享计算。
 于是提出将特征提取网络在图片整体上运行完毕后，再在其特征图上根据region proposal的区域进行选取特征，共享了大部分计算。
 
 ![image](https://user-images.githubusercontent.com/31475416/160545615-32164372-90e0-4ca3-95cd-2d1f29a3a65b.png)

  如上图，图片经过特征提取模型得到feature map, 同时在原图上运行selective search 算法得到ROI (Region of interest,实为坐标组)，将ROI映射到feature map上，
  再对每个ROI进行ROI pooling 操作得到等长的feature vector, 并将这些feature vectore 进行正负样本的整理(保持一定的正负样本比例)，分batch传入并行的RCNN子网络，
  同时进行分类和回归，并将两者的损失结合起来。
  
  ![image](https://user-images.githubusercontent.com/31475416/160547001-5bc0f3f6-a501-440d-97aa-7003e4dba491.png)

  我们得到的ROI通常是不同的大小，在映射到feature map后，会得到不同大小的特征向量。ROI Pooling先将ROI 等分成目标个数的网格，然后在每个格子上进行max pooling,就可
  以得到等长的ROI feature vector.
  
  文章最后的讨论也有一定的借鉴意义：
  
  1. multi-loss traing 相比单独训练classification 确有提升。 (个人认为可能是目标框定位的准确性对分类结果也有影响)
  2. multi-scale相比single-scale精度略有提升，但带来的时间开销更大，一定程度上说明CNN的尺度不变性。
  3.... 其他的懒得看了 
  
  小结：
      
      Fast RCNN文章最重要的贡献是将Proposal,Feature Extractir,Object Classification& Localization 统一在一个整体的结构中，并通过共享卷积提高了特征的利用效率。
      
      
 ### 3. Faster RCNN 两阶段模型的深度化 Towards Real Time Object Detection with Region Proposal Networks
 
 Faster RCNN是two-stage算法的奠基性工作，提出的RPN网络取代Selective search 算法，使得检测任务可以由神经网络端到端完成。  
 粗略的讲，Faster RCNN = RPN + Fast RCNN 
 由于Fast RCNN共享卷积运算的特性，引入RPN带来的计算量很小，使得Faster RCNN能以较高的效率运行。 并且精度SOTA(state of the art ,当前最佳).
 
 本文的主要贡献是提出RPN(Region Proposal Networks）,替代之前的SS算法。RPN讲Proposal这一任务建模为二分类的问题。(是否为物体)。
 
 
  ![image](https://user-images.githubusercontent.com/31475416/160553790-b6aae9c3-6e0d-4812-b5e2-7d52fdd9c5d0.png)


第一步是在一个滑动窗口上生成不同大小和长宽比例的anchor box,取定iou的阈值，按照ground truth标定这些anchor的正负，于是，传入RPN网络的样本数据
被整理为anchor box（坐标）和每个anchor box是否有物体(二分类标签) ,RPN网络将每个样本映射成一个概率值和四个坐标值，概率值反应这个anchor box有
物体的概率，四个坐标值用于回归定义物体的位置，最后将二分零和坐标回归的损失统一起来，作为RPN网络的目标训练。 
由RPN得到的Region Proposal在根据概率值筛选后经过类似的标记过程，被传入RCNN子网络，进行多分类和坐标回归，同样用多任务损失将二者的损失结合。


RCNN系列的算法，最终的目的都是提出Proposal region,然后进行分类和回归。 不论是RCNN的基于SS算法提出2k个左右的Region,然后去提取特征，交由Alexnet分类。
还是FAST RCNN进一步优化，先提取整体图片的特征，再通过SS生成的proposal region在特征图上映射，再进行ROI pooling 归一化特征，还是Faster RCNN 提出的
FPN, 改用anchor 的方式进行proposal的生成。


# 2022-3-30

### 4. YOLO YOU ONLY LOOK ONCE 

单阶段模型没有第一步的区域检出过程，直接从图中检出结果，也被称为Region Free方法。

YOLO是单目标检测算法的开山之作，它将检测任务表述成一个统一的、端到端的回归问题，并且以只处理图片一次同时得到位置和分类而得名。

YOLO vs Faster RCNN

    1.统一网络：YOLO没有显求region proposal的过程，Faster RCNN中尽管RPN与fast rcnn共享卷积层，但是在模型训练中，需要反复训练RPN网络和Fast RCNN网络。
    2.YOLO将检测统一为一个回归问题，而RCNN系列将检测分为两部分求解：物体分类和位置回归。

1. YOLO V1

  核心思想： 将整张图片作为网络的输入，直接在输出层对BBOX的位置和类别进行回归。
  
  
  ![f0bd05c00f07a6a820a42a29d8859c2](https://user-images.githubusercontent.com/31475416/160964944-68a0bcda-29d7-4462-9193-6fbf7b4fc25b.jpg)


2. YOLO V2

  YOLO V2在V1的基础上，在保持速度的基础上，更准确，速度更快，识别的对象更多。（YOLO9000)
  
  文章提出了一种 联合训练算法。 同时在检测数据集和分类数据集上训练物体检测器，用检测数据集的数据学习物体的准确位置，用分类数据集的数量增加分类的类别量。
  
  ![image](https://user-images.githubusercontent.com/31475416/160965448-15be6772-f9c0-4e5c-8b6a-4abce5963588.png)


  Batch Normalization 批量归一化
  
      
     BN层一般放在线性层和非线性层之间，也就是卷积层和激活层之间。
  
     批量归一化有助于解决反向传播过程种的梯度消息和梯度爆炸现象，降低对一些超参数的敏感性，并且每个batch在进行归一化的时候，起到了一定的正则化效果，能够
     获得更好的收敛速度和收敛效果。
     

3. YOLO V5

  参考 ：https://zhuanlan.zhihu.com/p/172121380
  
  
  
  
