package baekjoon;

import java.util.Scanner;

public class Q2448 {

	public static void main(String[] args) {
/*		for(int i=0;i<3;i++) {
			for(int j=0;j<4;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}*/
/*		int k = 0;*/
		
		
		Scanner scan = new Scanner(System.in);
		
		int k = scan.nextInt();
		int N = 3*2^k;
		star(N);

	}
	public static void star(int n) {		
		for(int i=0; i<n; i++) {
			for(int j=1;j<6;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
	}

}
