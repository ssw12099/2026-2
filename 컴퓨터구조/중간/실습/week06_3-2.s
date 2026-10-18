# 주석칸
	.text
	.global main
main: 
	addi $a0, $0, 2		# 첫번째 인자: 2
	addi $a1, $0, 3		# 첫번째 인자: 3
	addi $a2, $0, 4		# 첫번째 인자: 4
	addi $a3, $0, 5		# 첫번째 인자: 5

	addi $sp, $sp, -8	# 메모리 할당
	sw $s0, 8($sp)		# push	
	sw $t0, 4($sp)		# push

	jal diffofsums

	lw $t1, 0($sp)		# pop
	lw $t0, 4($sp)		# pop
	addi $sp, $sp, 8		# 메모리 해제

	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

# Diffofsums 함수정의
diffofsums:		# diffofsums 함수

	# diffofsums에서 사용할 레지스터 값을 저장해 놓자 !!!
	addi $sp, $sp, -4	# 메모리 할당
	sw $t1, 0($sp)		# push

	# 실제 함수 연산 맘껏 맘껏 하자 !!!!	
	add $t0, $a0, $a1
	add $t1, $a2, $a3
	sub $s0, $t0, $t1
	add $v0, $s0, $0

	# diffofsums에서 사용할 레지스터 값을 돌려놓자 !!! ( 역순 )
	lw $s0, 8($sp)		# pop
	addi $sp, $sp, 4		# 메모리 해제


	jr	$ra		# return

		.data