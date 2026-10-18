# 주석칸
	.text
	.global main
main: 
	addi $a0, $0, 2		# 첫번째 인자: 2
	addi $a1, $0, 3		# 첫번째 인자: 3
	addi $a2, $0, 4		# 첫번째 인자: 4
	addi $a3, $0, 5		# 첫번째 인자: 5

	jal diffofsums

	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

# Diffofsums 함수정의
diffofsums:		# diffofsums 함수
	add $t0, $a0, $a1
	add $t1, $a2, $a3
	sub $s0, $t0, $t1
	add $v0, $s0, $0
	jr	$ra		# return

		.data