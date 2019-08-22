package baekjoon;

import java.util.Arrays;
import java.util.OptionalInt;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Q2108 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int N = scan.nextInt();
		scanf(N);

	}
	
	public static void scanf(int N) {
		Scanner scan = new Scanner(System.in);
		int sum = 0;
		int avg = 0;	
		int[] medianArray=new int[N];	  
		int median = 0;	
		int arraySize = medianArray.length;
		int medianResult=0;

		
		for(int i=0; i<medianArray.length; i++) {
			medianArray[i] = scan.nextInt();
			Arrays.stream(medianArray);
			
			sum += medianArray[i];	
			avg = sum / N;		// 1. »ê¼úÆò±Õ
			
			median = arraySize/2;
			medianResult=medianArray[median];	// 2. Áß¾Ó°ª
			
		}
		
		System.out.println(avg);
		System.out.println(medianResult);

		
	}
	
}
