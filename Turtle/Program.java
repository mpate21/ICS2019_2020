import java.util.Scanner;
import java.util.*;
import java.io.*;
public class Program{
	public static void main (String[] args) {
		System.out.println("How many sides do you want for your polygon?");
		Scanner in = new Scanner(System.in);
		int num = in.nextInt();
		Turtle bob;
		bob = new Turtle();
		int c;
		c = 360;
		int Angle;
		Angle =(c /num);
		sideToAngles(num, bob, c, Angle);

	}

	public static void sideToAngles(int num,Turtle bob,int c,int Angle){
		if (num <=2){
			throw new IllegalArgumentException();
		}else {
			bob.speed(100);
			bob.left(Angle);
			bob.forward(100);
			c = (c-(Angle));
			if (c > 0){
				sideToAngles(num,bob,c,Angle);
			}
		}
	}
}
