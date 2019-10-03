package baekjoon;

public class Q2775 {

	public static void main(String[] args) {
		int result = findliving(4,4,0);
		System.out.println(result);
		

	}
	public static int findliving(int k, int n, int result) {
		for(int i=k; i>=0; i--) {
			System.out.println("i : "+i);
			for(int j=n; j>=1; j--) {
				System.out.println("j : "+j);
				result += (j*(j+1))/2;
				System.out.println("result == "+result);
			}
			--n;
		}
		return result;
		
		
	}

}
