/*
Mary Silliman
Capstone Project
*/

import java.util.*;  //for exceptions, invalid input

public class BoardControl
{
   private String[][] minesweeperBoard;
   private String[][] completeBoard;
   private String[][] activeBoard;

   private int difficultyLevel;
   private CompleteBoard complete;
   private ActiveBoard active;
   
   public BoardControl(int difficultyLevel) {
      this.difficultyLevel = difficultyLevel;
   }

   //generates 2D array, size determined by difficulty level
   public String[][] createBoard() {      
      switch (difficultyLevel) {
         case 1:  //beginner
            minesweeperBoard = new String[9][9];
            break;
         case 2:  //intermediate
            minesweeperBoard = new String[16][16];
            break;
         case 3:  //expert
            minesweeperBoard = new String[16][30];
            break;
         default: //beginner board is the default option
            minesweeperBoard = new String[9][9];
            break;
      }
      
      int i;
      int j;
      
      //blank board, filled with dash for easy element readability
      for (i = 0; i < minesweeperBoard.length; i++) {
         for (j = 0; j < minesweeperBoard[0].length; j++) {
            minesweeperBoard[i][j] = "-";
         }
      }
      return minesweeperBoard;
   }
   
   //active and complete board classes called
   //boards initialized blank, complete board filled with called methods
   public void setBoards() {
      this.active = new ActiveBoard(difficultyLevel, createBoard());
      activeBoard = active.getBoard();
      active.print(activeBoard);
      
      this.complete = new CompleteBoard(difficultyLevel, createBoard());
      complete.setMines();
      completeBoard = complete.setCounts();
   }
   
   //receives user element guesses
   //will terminate program is user selects a hidden mine element
   //converts column char guess to int
   public void findElement(int row, char column) {
      int num_column;
      String currentGuess;
      String guessHold;
      num_column = (int) column;
      
      //determine and add element to active board (from user selection) based on complete board
      currentGuess = completeBoard[row - 1][num_column - 65];
      activeBoard[row - 1][num_column - 65] = currentGuess;
       
      int i;
      int j;
      String testGuess;
      
      //fills in 0 elements in adjacent spaces surrounding user guess
      if (currentGuess.equals("0")) {
         //upper left diagonal
         try {
            testGuess = completeBoard[row - 2][num_column - 66];
            if (testGuess.equals("0")) {
               activeBoard[row - 2][num_column - 66] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
         
         //above
         try {
            testGuess = completeBoard[row - 2][num_column - 65];
            if (testGuess.equals("0")) {
               activeBoard[row - 2][num_column - 65] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
         
         //upper right diagonal
         try {
            testGuess = completeBoard[row - 2][num_column - 64];
            if (testGuess.equals("0")) {
               activeBoard[row - 2][num_column - 64] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
         
         //left
         try {
            testGuess = completeBoard[row - 1][num_column - 66];
            if (testGuess.equals("0")) {
               activeBoard[row - 1][num_column - 66] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
         
         //right
         try {
            testGuess = completeBoard[row - 1][num_column - 64];
            if (testGuess.equals("0")) {
               activeBoard[row - 1][num_column - 64] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
         
         //lower left diagonal
         try {
            testGuess = completeBoard[row][num_column - 66];
            if (testGuess.equals("0")) {
               activeBoard[row][num_column - 66] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
         
         //below
         try {
            testGuess = completeBoard[row][num_column - 65];
            if (testGuess.equals("0")) {
               activeBoard[row][num_column - 65] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
         
         //lower right diagonal
         try {
            testGuess = completeBoard[row][num_column - 64];
            if (testGuess.equals("0")) {
               activeBoard[row][num_column - 64] = testGuess; 
            }          
         }
         catch (ArrayIndexOutOfBoundsException e) {
            //adjacent space does not contain a 0
         }
      }
      
      //print active board with count based on user guess
      active.print(activeBoard);
            
      //gameover if user hits a mine
      if (currentGuess.equals("*")) {
         System.out.println("Oh no! Gameover!");
         System.exit(0);
      }
      else {
         activeBoard = active.getBoard();
      }   
      
      //count the number of empty spaces
      int x;
      int y;
      int count = 0;
         
      for (x = 0; x < activeBoard.length; x++) {
         for (y = 0; y < activeBoard[0].length; y++) {
            if (activeBoard[x][y].equals("-")) {
               count++;
            }
         }
      }
      
      //print victory message if all the mines are found   
      switch (difficultyLevel) {
         case 1:  //beginner
            if (count == 10) {
               System.out.println("You win!!");
               System.exit(0);
            }
            break;
         case 2:  //intermediate
            if (count == 40) {
               System.out.println("You win!!");
               System.exit(0);
            }
            break;
         case 3:  //expert
            if (count == 99) {
               System.out.println("You win!!");
               System.exit(0);
            }
            break;
         default: //beginner board is the default option
            if (count == 10) {
               System.out.println("You win!!");
               System.exit(0);
            }
            break;
         }
   }

   //stop
} //end class   