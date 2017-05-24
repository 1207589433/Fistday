#-*-coding:utf-8-*-
print_number=input("请输入：")
count=0
while count<10000000:
    #print 'loop:',count


    if count==print_number:
        print 'There you got the number:',count
        choice=raw_input("do you want to continue?")
        if choice=='n':
            break
        else:
            while print_number<=count:
                print_number=input('which loop do you want it te be printed out')
                if print_number<=count:
                    print '已经过了'
                else:
                    print '继续'
    else:
        print 'loop',count
    count+=1

else:
    print 'loop:',count