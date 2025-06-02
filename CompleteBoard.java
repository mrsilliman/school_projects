/*
Mary Silliman
Capstone Project
*/

import java.util.Random;                  //for generating random numbers

public class CompleteBoard
{
   private String[][] minesweeperBoard;
   private int difficultyLevel;
   
   public CompleteBoard(int difficultyLevel, String[][] minesweeperBoard) {
      this.difficultyLevel = difficultyLevel;
      this.minesweeperBoard = minesweeperBoard;
   }
   
   //randomly sets mines within the board
   //mine count based on difficulty level
   public void setMines() {
      Random randGen = new Random();
      int i;
      int column;
      int row;
      
      switch (difficultyLevel) {
         case 1:  //beginner
            for (i = 0; i < 10; ++i) {
               column = randGen.nextInt(minesweeperBoard[0].length);
               row = randGen.nextInt(minesweeperBoard.length);
               
               //ensure that mines are placed in unique spots
               if (minesweeperBoard[row][column] == "*") {
                  i--;
               }
               else {
                  minesweeperBoard[row][column] = "*";
               }
            }
            break;
         case 2:  //intermediate
            for (i = 0; i < 40; ++i) {
               column = randGen.nextInt(minesweeperBoard[0].length);
               row = randGen.nextInt(minesweeperBoard.length);
               
               //ensure that mines are placed in unique spots
               if (minesweeperBoard[row][column] == "*") {
                  i--;
               }
               else {
                  minesweeperBoard[row][column] = "*";
               }
            }
            break;
         case 3:  //expert
            for (i = 0; i < 99; ++i) {
               column = randGen.nextInt(30);
               row = randGen.nextInt(16);
               
               //ensure that mines are placed in unique spots
               if (minesweeperBoard[row][column] == "*") {
                  i--;
               }
               else {
                  minesweeperBoard[row][column] = "*";
               }
            }
            break;
         default: //beginner board is the default option
            for (i = 0; i < 10; ++i) {
               column = randGen.nextInt(minesweeperBoard[0].length);
               row = randGen.nextInt(minesweeperBoard.length);
               
               //ensure that mines are placed in unique spots
               if (minesweeperBoard[row][column] == "*") {
                  i--;
               }
               else {
                  minesweeperBoard[row][column] = "*";
               }
            }
            break;
      }
   }
   
   //counts set based on number of mines adjacent to a specific element
   public String[][] setCounts() {
      int count;
      int row;
      int column;
      
      for (row = 0; row < (minesweeperBoard.length); row++) {
         for (column = 0; column < (minesweeperBoard[0].length); column++) {
            count = 0;

            if ((row == 0) && (column == 0)) {                  
               if (this.minesweeperBoard[row + 1][column] == "*") {
                  count++;
               }
                        
               if (this.minesweeperBoard[row][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column + 1] == "*") {
                  count++;
               }
            }
            else if ((row == 0) && (column == (minesweeperBoard[0].length - 1))) {
               if (this.minesweeperBoard[row][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column] == "*") {
                  count++;
               }
            }
            
            else if (row == 0) {
               if (this.minesweeperBoard[row][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column + 1] == "*") {
                  count++;
               }
      
            }
            else if ((row == (minesweeperBoard.length - 1)) && (column == 0)) {         
               if (this.minesweeperBoard[row - 1][column] == "*") {
                  count++;
               }
                        
               if (this.minesweeperBoard[row - 1][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column + 1] == "*") {
                  count++;
               }
            }
            else if (column == 0) {
               if (this.minesweeperBoard[row - 1][column] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row - 1][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column + 1] == "*") {
                  count++;
               }
            }
            else if ((row == (minesweeperBoard.length - 1)) && (column == (minesweeperBoard[0].length - 1))) {
               if (this.minesweeperBoard[row - 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column - 1] == "*") {
                  count++;
               }
                        
               if (this.minesweeperBoard[row - 1][column] == "*") {
                  count++;
               }
            }
            else if (row == (minesweeperBoard.length - 1)) {
               if (this.minesweeperBoard[row - 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row - 1][column] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row - 1][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column + 1] == "*") {
                  count++;
               }
            }
            else if (column == (minesweeperBoard[0].length - 1)) {
               if (this.minesweeperBoard[row - 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row - 1][column] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column] == "*") {
                  count++;
               }
            }
            else {
               if (this.minesweeperBoard[row - 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column - 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row - 1][column] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row - 1][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row][column + 1] == "*") {
                  count++;
               }
               
               if (this.minesweeperBoard[row + 1][column + 1] == "*") {
                  count++;
               }         
            }   
                        
            if (this.minesweeperBoard[row][column] == "*") {
               minesweeperBoard[row][column] = "*";
            }
            else {
               minesweeperBoard[row][column] = Integer.toString(count);
            }
         }   
      }
      return minesweeperBoard;      
   }

   //stop
} //end class   