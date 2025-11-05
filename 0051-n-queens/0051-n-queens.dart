class Solution {
  List<List<String>> solveNQueens(int n) {
    List<List<String>> board=List.generate(n, (_)=>List.generate(n, (_)=>'.'));
    List<List<String>> result = [];
    void solve(int row ){
      if(row==n){
        // Each solution you store is frozen in time.
        //Backtracking in later recursion steps won’t touch previously saved solutions.
        List<String> snapshot = board.map((r) => r.join()).toList();
        // if we add directly board then it will saves reference not the value ;
        result.add(snapshot);
        return; 
      }
      //check whether the queen which is string can be placed in the column or diagonal by keeping one row fixed
      // [".Q..","...Q","Q...","..Q."] is an 1d array which has 4 columns containing the queens at the respective rows 
      for(int col=0;col<n;col=col+1){
          if(isValid(board,n,row,col)){
            board[row][col]="Q";
            solve(row+1);
            board[row][col]=".";
          }
        }
    }
  solve(0); 
  return result;
  }
}

bool isValid(List<List<String>> board,int n,int i,int j){
  for(int k=0;k<n;k=k+1){
    // check only for columns since every row is guaranteed to get a single queen 
    if(board[k][j]=="Q"){
      return false;
    }
    // check the diagonals
    //1.Check upper-left  and we are going down so check for the upper side diagonal (\)
    for (int row = i - 1, col = j - 1; row >= 0 && col >= 0; row--, col--) {
        if (board[row][col] == "Q") return false;
      }
    //2.Check upper-right diagonal (/)
    for (int row = i - 1, col = j + 1; row >= 0 && col < n; row--, col++) {
        if (board[row][col] == "Q") return false;
  }


  }
  return true;
}