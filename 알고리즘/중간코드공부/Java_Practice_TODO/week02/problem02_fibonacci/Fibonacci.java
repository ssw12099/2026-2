// 2주차 2번: 재귀를 이용한 피보나치 수열
// 제공된 PDF의 기본 코드 및 main() 보존 / 구현할 함수만 TODO 처리
// TODO에 들어 있는 throw는 임시 표시이므로, 직접 구현할 때 삭제하세요.

import java.util.Scanner;

public class Fibonacci {

     public static int fibonacci(int n) {

          if (n <= 1)
               return 1;
          return fibonacci(n - 1) + fibonacci(n - 2);

     }

     public static void main(String[] args) {

          Scanner sc = new Scanner(System.in);

          System.out.print("n 입력: ");

          int n = sc.nextInt();

          System.out.println("F(" + n + ") = " + fibonacci(n));
          sc.close();
     }

}
