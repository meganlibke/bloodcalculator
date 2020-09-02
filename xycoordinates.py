## function
def interface():
    print("XY Coordinates Program")
    coords = [(1,2), (3,4)]#int(input("Input your coordinates in a tuple: "))
    [slope,offset]=xyline_coordinates(coords)
    xloc = input("Input your x-loc: ")
    result = new_location(slope, offset, xloc)
    print(result)

def xyline_coordinates(coords):
    slope = (coords[0][1]-coords[1][1])/(coords[0][0]-coords[1][0])
    offset=coords[0][1]-slope*coords[0][0]
    print(slope,offset)
    return slope, offset

def new_location(slope,offset, xval):
    yval = slope*int(xval) + offset
    return yval

if "__name__" == "__main__":
    interface()
    #[slope,offset]=xline_coordinates([(1,2), (3,4)])
    #print(new_location(slope,offset,2))
