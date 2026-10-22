# 자바 자료구조 실습 — 직접 구현용 (2·3·5·7주차)

첨부된 교수님 PDF의 **기본 코드와 main()을 유지**하고, `// 코드 작성` 자리만 `// TODO`로 표시한 실습용 Java 파일입니다.
**정답/완성 구현은 포함하지 않았습니다.**

## 사용법
1. 문제별 폴더 안의 `.java` 파일을 열어 `TODO`를 검색합니다.
2. 각 `throw new UnsupportedOperationException("TODO: ...");` 문장을 **삭제하고** 그 자리에 직접 코드를 작성합니다.
3. 각 폴더에서 파일을 컴파일하고 실행합니다. 예시:

```bash
javac Factorial.java
java Factorial
```

`throw`는 **아직 구현하지 않았다는 표시**이면서, 빈 함수 때문에 컴파일 오류가 나지 않도록 한 임시 문장입니다. TODO를 구현하기 전 실행하면 `UnsupportedOperationException`이 뜨는 것이 정상입니다.

## 문제 구성

| 주차 | 문제 | 파일 경로 | TODO 수 |
|---|---|---|---:|
| 2 | 1. 재귀를 이용한 팩토리얼 계산 | `week02/problem01_factorial/Factorial.java` | 1 |
| 2 | 2. 재귀를 이용한 피보나치 수열 | `week02/problem02_fibonacci/Fibonacci.java` | 1 |
| 2 | 3. 배열을 이용한 리스트 구현 | `week02/problem03_array_list/Main.java` | 5 |
| 2 | 4. 연결 표현을 이용한 리스트 구현 | `week02/problem04_linked_list/Main.java` | 7 |
| 3 | 1. 이진 트리의 기본 연산 구현 | `week03/problem01_binary_tree/BinaryTreeTest.java` | 12 |
| 5 | 1. 이진 트리의 순회 및 복사 구현 | `week05/problem01_traversal_copy/BinaryTreeTest.java` | 9 |
| 7 | 1. 이진 탐색 트리의 검색, 삽입, 삭제 및 분할 구현 | `week07/problem01_bst/BSTTest.java` | 5 |

## 주의사항
- **문제마다 독립된 폴더**로 구성했습니다. 서로 `Main`, `BTNode`, `BinaryTree` 등 클래스 이름이 겹치므로 폴더 전체 파일을 한 디렉터리로 합치지 마세요.
- `main()`은 PDF의 테스트 순서를 유지합니다. TODO 기능을 모두 구현한 다음 실행 결과를 PDF 예시와 비교하세요.
- 5주차 파일에는 편의를 위해 `java.util.Stack`, `java.util.Queue`, `java.util.LinkedList` import만 추가했습니다.
- 7주차의 코드가 긴 이유는 PDF에 나온 검색/삭제/분할 테스트를 **모두 포함**했기 때문입니다.
