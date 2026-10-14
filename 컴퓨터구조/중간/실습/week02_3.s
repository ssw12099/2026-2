# 주석칸

	.text
	.global main
main: 
	lw $7, myIntA	# myIntA --> $7
	addi $7, $7, 1	# $7 <-- $7 + 1
	sw $7, myIntB	# $7 --> myIntB 
	
	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data
myIntA:	.word 9	#메모리주소: 10010000, 값: 00000009
myIntB:	.word 0	#메모리주소: 10010004, 값: 00000000