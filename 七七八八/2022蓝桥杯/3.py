import pygame
import random

# 初始化Pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 设置屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("打砖块游戏")

# 设置时钟
clock = pygame.time.Clock()

# 玩家板参数
paddle_width = 100
paddle_height = 10
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - paddle_height - 30
paddle_speed = 7

# 球参数
ball_size = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 * random.choice((1, -1))

# 砖块参数
brick_rows = 5
brick_cols = 10
brick_width = SCREEN_WIDTH // brick_cols
brick_height = 20
brick_padding = 5
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        bricks.append(pygame.Rect(col * (brick_width + brick_padding) + brick_padding,
                                  row * (brick_height + brick_padding) + brick_padding,
                                  brick_width, brick_height))

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x - paddle_speed >= 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x + paddle_speed <= SCREEN_WIDTH - paddle_width:
        paddle_x += paddle_speed

    # 更新球的位置
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 球碰到墙壁的反弹效果
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 球碰到板的反弹效果
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
        ball_speed_y = -ball_speed_y

    # 球掉出屏幕底部，游戏结束
    if ball_y >= SCREEN_HEIGHT:
        running = False

    # 球碰到砖块的反弹效果
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
    for brick in bricks:
        if brick.colliderect(ball_rect):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            break

    # 绘制屏幕
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle_rect)
    pygame.draw.ellipse(screen, WHITE, ball_rect)

    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出Pygame
pygame.quit()