import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.text.DecimalFormat;

public class program
{
	public static void main(String[] args)
    {
		JFrame frame = new JFrame("Example");
        MyPanel panel=new MyPanel();
        panel.setPreferredSize(new Dimension(400,400));
		frame.add(panel);
        panel.addMouseMotionListener(panel);
        panel.addMouseListener(panel);
        panel.addMouseWheelListener(panel);
        frame.pack();
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}

class MyPanel extends JPanel implements MouseMotionListener, MouseListener, MouseWheelListener
{
    
    public int x=0;
    public int y=0;
    public int w=10;
	public int color=255;
    public void paint(Graphics g)
    {
        //super.paint(g);
        
		Graphics2D g2=(Graphics2D)g;
        g2.setColor(Color.WHITE);
        //~ g2.fillRect(0,0,getWidth(),getHeight());
        //~ Color color = new Color(r, g, b);
        g2.setColor(new Color(255,0,0));
        g2.fillRect(75,150,250,125);
        g2.fillRect(135,125,125,31);
        g2.setColor(Color.WHITE);
        g2.fillRect(100,175,200,75);
        g2.setColor(new Color(color, color, color)); Font stringFont = new Font("SansSerif", Font.PLAIN, 32); g2.setFont( stringFont);
        g2.drawString("12:00 AM", 125, 225); //r+=15;
        
	}
    
    public void mouseDragged(MouseEvent e){}
    public void mouseMoved(MouseEvent e)
    {
        x=e.getX();
        y=e.getY();
        //~ repaint();
    }
    
    public void mouseClicked(MouseEvent e){}
    public void mouseEntered(MouseEvent e){}
    public void mouseExited(MouseEvent e){}
    public void mousePressed(MouseEvent e)
    {
        if((e.getButton()==1)&&((e.getX()>=100)&&(e.getX()<=300))&&((e.getY()>=175)&&(e.getY()<=250))) color=color-15;
        if(color<0) color=0;
        else if(color>255) color=255;
        repaint();
    }
    public void mouseReleased(MouseEvent e){}
    public void mouseWheelMoved(MouseWheelEvent e) {
        int notches = e.getWheelRotation();
        if(notches<0) notches=notches*-1;
        color=color/notches;
        color=Math.round( color*100);
        if (color>255) color=255;
        else if(color<0) color=0;
        repaint();
        notches=0;
	}
}
