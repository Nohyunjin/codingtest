import java.util.ArrayList;

class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList <Integer> tmp = new ArrayList<>();
        
        while(n>0){
            tmp.add(n%3);
            n = n/3;
        }
        
        for(int i=tmp.size()-1; i >= 0; i--){
            answer += Math.pow(3,tmp.size()-i-1)*tmp.get(i);
        }       
        return answer;
    }
}