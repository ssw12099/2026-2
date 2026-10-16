# 주석칸
	.text
	.global main
main: 
	# list 배열의 데이터의 합을 구하기
	# sum = 0
	# for(i=0; i<6; i++)
	#	sum = sum + list[ i ]
	# $s0 = array base address, $s1 = i, $t3 = sum

	la $s0, list	# list 주소를 가져와서 $s0에 넣기
	addi $s1, $0, 0	# $s1을 i index 변수로 사용 !
	addi $t3, $0, 0 	# $s1을 i index 변수로 사용 !
	addi $t2, $0, 6

loop:
	slt $t0, $s1, $t2		# i < 6
	beq $t0, $0, done	# 루프 탈출
	sll $t0, $s1, 2		# offset 계산: i*4
	add $t0, $t0, $s0		# address of myArray[ i ] = base 주소 + offset
	lw $s1, 0($t0)		# $t1 <- list[ i ]
	add $t3, $t3, $t1		# sum = sum + list[ i ]
	addi $s1, $s1, 1		# i = i + 1
	j loop

done:
	li $v0 , 1			# 합 프린트 !
	addi $a0, $t3, 0
	syscall

	li $v0, 10			# 프로그램 끝내기 위한 코드
	syscall
    
	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data
list:		.word 3, 5, 1, 0, 7, 2	# 3+5+1+0+7+2 = 18
