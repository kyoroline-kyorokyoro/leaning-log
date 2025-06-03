1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 整数の配列nums と整数が与えられた場合target、その合計が となる 2 つの数値のインデックスtargetを返します。

各入力には正確に1 つの解があり、同じ要素を 2 回使用しない可能性があると想定できます。

回答は任意の順序で返すことができます。

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

フォローアップ: 時間計算量が少ないアルゴリズムを思いつくことができますか?O(n2) 