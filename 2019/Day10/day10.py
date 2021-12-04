import math

def render_map(star_map):
    for row in star_map:
        print(' '.join(map(str, row)) )

def count_astroids(star_map,start_y,start_x,debug=0):
    asteroid_count=0
    y=0
    star_map=list(star_map)
    for row in star_map:
        x=0
        # print("Row: " + str(y))
        for col in star_map:
            # print("Col:" + str(x))
            if(star_map[y][x]=="#" and (not (x==start_x and y==start_y))):
                if(debug>0):
                    print(str(y)+", "+str(x))
                dif_x=x-start_x
                dif_y=y-start_y


                if(dif_y!=0 and dif_x!=0):
                    y_left=int(dif_y)

                    asteroid_found=1
                    while(abs(y_left)>0):
                        if((dif_x*y_left)%dif_y==0):
                            if(debug==2):
                                print("Looking at: " + str(start_y+y_left) + ", " + str(int(start_x+dif_x*y_left/dif_y)))
                            if(y_left!=dif_y and star_map[start_y+y_left][int(start_x+dif_x*y_left/dif_y)]=="#"):
                                asteroid_found=0
                        if(y_left>0):
                            y_left-=1
                        else:
                            y_left+=1
                    asteroid_count+=int(asteroid_found)
                    if(debug>1):
                        print(asteroid_found)
                else:
                    if(dif_y==0):
                        x_left=int(dif_x)
                        asteroid_found=1
                        while(abs(x_left)>0):
                            if(x_left!=dif_x and star_map[y][start_x+x_left]=="#"):
                                asteroid_found=0                           
                            if(x_left>0):
                                x_left-=1
                            else:
                                x_left+=1
                        asteroid_count+=int(asteroid_found)
                        if(debug>1):
                            print(asteroid_found)
                    else:
                        y_left=int(dif_y)
                        asteroid_found=1
                        while(abs(y_left)>0):
                            if(y_left!=dif_y and star_map[start_y+y_left][x]=="#"):
                                asteroid_found=0                           
                            if(y_left>0):
                                y_left-=1
                            else:
                                y_left+=1
                        asteroid_count+=int(asteroid_found)
                        if(debug>1):
                            print(asteroid_found)
            x+=1
        y+=1
    if(debug>0):
        print("Asteroid count: " + str(asteroid_count))
    return(asteroid_count)

def part1(filename,draw_maps=0):
    file = open(filename, "r")
    star_map=[]
    for line in file:
        star_map.append(list(line[:-1]))

    if(draw_maps==1):
        render_map(star_map)

    counter_map=[]

    y=0
    max_found=0
    location_found=[]
    for row in star_map:
        counter_map.append([])
        x=0
        for col in row:
            counter_map[y].append(".")
            if(col=="#"):
                count=count_astroids(star_map,y,x)
                if(count>max_found):
                    max_found=count
                    location_found=[x,y]
                counter_map[y][x]=count
            x+=1
        y+=1

    if(draw_maps==1):
        render_map(counter_map)
    print("Max: " + str(max_found))
    print("Found in:" + str(location_found))
    return max_found, location_found

def taxi_dis(point1, point2):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

def part2(filename,laser_location,draw_maps=0):
    file = open(filename, "r")
    star_map=[]
    for line in file:
        star_map.append(list(line[:-1]))

    star_map[laser_location[1]][laser_location[0]]="X"

    angle=0

    if(draw_maps==1):
        render_map(star_map)

    angle_map=star_map

    y=0
    max_found=0
    location_found=[]
    angle_dict={}
    for row in star_map:
        x=0
        for col in row:
            # print(str(x) + ", " + str(y))
            if(col=="#"):
                angle=math.atan2(x-laser_location[0],laser_location[1]-y)
                if(angle<0):
                    angle+=2*math.pi
                if angle in angle_dict.keys():
                    angle_dict[angle].append([x,y])
                else:
                    angle_dict[angle]=[[x,y]]
                angle_map[y][x]=round(angle,1)
            else:
                if(angle_map[y][x]=="X"):
                    angle_map[y][x]=" X "    
                else:
                    angle_map[y][x]=" . "
            x+=1
        y+=1
    if(draw_maps==1):
        render_map(angle_map)
    
    output_list=[]
    print(len(angle_dict.keys()))
    while(len(angle_dict.keys())>0):
        print(angle_dict)
        for key in sorted (angle_dict.keys()):
            value=angle_dict[key]
            if(len(value)==1):
                output_list.append(value[0])
                del angle_dict[key]
            else:
                closest_point=0
                i=1
                while(i<len(value)):
                    if(taxi_dis(value[i],laser_location)<taxi_dis(value[closest_point],laser_location)):
                        closest_point=i
                    i+=1
                output_list.append(value[closest_point])
                angle_dict[key].pop(closest_point)
                # print(closest_point)
                # print(value)

    return(output_list)

""" part1("Day10/ex0.txt")
part1("Day10/ex1.txt")
part1("Day10/ex2.txt")
part1("Day10/ex3.txt")
part1("Day10/ex4.txt")
part1("Day10/input.txt") """

file="Day10/input.txt"

total_asteroids, laser_location = part1(file)

print(laser_location)

output=part2(file,laser_location,1)

# The 1st asteroid to be vaporized is at 11,12.
print(output[0])
# The 2nd asteroid to be vaporized is at 12,1.
print(output[1])
# The 3rd asteroid to be vaporized is at 12,2.
print(output[2])
# The 10th asteroid to be vaporized is at 12,8.
print(output[9])
# The 20th asteroid to be vaporized is at 16,0.
print(output[19])
#The 50th asteroid to be vaporized is at 16,9.
print(output[49])
#The 100th asteroid to be vaporized is at 10,16.
print(output[99])
#The 199th asteroid to be vaporized is at 9,6.
print(output[198])
#The 200th asteroid to be vaporized is at 8,2.
print(output[199])
""" #The 201st asteroid to be vaporized is at 10,9.
print(output[200])
#The 299th and final asteroid to be vaporized is at 11,1.
print(output[298]) """

print(len(output))