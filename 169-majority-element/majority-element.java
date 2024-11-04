class Solution {
    public int majorityElement(int[] nums) {
		double n = nums.length;
        int ans = nums[0];
		for(int j=0;j<n;j++){
			int count = 1;
			for(int k=j+1;k<n;k++){
				if(nums[k]==nums[j]){count++;}
			}
			if(count>=(n/2)){ans = nums[j];break;}
		}
        return ans;       
    }
}