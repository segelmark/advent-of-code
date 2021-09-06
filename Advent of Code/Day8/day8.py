def open_image(image,width,height):
    layers=[]

    i=0
    for pixel in image:
        layer=i//(width*height)

        if(i%(width*height)==0 or i==0):
            layers.append([])
        row=(i-layer*width*height)//width

        if(i%(width)==0 or i==0):
            layers[layer].append([])

        layers[layer][row].append(pixel)
        i+=1

    return layers

def count_numbers_in_layer(layer, number):
    count_numbers=0
    for row in layer:
        for column in row:
            if(column==str(number)):
                count_numbers+=1
    return count_numbers

def part1(layers):
    zeros_per_layer=[]
    for layer in layers:
        zeros_per_layer.append(count_numbers_in_layer(layer,"0"))


    print(zeros_per_layer)

    min_zero_layer=zeros_per_layer.index(min(zeros_per_layer))

    print(layers[min_zero_layer])

    print(count_numbers_in_layer(layers[min_zero_layer], "1")*count_numbers_in_layer(layers[min_zero_layer], "2"))

def part2(layers):
    r=0
    output=layers[0]
    for row in layers[0]:
        c=0
        for column in row:
            for layer in layers:
                if(layer[r][c]=="0"):
                    output[r][c]=" "
                    break
                if(layer[r][c]=="1"):
                    output[r][c]="X"
                    break
            column=column
            c+=1
        r+=1
    return(output)

def render_layer(layer):
    for row in layer:
        print(' '.join(map(str, row)) )

part1(open_image("123456789012",3,2))

render_layer(part2(open_image("0222112222120000",2,2)))

filename = "Day8/input.txt"
file = open(filename, "r")
image=file.readline()
layers = open_image(image,25,6)
part1(layers)
render_layer(part2(layers))