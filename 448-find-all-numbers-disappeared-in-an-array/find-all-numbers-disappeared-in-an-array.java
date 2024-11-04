class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
 		ArrayList<Integer> ans = new ArrayList<Integer>();
		Arrays.sort(nums);
		int curr = 0;
		for(int i:nums){
			for(int j=curr+1;j<i;j++){
				ans.add(j);	
			}
			curr = i;
		}
		for(int k=nums[nums.length-1]+1;k<=nums.length;k++){
			ans.add(k);
		}
		return ans;       
    }
}