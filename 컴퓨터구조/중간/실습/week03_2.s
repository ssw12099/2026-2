# 주석칸

	.text
	.global main
main: 
	add $s0, $s1, $s2
	sub $t0, $t3, $t5 

	addi $s0, $s1, 5
	addi $t0, $s3, -12
	lw $t2, 32($0)
	sw $s1, 4($t1)

	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data
