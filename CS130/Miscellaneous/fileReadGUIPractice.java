import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/* Kayla Gormley 
 * 10/19/22
 * 
 * InClass practice File IO reading and parsing a file.
 * Reads in coordinates in coords.txt file 
 * 
 */
public class fileReadGUIPractice extends Canvas {

    // instance of main class for both methods
    ArrayList<String> xs = new ArrayList<String>(); // to store the information we get
    ArrayList<String> ys = new ArrayList<String>();

    public static void main(String[] args) throws IOException {
        JFrame frame = new JFrame("My Drawing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Canvas canvas = new fileReadGUIPractice();
        canvas.setSize(400, 400);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);

        fileReadGUIPractice fr = new fileReadGUIPractice();
        Scanner scan = null; // to get information in, out here to allow accessibility

        try {
            scan = new Scanner(new FileReader("coords.txt")); // this file needs to be in the same folder/project // as
                                                              // this .java file.
            while (scan.hasNext()) {// while there is more in the file that you have not read into your program
                fr.xs.add(scan.next());
                if (scan.hasNext()) {
                    fr.ys.add(scan.next());
                }
            }
        } finally {
            if (scan != null) {
                scan.close();
            }
        }
    }

    public void paint(Graphics g) {
        g.setColor(Color.black);
        // check access of xy and ys by printing their lengths and values
        System.out.println("xs length: " + xs.size());
        System.out.println("ys length: " + ys.size());
        System.out.println("xs: " + xs);
        System.out.println("ys: " + ys);
        // draw the points
        for (int i = 0; i < xs.size(); i++) {
            g.fillOval(Integer.parseInt(xs.get(i)), Integer.parseInt(ys.get(i)), 10, 10);
        }
        /*
         * int x = 0;
         * int y = 0;
         * System.out.println(xs.size());
         * for (int i = 0; i < xs.size(); i++) {
         * x = Integer.parseInt(xs.get(i));
         * y = Integer.parseInt(ys.get(i));
         * System.out.println(x);
         * System.out.println(y);
         * g.fillOval(x, y, 10, 10);
         * }
         */
    }
}