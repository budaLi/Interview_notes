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
  
  
### 2022-3-30

数组： 16. 最接近的三数之和

![image](https://user-images.githubusercontent.com/31475416/160732259-3b00c645-76ff-4e93-88d1-f4f2d7755d56.png)


排序+ 双指针


        class Solution {
            public:
                int threeSumClosest(vector<int>& nums, int target) {
                    sort(nums.begin(),nums.end());
                    int n=nums.size();
                    int ans=nums[0]+nums[1]+nums[2];
                    for(int i=0;i<=nums.size()-3;i++){
                        int left=i+1,right=n-1;
                        while(left<right){
                            int num=nums[i]+nums[left]+nums[right];
                            if(num==target)return target;
                            else if(num<target){
                                ans=abs(target-num)>abs(target-ans)?ans:num;
                                left++;
                            }
                            else {
                                ans=abs(target-num)>abs(target-ans)?ans:num;
                                --right;
                            }
                        }
                    }
                    return ans;
                }
            };


### 2022-3-31

字符串： 5. 最长回文子串

![image](https://user-images.githubusercontent.com/31475416/160960908-05b2bff8-29f0-4256-92c0-3de9de97d4ea.png)


这道题之前用python提交的几次始终是超时，静下心来尝试发现还是很有意思的。需要注意的是字符串的边界以及几个特殊case的处理。 


    class Solution(object):
          def longestPalindrome(self, s):
              """
              :type s: str
              :rtype: str
              """
              n = len(s)
              dp = [[False for _ in range(n)] for _ in range(n)]

              ans = s[0]
              for i in range(n):
                  dp[i][i] = True
                  x = i + 1
                  while x < n and s[i] == s[x]:
                      dp[i][x] = True
                      ans = s[i:x+1] if x - i >= len(ans) else ans
                      x += 1
              print("连续长的",ans)
              index = 1
              while index < n:
                  tem_1 = index
                  tem_2 = index
                  while tem_2<n and dp[tem_1][tem_2]:
                      tem_2 +=1
                  tem_2-=1
                  while  tem_1 >= 0 and tem_2 <n and s[tem_1] == s[tem_2] and dp[index][index] :
                      dp[tem_1][tem_2] = True
                      ans = s[tem_1:tem_2 +1] if tem_2 - tem_1 >= len(ans) else ans
                      tem_1 -= 1
                      tem_2 += 1
                  index +=1

              return ans


      S = Solution()

      s_list = ["babad","cbbd","a","aacabdkacaa","tattarrattat"]
      for s in s_list:
          ans = S.longestPalindrome(s)
          print(s,ans)

  
  c++ 版本的懒得写了。 
  
      vector<vector<int>> dp(n, vector<int>(n));   二维数组的声明  
      s.substr(begin, maxLen);

  
 
