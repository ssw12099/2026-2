# 주석칸

	.text
	.global main
main: 
	lw $t0, myVal	# $t0 <-- 0x23456789
	sw $t0, myVal2	# myVal2 <-- 0x23456789

	# la: load address
	la $t1, myVal2	# myVal2의 주소를 $t1에 가져오기 !!!!
	lb $s0, 1($t1)

	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data
myVal: .word 0x23456789
myVal2: .word 0
