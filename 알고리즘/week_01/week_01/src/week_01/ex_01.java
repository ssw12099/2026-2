package week_01;
import java.util.Scanner;

public class ex_01 {
	
	public static int fac(int i) {
		if (i <= 1) {
            return 1;
        }
		return i * (fac(i-1));
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.print("정수 입력: ");
		int n = sc.nextInt();
		int f = fac(n);
		System.out.println(n + "! = "+ f);
	}

}
