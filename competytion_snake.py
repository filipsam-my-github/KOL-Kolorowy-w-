to_int=lambda str_list: [int(i)-1+((number+1)//3) for number,i in enumerate(str_list)]

m=0

with open("snake.txt","r") as file:
    datas=[]
    for line in file:
        datas.append(line.split())
    n_datas=datas
    for data in datas:
        try:
            if int(data[0])>m:
                m=data[0]
            if int(data[1])>m:
                m=data[1]
        except:
            pass
    m=int(m)
    print()
    file.close()


def draw_empty_map(m):
    return [["." for i in range(m)] for i in range(m)]

def draw_object(game_map,objects_rects):
    for object_rects in objects_rects:
        for object_rect in object_rects:
            game_map[object_rect[1]][object_rect[0]]=object_rect[2]
    return game_map
        
def move(x,y,snake_rects,snack_rects):
    c_skack_rect=None
    for snack_rect in snack_rects:
        if snack_rect[0]==snake_rects[len(snake_rects)-1][0]+x and snack_rect[1]==snake_rects[len(snake_rects)-1][1]+y:
            snake_rects.append(snack_rect)
            snack_rects.remove(snack_rect)
            return snake_rects,snack_rects
    for snak_rect_number in range(len(snake_rects)):
        if len(snake_rects)==snak_rect_number+1:
            snake_rects[snak_rect_number][1]+=y
            snake_rects[snak_rect_number][0]+=x
            continue
        snake_rects[snak_rect_number][1]=snake_rects[snak_rect_number+1][1]
        snake_rects[snak_rect_number][0]=snake_rects[snak_rect_number+1][0]
    return snake_rects,snack_rects
    
def check_colision():
    pass

snacks_rects=[]        
game_map=draw_empty_map(m)
snake_rects=[[0,0,0]]
game_map=draw_object(game_map,[snake_rects,snacks_rects])
#for game_ma in game_map:
    #print(game_ma,"aaa")
 

for data in n_datas:
    x=0
    y=0
    if data[0].isnumeric():
        #print(data)
        data=to_int(data)
        data[2]%=(m**2-1)
        snacks_rects.append([data[1],data[0],data[2]])
        game_map=draw_object(game_map,[snake_rects,snacks_rects])
        # for map in game_map:
        #     print()
        # for map in game_map:
        #     print(map)
    elif data[0]=="Z":
        pass
        #if game_map[int(data[1])-1][int(data[2])-1]==3:
           #for i in range(3):
            #    print("~~~~~~")
            #for mm in game_map:
            #    print(mm)
        #
        # print(int(data[1])-1,int(data[2])-1)
        #print()
        #print()
        #print(int(data[1])-1,int(data[2])-1)
        print(game_map[int(data[1])-1][int(data[2])-1])
        #for line in game_map:
        #    print(line)
        #for line in game_map:
        #    print()
        #for game_ma in game_map:
            #print(game_ma)
    else:
        #game_map=draw_empty_map(m)
        match data[0]:
            case "P":
                #for map in game_map:
                #    print()
                game_map=draw_empty_map(m)
                snake_rects,snacks_rects=move(1,0,snake_rects,snacks_rects)
                
                #print()
                #print()
                game_map=draw_object(game_map,[snake_rects,snacks_rects])
                #for i in game_map:
                #    print(i)
                #for map in game_map:
                #    print(map)
                #snake_rects,snacks_rects=move(1,0,snake_rects,snacks_rects)
            case "L":
                #for map in game_map:
                #    print()
                game_map=draw_empty_map(m)
                snake_rects,snacks_rects=move(-1,0,snake_rects,snacks_rects)
                game_map=draw_object(game_map,[snake_rects,snacks_rects])
                
                #print()
                #print()
                #for i in game_map:
                #    print(i)
                #for map in game_map:
                #    print(map)
                #snake_rects,snacks_rects=move(-1,0,snake_rects,snacks_rects)
            case "D":
                #for map in game_map:
                #    print()
                game_map=draw_empty_map(m)
                snake_rects,snacks_rects=move(0,1,snake_rects,snacks_rects)
                
                #print()
                #print()
                game_map=draw_object(game_map,[snake_rects,snacks_rects])
                #for i in game_map:
                #    print(i)
                
                #for map in game_map:
                #    print(map)
                #snake_rects,snacks_rects=move(0,1,snake_rects,snacks_rects)
            case "G":
                #for map in game_map:
                #    print()
                game_map=draw_empty_map(m)
                snake_rects,snacks_rects=move(0,-1,snake_rects,snacks_rects)
                
                
                #print()
                #print()
                game_map=draw_object(game_map,[snake_rects,snacks_rects])
                #for i in game_map:
                 #   print(i)
                #for map in game_map:
                #    print(map)
        
