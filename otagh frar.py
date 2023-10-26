def rotate(list_):
    return list_[-1:] + list_[:-1]
    
    
first_line = input().split()
second_line = input().split()

accepted = False
for i in range(0, len(first_line)):
    for j in range(0, len(second_line)):
        result1 = (int(''.join(first_line[1])) + int(''.join(second_line[1]))) % 10
        result2 = (int(''.join(first_line[2])) + int(''.join(second_line[2]))) % 10
        result3 = (int(''.join(first_line[3])) + int(''.join(second_line[3]))) % 10
        result = int(str(result1) + str(result2) + str(result3))
        if result % 6 == 0:
            accepted = True
            
        second_line = rotate(second_line)
        
    first_line = rotate(first_line)
    

if accepted:
    print('Boro joloo :)')
else:
    print('Gir oftadi :(')
