package baekjoon;

import java.util.Scanner;

public class Q2839 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int result;
		int[] three;
		three = new int[] {0,2,4,1,3};
		
		if(N>=10&&N<=5000) {
			if(N%5==0) {
				result = N/5;
				System.out.println(result);
			} else {
				int a = N%5;
				int b = three[a];
				int c = (N-(3*b))/5;
				result = b+c;
				System.out.println(result);
			} 
		} else if(N>=3&&N<10) {
			if(N%5==0){
				result = N/5;
				System.out.println(result);
			} else if(N%3==0){
				result = N/3;
				System.out.println(result);
			}else {
				int alpha = N%5;
				if(alpha!=3) {
					result = -1;
					System.out.println(result);
				}else {
					int beta = N/5;
					int zeta = N/3;
					result = beta+zeta;
					System.out.println(result);
				}
			}
		} else {
			System.out.println("out of range");
		}
	}
}

// memory : 12116 KB, time : 120 MS


