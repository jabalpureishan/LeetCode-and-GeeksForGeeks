class Solution {
	public static boolean isprime(int num){
		if (num==2 || num==3){return true;}
		if (num<=1 || num%2==0 || num%3==0) {return false;}
		int i = 5;
		while (i*i<=num) {
			if((num%i)==0 || (num%(i+2))==0){return false;}
			i += 6;			
		}
		return true;		

	}
    public int diagonalPrime(int[][] nums) {
		int max = 0;
		int n  = nums.length;
		for(int i=0;i<n;i++){
			if(isprime(nums[i][i])){max = Math.max(max,nums[i][i]);}
		}
		int c = n-1;
		for(int j=0;j<n;j++){
			if(isprime(nums[j][c])){max = Math.max(max,nums[j][c]);}
			c--;
		}
		return max;
	        
    }
}