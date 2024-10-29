class Solution {
    public int vowelStrings(String[] words, int left, int right) {
		String vowels = "aeiou";
		int count = 0;
		for(int j=left;j<=right;j++){
			System.out.println("--------");
			System.out.println(words[j]);
			if(vowels.indexOf(words[j].charAt(0))!=-1 && vowels.indexOf(words[j].charAt(words[j].length()-1))!=-1){
				count += 1;
				System.out.println("tru");
			}
		}
		return count;     
    }
}