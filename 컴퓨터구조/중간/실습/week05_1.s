# 주석칸
	.text
	.global main
main: 
	# myArray에 데이터 저장하기 1부터 5까지
	# for(i=0; i<5; i++)
	#		myArray[ i ] = i
	#
	# $s0 = array base address, $s1 = i
	la $s0, myArray	# myArray 주소를 가져와서 $s0에 넣기
	addi $s1, $0, 0	# $s1을 i index 변수로 사용 !
	addi $t2, $0, 5

loop:
	slt $t0, $s1, $t2		# i < 5
	beq $t0, $0, done	# 루프 탈출
	sll $t0, $s1, 2
	add $t0, $t0, $s0		# address of myArray[ i ]
	sw $s1, 0($t0)		# myArray[ i ] = i
	addi $s1, $s1, 1		# i = i + 1
	j loop
done:

	li $v0, 10			# 프로그램 끝내기 위한 코드
	syscall
    
	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data
limit1:	.word 5
myArray:	.space   20
limit2:	.word 6
list:		.word 3, 5, 1, 0, 7, 2
