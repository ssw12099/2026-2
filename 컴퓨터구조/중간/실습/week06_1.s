# 주석칸
	.text
	.global main
main: 
	jal	simple		# simple();
	add	$s0, $s1, $s2	# a = b + c;
	
	# 프로그램 끝내기
	li $v0, 10	# li 명령어: load immediate (값을 읽는다) -> $v0
	syscall

# simple 함수 정의
simple:			# simple 함수
	jr	$ra		# return
	
		.data