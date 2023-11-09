/* Ariel Webster
 * 3/27/19
 * 
 * updated: 3/2/23
 *
 * InClass example File IO reading and parsing a file.
 * Reads in every word in the Examples.txt file 
 * adds each word to an ArrayList
 * Prints the ArrayList
 */

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;


public class FileRead {
    
	public static void main(String[] args) throws IOException {
		Scanner scan = null; // to get information in
	    ArrayList al = new ArrayList(); // to store the information we get
       
       try{
    	   scan = new Scanner(new FileReader("Example.txt")); // this file needs to be in the same folder/project 
    	   													  // as this .java file.
    	   while(scan.hasNext()){ // while there is more in the file that you have not read into your program
    		   al.add(scan.next()); // read the next thing into your program and save it in the next place in your array list
    	   }
       }finally{
    	 //it is important to close the stream we created above. This should be the last thing we do, since after
			// we close the stream nothing more can be written to the file, therefore we put it in the finally block.
			// We can't close the stream if nothing is there so we check to make sure the object is not null first.
    	   if(scan != null){
    		   scan.close();
    	   }
       }
       //print out everything in our arraylist as a check. 
       for(int i = 0; i < al.size(); i++){
    	   System.out.println(al.get(i));
       }
		
	}
}


/* 
 * You try: 
 * 
 * 1) Change the code so that it reads in ENIACProgrammers.txt 
 * 
 * 2) Change the code so that it adds only the names to the ArrayList
 * 
 * 3) Change the file so that each place in the ArrayList holds the first and last name of a programmer. eg (Kay McNulty)
 * 
 * 4) Make sure your program can work with various inputs - test the program with one fewer or one more programmer in the file
 * 
 * 5) Make sure your program can work with various inputs - create empty lines in the file and change your program so it still works.
 * 
 * 6) Create a Person class that has both a first name attribute and a last name attribute. 
 * Read in this file making Person objects out of each line. 
 * Add each person object to an ArrayList instead of the String names.
*/