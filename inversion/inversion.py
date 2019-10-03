# input the location of the text 
# return a int_list and its length
def read_txt(txt_location):
    int_lines=[]
    f = open(txt_location, "r")
    lines=f.read().splitlines()
    f.close()
    for line in lines:
        int_lines.append(int(line))
    count=len(int_lines)
    print(count)
    return int_lines,count

# the main inversion count algorithm 
# input : the list consisting all the integers and the length
# output: the sorted list and the number of inversion
def sort_and_count(lines,n):
    if n==1:
        return lines,0
    else:
        n1=n//2
        r= n % 2
        b,x=sort_and_count(lines[0:n1+r],n1+r)
        c,y=sort_and_count(lines[n1+r:n],n-n1-r)
        print(len(b))
        print(len(c))
        d,z=countsplitinv(b,c,n)
        return d,x+y+z

# the function that merge the list and count the number of split inversions
# input : the left list, the right list, the length of the whole list
# output: the sorted list and the number of split inversions

def countsplitinv(b,c,n):
    # initialization is also important
    i=0
    j=0
    z=0
    d=[]
    left=n//2+n%2
    for k in range(n):
        # pay attention to the condition "list out of range"
        if i==left:
            d.append(c[j])
            j+=1
            z+=left-i
        elif j==n-left:
            d.append(b[i])
            i+=1
        else:
            if b[i] <= c[j] :
                d.append(b[i])
                i+=1
            else :
                d.append(c[j])
                j+=1
                z+=left-i
    return d,z
