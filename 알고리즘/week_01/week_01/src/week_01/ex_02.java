package week_01;
import java.util.Scanner;

public class ex_02 {
	
	public static int fibonacci(int n) {
		 // 코드 작성
		if(n==0)return 0;
		else if(n==1)return 1;
		return fibonacci(n-1)+fibonacci(n-2);
		 }

	
	public static void main(String[] args) {
		 Scanner sc = new Scanner(System.in);
		 System.out.print("n 입력: ");
		 int n = sc.nextInt();
		 System.out.println("F(" + n + ") = " + fibonacci(n));
		 }
}
