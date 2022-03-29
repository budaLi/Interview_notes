### 2022-3-29 

刷题貌似从来没有认真总结分类过，尝试按照leetcode给分的n个小类每天一道题。

![image](https://user-images.githubusercontent.com/31475416/160514392-6c14234b-8e2b-409f-9e7a-918e8fd83bb3.png)

数组: 11. 盛最多水的容器
  
   ![image](https://user-images.githubusercontent.com/31475416/160514655-fd720ab4-fa5c-49cd-a9e0-442f2c0cce1f.png)

  
  能直接想到的办法仍然是暴力解决，即从第一个元素开始，依次与下一个元素比较，如果前者较小，则最大储水量为前者的高度乘以与后者的索引距离。
  该方法的时间复杂度为O(n²)，空间复杂度应该只需要设置一个变量存储最大水量即可。
  
  代码如下:
  

      class Solution {
        public:
              int maxArea(vector<int>& height) {
                  int max_number = 0;

                  for(int i=0;i<height.size()-1;i++){
                      for(int j=i+1;j<height.size();j++){
                          if(height[i]<height[j]){
                              max_number = std::max(max_number,height[i]*(j-i));
                          }
                          else{
                              max_number = std::max(max_number,height[j]*(j-i));
                          }
                      }
                  }
                  return max_number;
              }
        };
          

      
  不出意外的，超出时间限制，53 / 60 个通过测试用例。
  
  正确做法应该是双指针，左右指针分别指向数组的开头和末尾，每次移动较小的指针。
  
        class Solution {
              public:
                  int maxArea(vector<int>& height) {
                      int max_number = 0;
                      int i=0,j=height.size()-1;
                      while(i<j){
                          if(height[i]<height[j]){
                              max_number= std::max(max_number,height[i]*(j-i));
                              i+=1;
                          }
                          else{
                              max_number= std::max(max_number,height[j]*(j-i));
                              j-=1;
                          }
                      }

                      return max_number;
                  }
              };
  
  
