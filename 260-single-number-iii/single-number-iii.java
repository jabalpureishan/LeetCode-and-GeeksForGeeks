import java.util.*;
class Solution {
    public int[] singleNumber(int[] nums) {
        HashMap <Integer,Integer> map = new HashMap <>();

        for (int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }

        int ind = 0;
        int[] ans = new int[2];

        for (int i:map.keySet()){
            if (map.get(i)==1){
                ans[ind] = i;
                ind += 1;
            }
        }
        return ans; 
    }
}