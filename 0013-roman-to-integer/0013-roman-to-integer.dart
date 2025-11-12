class Solution {
  int romanToInt(String s) {
    int sum = 0;
    var romans = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    };

    int checkOrder(List<String> t) {
        if (t.length == 1) return romans[t[0]]!;
        if (romans[t[0]]! >= romans[t[1]]!) {
        return romans[t[0]]! + romans[t[1]]!;
      } else {
        return romans[t[1]]! - romans[t[0]]!;
      }
    }
    List<int> numsIntMod = [];
    List<int> specialFunction(List<String> l) {
      for (String element in l) {
        List<String> test = element.split("");
        numsIntMod.add(checkOrder(test));
      }
      return numsIntMod;
    }
    if(s.length<=2){
        sum=checkOrder(s.split(""));
        return sum;
    }
    else{
     List<String> numsMod = [];
    int i = 0;
    while (i < s.length) {
        if (i + 1 < s.length && romans[s[i]]! < romans[s[i + 1]]!) {
        numsMod.add(s.substring(i, i + 2)); // subtractive pair
        i += 2;
        } 
        else {
        numsMod.add(s[i]);
        i += 1;
    }
    }
    numsIntMod = specialFunction(numsMod);
    for (var ele in numsIntMod) {
        sum += ele;
  }
  }     
    return sum;
  }
}