class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        
        int len1=overwrite_string.length();
        int len2=my_string.length();
        
        String len01=my_string.substring(0,s);
        String len02=my_string.substring((s+len1),len2);
        
        answer += len01+overwrite_string+len02;
        
        return answer;
    }
}