import java.lang.*;
import java.util.*;
class Solution {
    public static boolean check_if_one(Vector<Character> dq){
        int len = dq.size();
        for (int i=0;i<len-1;i++){
            if (dq.elementAt(i)!='0'){

                return true;
            }
        }
        if (dq.elementAt(len-1)!='1'){
            return true;
        }
        return false;
    }
    public static Vector<Character> divide(Vector<Character> dq){
        int len = dq.size();
        for (int j=len-2;j>-1;j--){
            dq.set(j+1,dq.elementAt(j));
        }
        dq.set(0,'0');

        return dq;
    }
    public static Vector<Character> add(Vector<Character> dq){
        int carry = 1;
        int ind = dq.size()-1;
        while(carry>0 && ind>-1){
            if (dq.elementAt(ind)=='0'){
                dq.set(ind,'1');
                carry = 0;
                break;
            } else {
                dq.set(ind,'0');
            }
            ind -= 1;
        }
        if( carry>0){
            dq.add(0,'1');
        }

        return dq;
    }
    public int numSteps(String s) {
       Vector <Character> dq = new Vector<Character>();
       int n = s.length();
       for (int i=0;i<n;i++)
       {
            char c = s.charAt(i);
            dq.add(c);
       }
        System.out.println(check_if_one(dq));
        int count = 0;
       while (check_if_one(dq))
       {    
            int ln = dq.size();
            if (dq.elementAt(ln-1)=='1'){
                dq = add(dq);
                // System.out.println("add");

            } else {
                dq = divide(dq);
                // System.out.println("divided");
            }
            // System.out.println("After");
            // System.out.println(dq);
            count++;

        }
        return count;
}}