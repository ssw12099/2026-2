# 주석칸

	.text
	.global main
main: 
	add $5, $4, $3		# $5 <- $4 + $3
	sub $6, $4, $3		# $6 <- $4 - $3
	addi $7, $4, 5		# $7 <- $4 + 5.
	
	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data
myStr:	.asciiz "20235190 : sosunwoong"