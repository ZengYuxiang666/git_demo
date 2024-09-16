import pygame

# 初始化操作
pygame.init()
# 创建游戏窗口
# set_mode(大小）
window = pygame.display.set_mode((1200, 800))
# 设置游戏标题
pygame.display.set_caption("zje")
# 设置背景颜色
window.fill((255, 255, 255))


# ===================================游戏启动页面静态图==========================
# 1.显示图片
image1 = pygame.image.load("C:\pythonProject\图片\QQ图片20230813115056.jpg")

# 2.渲染图片
# blit(渲染对象，坐标）
window.blit(image1, (0, 0))

# 3.获取图片大小
w, h = image1.get_size()

# 4.旋转和缩放
# scale(缩放对象，目标大小）
new1 = pygame.transform.scale(image1, (200, 100))
window.blit(new1, (1000, 700))

# 5. rotozoom （缩放/旋转对象，旋转角度，缩放比例）
new2 = pygame.transform.rotozoom(image1, 180, 0.1)
window.blit(new2, (500, 700))


# ======================================显示文字===============================
# 1.创建字体对象
# Font（字体文件路径，字号）
font = pygame.font.Font('', 30)

# 2.创建文字对象
# render（文字内容，True，文字颜色，背景颜色）
text = font.render('zje', True, (255, 0, 0))

# 3.渲染到窗口上
window.blit(text, (0, 0))

# 4.操作文字对象
# 1）获取大小
w1, h1 = text.get_size()
window.blit(text, (1200-w1, 800-h1))




# ==========================显示图形================================
# 1.画直线
# line(画在哪，线的颜色，线的起点，线的终点，线宽=1)
pygame.draw.line(window, (255, 0, 0), (10, 20), (200, 20))

# 2.画折线
# lines(画在哪，线的颜色，是否闭合,多个点，线宽=1)
points = [(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), False, points, 3)

# 3.画圆
# circle(画在哪，线的颜色，圆心坐标，半径，线宽=0)
pygame.draw.circle(window, (0, 0, 225), (200, 250), 100, 2)

# 4.画矩形
# rect（画在哪，线的颜色，矩形范围(坐标，长，宽)，线宽=0）
pygame.draw.rect(window, (120, 20, 60), (100, 70, 100, 200), 3)

# 5.画椭圆  和矩形参数一样，相当于内切于矩形
pygame.draw.ellipse(window, (255, 0, 0), (100, 70, 100, 200), 3)

# 6.画弧线
# arc(画在哪，线的颜色，矩形范围，起始弧度，终止弧度，线宽=1)
pygame.draw.arc(window, (0, 0, 0), (100, 70, 100, 200), 0, 3.1415926,5)


# ===========按钮===========
# 1.确定按钮
pygame.draw.rect(window,(255,0,0),(30,100,100,50))
text1 = font.render('确定',True,(255,255,255))

# 2.取消按钮
pygame.draw.rect(window,(0,255,0),(100,50,700,800))


# 刷新显示页面
# pygame.display.flip()  第一次刷新/
# pygame.display.updata()   第一次以后刷新
pygame.display.flip()

# 让游戏保持一直运行的状态
# game loop 游戏循环
while True:
    # ==========游戏帧的刷新===========
    #  检测事件
    for event in pygame.event.get():
        # 检测关闭按钮被点击的事件
        if event.type == pygame.QUIT:
            exit()   # 退出的是一个线程
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标摁下
            mx,my = event.pos  # 取出鼠标的坐标
        elif event.type == pygame.MOUSEBUTTONUP:   # 鼠标弹起
            pass
        elif event.type == pygame.MOUSEMOTION:  # 鼠标移动
            pass
        elif event.type == pygame.KEYDOWN:  # 按键被摁下
            x = event.key  #获取被摁下的key的ASCII值
        elif event.type == pygame.KEYUP:  # 按键被弹起
            pass
