import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;

public class MickeyMousePractice extends Canvas {
    public static void main(String[] args) {
        JFrame frame = new JFrame("My Drawing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Canvas canvas = new MickeyMousePractice();
        canvas.setSize(400, 400);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);
    }

    public void paint(Graphics g) {
        g.setColor(Color.black);
        // draw main head for mickey mouse
        // asume we have coordinates x and y, we know size of head
        int x = 200;
        int y = 200;
        int size = 100;
        int recursions = 5;
        //draw head using above values
        g.fillOval(x, y, size, size);
        //call recursive method to draw ears until we reach the base case
        recursiveMickey(x, y, size, recursions, g);
    }

    //method to take in x, y, size of head and recursions and ears until recursions = 0
    public void recursiveMickey(int x, int y, int size, int recursions, Graphics g) {
        //base case: if recursions = 0, stop
        if (recursions == 0) {
            return;
        }
        //decrease size for ears by half
        size = size/2;
        //decrease recursions by 1
        recursions = recursions - 1;
        //if recursions is greater than 0, call recursive method again with new values for the two newly created ears
        if (recursions > 0) {
            //draw ears
            g.fillOval(x - size/2, y - size/2, size, size);
            g.fillOval(x + size/2 + size, y - size/2, size, size);
            //call recursive method again
            recursiveMickey(x - size/2, y - size/2, size, recursions, g);
            recursiveMickey(x + size/2 + size, y - size/2, size, recursions, g);
        }
    }
}