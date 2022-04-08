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


### 2021-4-28  华为测试岗机试(时间原因放弃)

上来就是牛客网华为机试题...刷几道熟悉下环境吧

### 2021-4-29  外包宝马(要求英语读写 放弃)

外企其实挺好的，就是英语要求读写...所以就做了个笔试题，暂时不打算去面试了。

笔试题是用伪代码解决自动驾驶中的具体问题，主要思路是用opencv裁剪出指定颜色的区域，进行分析...挺有意思的，具体要求和文档已上传. 

文档： 暂时无法上传...

代码： https://github.com/budaLi/Interview_notes/tree/main/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95

主要涉及内容：  opencv处理图像


### 2021-5-7  仙豆智能(过)

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


### 2021-5-12 香侬后端开发

1. a = [{"name": "zhangsan", "age": 43}, {"name": "lisi", "age": 18}, {"name": "mazi", "age": 25}, {"name": "wanger", "age": 21}]，对a按age降序排列。
   
   ```
      a = [{"name": "zhangsan", "age": 43}, {"name": "lisi", "age": 18}, {"name": "mazi", "age": 25}, {"name": "wanger", "age": 21}]
      
      新的列表：
      # lambad中的y其实已经是a中的每个字典 只需取age
      new_a = sorted(a,key=lambda y:y["age"],reverse = True)
      print(new_a)
      
      更改原列表：
      a.sort(key = lambda:y["age"],reverse=True)
      print(a)
   ```

 2. 给一个列表， 如 a = [1, 3, 54, 300, 33, 72]，用列表表达式求列表中的所有奇数。

    ```
       a = [1, 3, 54, 300, 33, 72]
       new_a = [one for one in a if one%2!=0]
       print(new_a) 
    ```
 3. 写出打印结果

    ```
      def test(p1, p2=dict()):
          p2.update(p1)
          return p2
      a = {"a": 1}
      b = {"b": 2}
      a = test(a)
      b = test(b)
      print(a)
      print(b)
    ```
    
    这道题答案是a 和b均为 {"a":1,"b":1},原因猜测为调用两次test()函数时p2在内存中都是同一个对象，即id不变，如下：
    ```
        def test(p1, p2={}):
            print(id(p2))
            p2.update(p1)
            return p2
        a = {"a": 1}
        b = {"b": 2}
        a = test(a)
        b = test(b)
        print(a)
        print(b)
    ```

4. 实现一个装饰器并调用。

  很久不写，不会了..
  
  ```
    def print_wraps(fun):
      def wraps():
          print("waaps")
          fun()
      return wraps
    @print_wraps
    def print_number():
        print(1)
    print_number()
  ```
  
5. 编写一个类，为该类实现___call__方法并调用。
    
   __call__函数的主要作用是可以把类实例当做函数调用，具体的用途..没有接触过
   
   参考https://blog.csdn.net/xie_0723/article/details/79505131

6. 实现一个函数反转链表，例如输入的链表是: 1->2->3->null，输出的是3->2->1->null
  
  ```
      class ListNode:
            def __init__(self,val,next=None):
                self.val = val
                self.next = next

      def revser_node(root):
          next_node = root.next
          new_root =root
          new_root.next = None
          while next_node:
              new_next_node = next_node.next
              next_node.next = new_root
              new_root = next_node
              next_node = new_next_node
          return new_root

      def print_node(root):
          while root:
              print(root.val)
              root = root.next
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    print_node(node1)
    new_root = revser_node(node1)
    print_node(new_root)
  ```

7. （非递归）遍历一颗二叉树，返回节点值列表（数组）。
  
   ```
      class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

      def print_tree(root):
          nodes = [root]
          nodes_val_list = []
          while len(nodes)>0:
              node = nodes.pop(0)
              nodes_val_list.append(node.val)
              if node.left:
                  nodes.append(node.left)
              if node.right:
                  nodes.append(node.right)
          return nodes_val_list

      root = TreeNode(1)
      root2 = TreeNode(2)
      root3 = TreeNode(3)
      root.left = root2
      root.right = root3
      nodes_val_list = print_tree(root)
      print(nodes_val_list)
   ```
   
   再就是问了一个项目，大概介绍了下..没有涉及什么具体技术 


### 2021-5-21  累了...缓缓，再议吧，怎么选都会后悔...


### 2021-1-7  
时隔半年，好像工作越久越没了学习的动力..

### 2022-1-6 神策 大数据开发

大概几天没收到回复，应该是没过。要求大数据和nlp多一点。

