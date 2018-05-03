package baekjoon;

import java.util.Scanner;

public class Q1001 {

	public static void main(String[] args) {
		
		int A;
		int B;
		int minus;
		
		Scanner scan = new Scanner(System.in);
		
		A = scan.nextInt();
		B = scan.nextInt();
		
		if(A>0 && B<10) {
			minus = A - B;
			System.out.println(minus);
		} else {
			System.out.println("A>0, B<10 이어야 합니다.");
		}
	}

}

// memory : 12168 KB , time : 120 MS
