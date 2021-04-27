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

 

我的问题：

1. 这就是最后一面嘛，大概薪资能给到期望么...


### 2021-4-27 清北道远课程 

待更新..
