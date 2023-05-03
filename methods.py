def area_of_rectangle(width, height):
    area = width*height
    return area
 
def perimeter_of_rectangle(width, height):
    perimeter = 2 * (width + height)
    return perimeter

def volume_of_parallelepiped(length, width, height):
    volume = length*width*height
    return volume

def test_surface_area_of_parallelepiped(length, width, height):
    surface = 2*(length*width+width*height+length*height)
    return surface