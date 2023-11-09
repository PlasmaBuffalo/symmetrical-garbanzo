import java.awt.AlphaComposite;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.AlphaComposite;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class BackPaint extends Canvas{
	Image bg;
	
	public BackPaint(){
		ImageIcon obj = new ImageIcon("stars.jpg");
		bg = obj.getImage();
	}
	
	public void paint(Graphics g){
		g.drawImage(bg, 0,0,null);
		g.setColor(Color.yellow);
		g.drawLine(0, 0, 200, 200);
	}

	public static void main(String[] args){
		JFrame window = new JFrame("Drawontheimage");
		BackPaint bg = new BackPaint();
		window.setSize(300, 300);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.add(bg);
		window.setVisible(true);
	}


}
