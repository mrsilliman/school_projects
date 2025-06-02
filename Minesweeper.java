/*
Mary Silliman
Capstone Project
*/

import java.util.Scanner;              //for keyboard input
import java.util.*;                    //for exceptions, invalid input


public class Minesweeper
{     
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int difficultyLevel = 1;               //difficulty level defaulted to beginner
      boolean difficultyInput = false;
      
      System.out.println("Welcome to Minesweeper!\n");
      
      //prompt difficulty level from user
      //difficulty must be an integer from 1-3
      while (!difficultyInput) {
         //prompt for difficulty level: beginner, intermediate, expert
         System.out.println("Enter your desired difficulty level (1-3)");
         System.out.println("1: Beginner");
         System.out.println("2: Intermediate");
         System.out.println("3: Expert");
         
         //difficulty levels: beginner, intermediate, expert
         //input must be an integer from 1-3
         try {
            difficultyLevel = scnr.nextInt();
            
            if ((difficultyLevel >= 1) && (difficultyLevel <= 3)) {
               difficultyInput = true;
            }
            else {
               throw new Exception("\nTry again. Please enter a number from 1-3.");
            }
         }
         catch (InputMismatchException e) {
            System.out.println("\nTry again. Please enter a number from 1-3.");
            scnr.next();
         }
         catch (Exception exc) {
            System.out.println(exc.getMessage());
         }
      }
      
      //call boardcontrol call to create and set active and complete boards
      BoardControl control = new BoardControl(difficultyLevel);
           
      control.createBoard(); 
      control.setBoards();
      
      int row = 0;
      char column = 'A';
      Boolean continuePlay = true;
      String termination;
      
      //user can terminate game at any time
      while (continuePlay) {
         System.out.print("\nAvoid the hidden mines and select a spot.");
         
         String[][] exceptionsTest = control.createBoard();
         boolean validRow = false;
         boolean validColumn = false;
         String testValue = "";
         
         //prompt user for element guess
         //rows must be ints, columns must be Strings (converts to char)
         while (!validRow) {
            try {
               System.out.print("\nEnter the row (#): ");
               row = scnr.nextInt();
                  
               testValue = exceptionsTest[row - 1][0];
               validRow = true;
            }
            catch (InputMismatchException e) {
               System.out.println("Invalid input. Try again.");
               scnr.nextLine();
            }
            catch (Exception e) {
               System.out.println("Invalid input. Try again.");
            }
         }
         
         int numericCol;
         
         while (!validColumn) {
            try {
               System.out.print("\nEnter the column (letter): ");
               column = scnr.next().toUpperCase().charAt(0);
                  
               numericCol = (int) column;
               testValue = exceptionsTest[0][numericCol - 65];
               validColumn = true;
            }
            catch (InputMismatchException e) {
               System.out.println("Invalid input. Try again."); 
               scnr.nextLine();
            }
            catch (Exception e) {
               System.out.println("Invalid input. Try again."); 
            }
         }
                        
         //calls BoardControl to display result of user element guesses
         control.findElement(row, column);
         
         scnr.nextLine();
         System.out.print("\nEnter any key to continue or \'exit\' to terminate: ");
         termination = scnr.nextLine();
         
         if (termination.toLowerCase().equals("exit")) {
            continuePlay = false;
         }
      }

   }  //end main() 
   //stop
} //end class   