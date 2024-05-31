import java.util.*;
class Solution {
    public int[] singleNumber(int[] nums) {
        HashMap <Integer,Integer> map = new HashMap <>();
        for (int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        Vector<Integer> V = new Vector<>();
        for (int i:map.keySet()){
            if (map.get(i)==1){
                V.add(i);
            }
        }
        Integer[] array = new Integer[V.size()];
        V.toArray(array);
        int[] ans = new int[array.length];
        for (int i=0;i<array.length;i++){
            ans[i] = array[i];
        }
        return ans;   
    }
}