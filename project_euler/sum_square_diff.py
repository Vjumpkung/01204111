def sigma_i(x):
    sumPowerOne = (((x)*(x+1))/(2))
    return (sumPowerOne)
def sigma_i_square (x):
    sumSquare = (x*(x+1)*(2*x+1))/6
    return(sumSquare)
def sigma_i_cube (x):
    sumCube = (x*(x+1)/2)**2
    return(sumCube)

i = 100
diff = sigma_i_cube(i) - sigma_i_square(i)

