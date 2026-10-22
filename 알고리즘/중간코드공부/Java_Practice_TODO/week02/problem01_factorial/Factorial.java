// 2주차 1번: 재귀를 이용한 팩토리얼 계산
// 제공된 PDF의 기본 코드 및 main() 보존 / 구현할 함수만 TODO 처리
// TODO에 들어 있는 throw는 임시 표시이므로, 직접 구현할 때 삭제하세요.

import java.util.Scanner;

public class Factorial {

       public static int factorial(int n) {

              if (n == 1 || n == 0)
                     return 1;
              return n * factorial(n - 1);

       }

       public static void main(String[] args) {

              Scanner sc = new Scanner(System.in);

              System.out.print("정수 입력: ");

              int n = sc.nextInt();

              System.out.println(n + "! = " + factorial(n));
              sc.close();
       }

}
