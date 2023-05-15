def check_prime_number(n):
    #flag = 0 => không phải số nguyên tố
    #flag = 1 => số nguyên tố
    flag = 1;
    if (n <2):
        flag = 0
        return flag  #Số nhỏ hơn 2 không phải số nguyên tố => trả về 0
    
    #Sử dụng vòng lặp while để kiểm tra có tồn tại ước số nào khác không
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break #Chỉ cần tìm thấy 1 ước số là đủ và thoát vòng lặp
    return flag
