package baekjoon;

import java.util.Scanner;

public class Q11721 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String tenSentence = scan.nextLine();
		
		tenSent(tenSentence);

	}
	public static void tenSent(String tenSentence) {
		int l = tenSentence.length();
		int a = tenSentence.length()/10;
		
		if (tenSentence.length()>0 && tenSentence.length()<=100) {
			for(int i=0; i<a; i++) {
				System.out.println(tenSentence.substring(10*i, 10*i+10));
			}
			System.out.println(tenSentence.substring(a*10, l));	
		}
		else {
			System.out.println("������ ���̴� 1�̻� 100���Ͽ��� �մϴ�.");
		}
	}
}


// ���ĺ� �ҹ���, �빮�ڸ� �ް� ���ִ� �Ǻ��ڵ尡 ���� 


// memory : 12120 KB , time : 144 MS

