import pygame as pg
import sys,time
from random import randint

pg.init()
side = 30
w = 17
h = 15
num = 1
disp = pg.display.set_mode((w * side, h * side))

game_running = 0


dirs = [pg.K_RIGHT, pg.K_DOWN, pg.K_LEFT, pg.K_UP]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake = [(7, 3), (7, 4)]
imgs = []
direction = 0
apple_idx = 0
apple_name = ''
apple = None
fTime = 20
sucKey = ''
SUCTIME = 'sucTime'
SUCRANGE = 'sucRange'
SUCLENGTH = 'sucLen'
CURTIME = 'currentTime'
FOODNUMBER = 'foodNumber'
failMsg = ''
success = {SUCTIME:300,SUCRANGE:10,SUCLENGTH:40,CURTIME:0,FOODNUMBER:0}
# sucTime = 300
# sucRange = 10
# sucLen = 40

def food_time(t):
    global fTime
    fTime = t

def success_time(t):
    global sucKey
    sucKey = 'sucTime'
    success[sucKey] = t
    success[CURTIME] = time.clock()

def success_number(n):
    global sucKey
    sucKey = 'sucRange'
    success[sucKey] = n
    success['foodNumber']=0

def success_length(n):
    global sucKey
    sucKey = 'sucLen'
    success[sucKey] = n

def place_food(idx):
    global apple_idx,apple
    apple = (randint(0, w - 1), randint(0, h - 1))
    while apple in snake:
        apple = (randint(0, w - 1), randint(0, h - 1))
    apple_idx = idx
    # return a

def add(n):
    global num,apple_name
    num = n
    apple_name = ''

def end():
    global num,apple_name
    num = 0
    apple_name='dilei'
    # print('end')

def check_edge():
    global direction
    x = snake[-1][0] + dx[direction]
    y = snake[-1][1] + dy[direction]
    if x<0:
        if y<=0:
            direction = 1
        elif y>=h-1:
            direction = 3
        else:
            direction = 1
    if x>=w:
        if y <= 0:
            direction = 1
        elif y >= h - 1:
            direction = 3
        else:
            direction = 1
    if y<0:
        if x<=0:
            direction = 0
        elif x>=w-1:
            direction = 2
        else:
            direction = 0
    if y>=h:
        if x<=0:
            direction = 0
        elif x>=w-1:
            direction = 2
        else:
            direction = 0

def check_collisions():
    global failMsg
    head = snake[-1]
    for i in range(len(snake) - 1):
        if head == snake[i]:
            # print("吃到自己")
            failMsg = '蛇咬到了自己！'
            return 2
    if head[0] >= w or head[0] < 0:
        return 3
    if head[1] >= h or head[1] < 0:
        return 3
    if head == apple:
        return 1
    return 0

for i in range(6):
    img = pg.image.load("{}.png".format(i+1))
    # img = pg.transform.scale(background, (self.WIDTH, self.HEIGHT))
    img = pg.transform.scale(img, (side, side))
    imgs.append(img)



clock = pg.time.Clock()
f = pg.font.Font('chanyujinge.ttf', 24)

# def

def eat():
    global game_running,direction,snake,fTime,num,apple_name,sucKey,failMsg
    # print(num, apple_name)
    game_running = 0
    # print(game_running)
    success[FOODNUMBER]+=1
    dup = 0   # It is convenient to call it once when returning, reducing the failure caused by the user's too late operation
    t1 = time.clock()
    while True:
        t2 = time.clock()
        if t2 - t1 > fTime and game_running!=3:
            # place_food(randint(1, 6))
            return
        clock.tick(5)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                exit(0)
                # break
            if e.type == pg.KEYDOWN:
                if game_running == 0:
                    game_running = 1
                if e.key == pg.K_SPACE:
                    # if game_running!=3:
                    #     game_running = 3
                    # else:
                    #     game_running = 1
                    pass
                    # game_running = 0
                    # snake = [(7, 3), (7, 4)]
                    # direction = 0
                    # apple = place_apple()

                for i in range(4):
                    if e.key == dirs[i] and direction != (i + 2) % 4:
                        direction = i

        if sucKey==SUCTIME:
            suc_t = time.clock()
            # print(suc_t-success[CURTIME],success[sucKey])
            if (suc_t-success[CURTIME])>success[sucKey]:
                disp.blit(f.render("恭喜你，你坚持了"+str(success[sucKey])+"秒！",False,pg.Color("blue")),(3*side,3*side))
                pg.display.update()
                game_running = 3
        if sucKey==SUCLENGTH:
            leng = len(snake)
            if leng >= success[sucKey]:
                disp.blit(f.render("恭喜你，蛇的长度达到了" + str(success[sucKey]) + "节！", False, pg.Color("blue")),
                          (3 * side, 3 * side))
                pg.display.update()
                game_running = 3
        if sucKey == SUCRANGE:
            if success[FOODNUMBER]>=success[sucKey]:
                disp.blit(f.render("恭喜你，你已经吃了" + str(success[sucKey]) + "个食物！", False, pg.Color("blue")),
                          (3 * side, 3 * side))
                pg.display.update()
                game_running = 3

        if game_running == 2:
            # disp.fill(pg.Color("black"))
            disp.blit(f.render(failMsg+"游戏失败!", False, pg.Color("blue")), (3 * side, 3 * side))
            pg.display.update()
            game_running = 3
        if game_running == 3:
            snake = [(7, 3), (7, 4)]
            continue
        if dup == 0:
            check_edge()
            snake.append((snake[-1][0] + dx[direction], snake[-1][1] + dy[direction]))
            coll = check_collisions()
            # print(coll)
        else:
            dup += 1

        if coll == 2:
            game_running = 2
            pass
        elif coll == 1:
            dup += 1
            if num > 0:
                tail = snake[0]
                for i in range(num-1):
                    snake.insert(0,tail)
            elif num == 0 and apple_name=='dilei':
                # p = snake[-1]
                # snake.clear()
                # snake.append(p)
                # print(num)
                failMsg = '你不小心吃到了地雷！'
                # print(failMsg)
                game_running = 2
                dup = 0

            else:
                snake.pop(0)
                # print(num,len(snake))
                for i in range(-num):
                    if len(snake) > 2:
                        snake.pop(0)
            # print(snake)


            # return
            # pass
        elif coll == 0:
            snake.pop(0)
        disp.fill(pg.Color("black"))
        # print(snake)
        for i in range(len(snake)):
            pg.draw.rect(disp, pg.Color("green"), pg.Rect(snake[i][0] * side, snake[i][1] * side, side, side))

        if dup==0:
            disp.blit(imgs[apple_idx - 1], (apple[0] * side, apple[1] * side))
        # pg.draw.rect(disp, pg.Color("red"), pg.Rect(apple[0] * side, apple[1] * side, side, side))
        pg.display.update()
        if dup>=1:
            return

if __name__ == '__main__':
    # print("便便，-2，石头，-1，汉堡，+4，香蕉，+2，玉米，+1，地雷，死亡")
    food_time(15)
    success_length(40)
    success_number(10)
    success_time(180)
    for i in range(1000):
        idx = randint(1,6)
        place_food(idx)
        if idx == 1:
            add(-2)
        if idx == 2:
            add(4)
        if idx == 3:
            add(-1)
        if idx == 4:
            add(2)
        if idx == 5:
            add(1)
        if idx == 6:
            end()
        eat()
        # print(snake)
    pass
