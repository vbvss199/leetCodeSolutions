class Solution {
  bool isPalindrome(int x) {
    int original=x;
    String reverse="";
    if(x<0){
      return false;
    }
    if(x==0 || x<9){
        return true;
    }
    while(x>0){
      int k=x%10;
      reverse=reverse+k.toString();
      x=x~/10;
    }
    if(reverse==original.toString()){
      return true;
    }
    else{
      return false;
    }
  }
}