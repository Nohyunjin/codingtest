import java.util.ArrayList;
import java.lang.System;

class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList <Integer> tmp = new ArrayList<>();
        while(true){
            if(n > 3){
                tmp.add(n%3);
                n = n/3;
            }
            else{
                tmp.add(n);
            }
        }
        System.out.println();
        return answer;
    }
}