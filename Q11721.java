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
			System.out.println("문장의 길이는 1이상 100이하여야 합니다.");
		}
	}
}


// 알파벳 소문자, 대문자만 받게 해주는 판별코드가 없음 


// memory : 12120 KB , time : 144 MS

