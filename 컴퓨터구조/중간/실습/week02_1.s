# 주석칸



	.text
	.global main
main: 
	# myStr 프린트 !
	li $v0, 4
	la $a0, myStr	# la 명령어: load address (주소가져와)
	syscall
	
	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

		.data

myStr:	.asciiz "20235190 : sosunwoong"