/*
Mary Silliman
Capstone Project
*/


public class ActiveBoard
{
   private String[][] minesweeperBoard;
   private int difficultyLevel;
   
   public ActiveBoard(int difficultyLevel, String[][] minesweeperBoard) {
      this.minesweeperBoard = minesweeperBoard;
      this.difficultyLevel = difficultyLevel;
   }
   
   public String[][] getBoard() {
      return minesweeperBoard;
   }
   
   //prints active board with axes
   public void print(String[][] minesweeperBoard) {
      int i;
      int j;
      int k;
      char xAxis = 'A';
      int yAxis = 1;
      
      System.out.print("   ");
      for (k = 0; k < minesweeperBoard[0].length; ++k) {
         System.out.print(xAxis + " ");
         xAxis++;
      }
      System.out.println();
      
      for (i = 0; i < minesweeperBoard.length; ++i) {
         System.out.printf("%2d", yAxis);
         System.out.print(" ");
         for (j = 0; j < minesweeperBoard[i].length; ++j) {
            System.out.print(minesweeperBoard[i][j] + " ");
         }
         System.out.println();
         yAxis++;
      }
   }

   //stop
} //end class   