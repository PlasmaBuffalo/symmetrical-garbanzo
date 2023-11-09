//import random
import java.util.Random;
import java.util.Scanner;

//import gui 
import javax.swing.*;
//import graphics
import java.awt.*;
import java.io.FileNotFoundException;
import java.io.FileReader;
//import arraylist
import java.util.ArrayList;

public class CoordGraphing extends Canvas{

    //create arraylist to hold x-y coordinate pairs
    ArrayList<String> x = new ArrayList<String>();
    ArrayList<Integer> y = new ArrayList<Integer>();
    public static void main(String[] args) {
        //instance of cg
        CoordGraphing cg = new CoordGraphing();
        //read in coords.txt file and store in arraylist
        JFrame frame = new JFrame("My Drawing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Canvas canvas = new fileReadGUIPractice();
        canvas.setSize(400, 400);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);
        //create new instance of Scanner
        Scanner scan = null;
        //try to read in file
        try {
            scan = new Scanner(new FileReader("coords.txt"));
            //while there is more in the file that you have not read into your program
            while (scan.hasNext()) {
                //add the next x coordinate to the x arraylist
                cg.x.add(scan.next());
                //if there is another value in the file
                if (scan.hasNext()) {
                    //add the next y coordinate to the y arraylist
                    cg.y.add(scan.nextInt());
                }
            }
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();}

            //print out the x and y coordinates
            System.out.println("x: " + cg.x);
            System.out.println("y: " + cg.y);
    }

    //paint method to add points to graph
    public void paint(Graphics g) {
        g.setColor(Color.black);
        //for loop to add points to graph
        //print out the x and y coordinates
        for (int i = 0; i < x.size(); i++) {
            System.out.println("x: " + x.get(i) + " y: " + y.get(i));
            //add the points to the graph
            g.fillOval(Integer.parseInt(x.get(i)), y.get(i), 5, 5);
        }
    }
}
