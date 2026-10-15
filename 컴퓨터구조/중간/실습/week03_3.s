# 주석칸

	.text
	.global main
main: 
	# “.data”에 3개의 정수형(.word) 변수, myAge, Snum, year를 각각 지정하고, 3개의 변수의 총합을 계산하여 “.data”에 정수형 변수명 Final에 저장하고 그 값을 프린트하는 MIPS Assembly 코드를 작성하라.

	# (정수 값 프린트를 위하여, system call service code 1을 사용하라! $a0에 프린트하고자 하는 정수 값을 넣고 $v0 ← 1로 설정한 후 syscall)
	

	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data
myAge:	.word 49
Snum:	.word 35814
year:		.word 1992
FInal:		.word 0
