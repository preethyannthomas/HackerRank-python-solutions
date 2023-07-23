i = 0
while(i<=3):
    j = i
    while(j<=3):
        print(" ", end="")
        j = j+1
    j=3-i
    while(j<=3):
        print("* " , end = "")
        j = j+1
    print()
    i = i + 1


Output
    * 
   * * 
  * * * 
 * * * * 
