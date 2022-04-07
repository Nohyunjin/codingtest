//두 정수 left와 right가 매개변수로 주어집니다.
//left부터 right까지의 모든 수들 중에서, 
//약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

import java.util.ArrayList;

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        ArrayList <Integer> s = new ArrayList<>();
        ArrayList <Integer> m = new ArrayList<>();
        
        for(int i=left; i <= right; i++){
            int count = 0;
            for(int j = 1; j <= i; j++){
                if(i%j==0){
                    count++;
                }
            }
            if(count%2==0){
                s.add(i);
            }else{
                m.add(i);
            }
        }
        int sum = 0;
        int minus = 0;
        for(int a : s){
            sum += a;
        }
        for(int b : m){
            minus += b;
        }
        System.out.println(s);
        System.out.println(m);
        answer = sum - minus;
        return answer;
    }
}

// 다른 사람 풀이
class Solution2 {
    public int solution(int left, int right) {
        int answer = 0;

        for (int i=left;i<=right;i++) {
            //제곱수인 경우 약수의 개수가 홀수
            if (i % Math.sqrt(i) == 0) {
                answer -= i;
            }
            //제곱수가 아닌 경우 약수의 개수가 짝수
            else {
                answer += i;
            }
        }
        return answer;
    }
}