1. 16进制转10进制。  B1-> 177 AA0F245C 转成2853119068   
   
   初版的实现是用list存储了16位数字，进行进制转换时用index获取该字符所对应的数字，初版代码如下:
   ```
   def trans(s):
      res = 0
      lis = [str(i) for i in range(10)]+["A",'B','C','D','E','F']

      for index in range(len(s)):
          s_index = lis.index(s[index])
          res += s_index*(16**(len(s)-1-index))
      return res
    s = "AA0F245C"
    print(trans(s))
   ```
   面试官提出复杂度有优化。最终代码如下:
      ```
      def trans(s):
          res = 0
          dic = {str(i):i for i in range(10)}
          dic2 = { "A":10, "B":11, "C":12,"D":13, "E":14, "F":15}
          dic.update(dic2)
          for index in range(len(s)):
              s_index = dic[s[index]]
              res += s_index*(16**(len(s)-1-index))
          return res
      s = "AA0F245C"
      print(trans(s))
      ```

### 2022-1-10 听起来是商汤的ai测试外包

1. 一个字符串里是无序的"+""-"符号，排序使得前半部分是"+",后半部分是"-"。
   ```
      def sort(s):
          new_s = []
          for one in s:
              if one=="+":
                  new_s.insert(0,one)
              else:
                  new_s.append(one)
          return "".join(new_s)

      s = "+-+-++++--"
      print(sort(s))
   ```
 
2. 第1题的修改版，输入为列表，想要原地修改实现排序。
   
   ```
      def sort(lis):
          start = 0
          end = len(lis)-1
          while start<end:
              while lis[start]=="+":
                  start+=1
              while start<end and lis[end]=="-":
                  end-=1
              lis[start],lis[end] = lis[end],lis[start]
              print(start,end,lis)
          return lis
      lis =list("+-+-++++--")
      print(sort(lis))
   ```
   
3. 将列表转成键为列表值，值为0的字典。如: ["李不搭"]转为{"李不搭":0}。
    ```
      names = ["李不搭"]
      print({name:0 for name in names})
    ```
4. 列表中出现次数最多的元素及其出现次数
   ```
      def get_max(lis):
          dic = {}
          max_count = 0
          max_one = None
          for one in lis:
              if one not in dic:
                  dic[one] = 1
              else:
                  dic[one]+=1
                  max_one,max_count = one if max_count<dic[one] else max_one,dic[one] if max_count<dic[one] else max_count
          return max_one,max_count
      lis =list("+-+-++++--11122223333333331111")
      print(get_max(lis))
   ```

### 2022-1-27 人民中科

写在前面的话: 一面面了大概一个小时，二面聊了半个多小时，第二天通知没通过二面，还是有点说不出的感觉。从大的方面考虑，我总是怕自己好高骛远，实力达不到野心；仔细想想，
还是要认真考虑是否有必要再沉淀，到底是换了工作学习新东西，还是呆在旧岗位厚积薄发。

### 2022-3-28

一时间想不起来从哪里开始。原以为能安心找个女朋友，在北京好好呆着，上周经理突然找部门每个人面谈..... 好像没什么不开心，之前总是想着换工作之前去西藏玩一趟，现在突然得到的
劝退消息，好像有点不知所措。  


### 2022-3-29

突然觉得...好像连准备面试都不知道从哪里开始，看来要找一份比较好的面试资料先。噢好像c++也需要巩固，总觉得是半吊子，每天尽量一道leetcode c++版吧。


### 2022-4-2 

婉拒了一家公司的线下面试，总觉得现在还不是找工作的好时机...总想再等等。 早上开会听说同事已经找好下家提了离职，日常惆怅....


### 2022-4-6 四海华辰

早上面试的....一时间想不起来问了点什么  感觉良好，约了明天下午三点的线下面试。
好像待遇挺好...公积金说是给全额。

## 2022-4-6  顺联软件科技

1. 大概介绍下自己以及做的几个项目中主要负责的内容。
2. 分类中可能存在部分样本稀缺的情况怎么处理的，有考虑训练中设置部分图片的训练频率嘛？ 
3. 模型训练出来几十兆，但是加载后几百兆是为什么   回答可能和参数量和计算量有关
4. 了解目标检测么    
5. 人脸关键点检测中选用的算法是什么，为什么选这个算法
6. ....其他的好像印象不太深了


### 2022-4-7 四海华辰

参加了线下面试，好像没聊一点技术相关的东西，Leader是山西人...介绍了很多公司现有的业务和发展方向。 感觉没啥问题。

### 2022-4-7 中科海微

线上电话面试，聊了很多关于人脸门禁的内容，看起来是比较相同的业务。

### 2022-4-8 

大早上和女友吵架，发现拉黑了微信，qq支付宝淘宝什么的都被删除了，有点想骂娘。

