def main():
    num_input = int(input())
    for x in range(num_input):
        seq_len = int(input())
        seq  = input()
        output = ''
        skip = False
        for c in seq:
            if c == 'A':
                output += 'T'
            elif c == 'T':
                output += 'A'
            elif c == 'C':
                output += 'G'
            elif c == 'G':
                output += 'C'
            else:
                print('Error RNA nucleobases found!')
                skip = True
				
        if not skip:
            print(output)
	
if __name__ == '__main__':
    main()