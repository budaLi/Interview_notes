# Interview_notes

面试多了就会觉得去哪家公司缘分很重要，记录面试中的一些问题和我印象中的回答吧...

### 2021-4-26  中软华为外包初面(过)

1.python有哪些基础的数据类型:数字，字符串(前两个没说),列表，元组，字典

2.python有哪些内置模块：os,json,shutil,copy,threading,time,datatime等等

4.用过哪些数据库，有什么区别呢: Mysql,Redis,SqlServer  关系型和非关系型，答案：https://www.huaweicloud.com/articles/fe5cc4f2814e2b690e3162675800a042.html 

6.url到浏览器会有哪些步骤   不是很清楚，回答了个dns解析再到服务器..答案:https://segmentfault.com/a/1190000006879700  

7.linux有哪些基础命令: cd,mkdir,ln,ls,su,top,rm,mv 

8.如何查看python中某个类的对象有哪些方法:dir可以看属性和方法，hasattr看有哪些属性

9.用过线程么，怎么用的:threading  写个参数为queue的函数消耗queue里的内容，thread = threading.Thread()...  start()  join()  

我的问题：

1. 工作地点是哪里，大概还有几轮面试，工作职责是什么..

### 2021-4-27 中软华为外包技术面(过)

1. 列表和set有什么区别: list可以重复，set不可以。

2. 如何遍历字典: for key,value in dict.items():...

3. 二叉树的定义..完全二叉树，搜索二叉树，平衡二叉树. 

4. 如何判断两个二叉树一致

  第一种思路是先序或者中序或者后序遍历两个二叉树，遍历的结果存到list，判断是否一致，比较麻烦。

  第二种思路是递归： 
  ```
  def judge(root1,root2):
      # 其中一个为空return False
      if root1 and not  root2: return False
      if root2 and not  root1: return False
      # 都为空为True
      if not root1 and not root2: return True
      return (root1.val==root2.val and judge(root1.left,root2.left)  and judge(root1.right,root2.right)) 
  ```
5. inner join,left join,right join的区别.

    回答的不咋对，答案：https://www.cnblogs.com/pcjim/articles/799302.html

    left join(左联接) 返回包括左表中的所有记录和右表中联结字段相等的记录

    right join(右联接) 返回包括右表中的所有记录和左表中联结字段相等的记录

    inner join(等值连接) 只返回两个表中联结字段相等的行.


6. sql实现for循环，不会。

7. 判断链表中是否存在target值。

  ```
  while root:
       if root.val == target:
           return True
       root = root.next
 return False
  ``` 

 8. Python中深浅拷贝的区别  

答案：浅拷贝(影子克隆):只复制对象的基本类型,对象类型,仍属于原来的引用. 深拷贝(深度克隆):不紧复制对象的基本类,同时也复制原对象中的对象. 就是说完全是新对象产生的. 浅拷贝和深拷贝之间的区别：浅拷贝是指将对象中的数值类型的字段拷贝到新的对象中，而对象中的引用型字段则指复制它的一个引用到目标对象。


我的问题：

1. 这就是最后一面嘛，大概薪资能给到期望么...


### 2021-4-27 清北道远课程初面(挂)

感觉整体回答的一般，没有实际的后端开发经验...

1. Mysql有哪些优化方法： 查询优化，索引优化..说了几个不咋靠谱的..

答案：  https://www.jianshu.com/p/dac715a88b44

2. 编程,有这样的数据需要转换：[[[[[1, 2, 3, 4, 5], 6]]]] --> [1,2,3,4,5,6]
    
    ```
    lis = [[[[[1, 2, 3, 4, 5], 6]]]]
    return_lis = []
    def get_number(lis):
        for one in lis:
            if isinstance(one, list):
                get_number(one)
            else:
                return_lis.append(one)
    get_number(lis)
    print(return_lis)
    ```
    
3. 解释下flask的蓝图，用过flask的G么..不知道是什么

    蓝图：https://www.zhihu.com/question/31748237

    flask中的G：https://blog.csdn.net/youzhouliu/article/details/88666209
    

4. 用过redis么，知道持久化机制么，Mysql呢？  参考：https://zhuanlan.zhihu.com/p/110073412 

    redis持久化：https://www.jianshu.com/p/bedec93e5a7b

5. 项目中的难点有哪些.. AI算法开发，拿实际的项目说了说

6. Thread.Local() 用过么..没有   参考：https://zhuanlan.zhihu.com/p/60126952


我的问题：

接受我这种没有后端开发基础的人么，还有几轮面试呢 

还是比较遗憾..没有过初面


### 2021-4-28  华为测试岗机试

上来就是牛客网华为机试题...刷几道熟悉下环境吧

### 2021-4-29  外包宝马

外企其实挺好的，就是英语要求读写...所以就做了个笔试题，暂时不打算去面试了。

笔试题是用伪代码解决自动驾驶中的具体问题，主要思路是用opencv裁剪出指定颜色的区域，进行分析...挺有意思的，具体要求和文档已上传. 

文档： 暂时无法上传...

代码： https://github.com/budaLi/Interview_notes/tree/main/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95

主要涉及内容：  opencv处理图像


### 2021-5-7  仙豆智能

五一之前进行了第一轮电话面，时间太长具体忘了问什么了...

一面电话面： 问了点python基础...具体的忘了

二面：

1. lis = {"x":1,"y":2,"z":3}
    
  删除lis中最小的元素
  
   ```
      lis = {"x":1,"y":2,"z":3}
      lis_tem = sorted(lis.items(),key=lambda y:y[1])
      print(type(lis_tem))  # list
      min_itmes = lis_tem[0]  # ("x",1)
      print(min_itmes)
      del lis[min_itmes[0]]
      print(lis)
   ```

2. 冒泡排序
    
   lis = [3,2,1,5,4]
   
   ```
      for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j]>lis[j+1]:
               lis[j],lis[j+1] = lis[j+1],lis[j]
   ```
  
  用过多线程没，爬虫呢...大概介绍了用的场景
  
  多线程如何等待呢，如何获取线程的输出结果..
  
  
  三面 ： 为啥换工作，打算要多少..没问什么技术上的东西，问的很多都是工作内容。
  
  Hr面： 你的优势,为啥换工作，打算要多少，介绍了下公司现在的情况

