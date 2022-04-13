
###  An Overview of Facial Micro-Expression Analysis: Data, Methodology and Challenge
 
微表情识别(MER)与分析。

其主要介绍微表情识别与宏观表情识别的区别是微表情时间跨度短，变化力度较细。应用领域主要包括警察询问、临床诊断、抑郁分析、商务谈判等。 

1. MER的主要数据集包括CASME系列、SMIC、SAMM ,其中CASME表情分类主要包括8类(快乐、悲伤、厌恶、惊讶、蔑视、恐惧、压抑、紧张)。SMIC主要包括三类(积极、消极、惊讶)。SAMM包括7类(与CASME相比缺少压抑和紧张、增加愤怒)。
还可通过3D人脸模型、gan方法生成ME数据集。

2. ME的pipeline流为: 人脸检测-> 关键点检测(人脸矫正) + 动作方法 + 特征提取 + 微表情识别
3. 
4. MER主要有三类方法:1. 从宏观表情到微观表情的识别。 2.基于关键点顶点帧。 3. 基于面部动作单元 。  实现细节有待研究。
结论： 从不同MER方法在各个数据集上的ACC来看，算法效果都比较一般。(acc最多70+)



![image](https://github.com/budaLi/Interview_notes/blob/main/paper_reading/2_1.jpg)
![image](https://github.com/budaLi/Interview_notes/blob/main/paper_reading/2_2.jpg)
![image](https://github.com/budaLi/Interview_notes/blob/main/paper_reading/2_3.jpg)
