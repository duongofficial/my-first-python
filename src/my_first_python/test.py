import pygame
import sys

# ---------------- Cấu hình ----------------
PASSWORD_DUNG = "hello"   # Mật khẩu đúng (đúng 5 chữ cái) - đổi tùy ý
DO_DAI = 5                # Mật khẩu chỉ được 5 chữ
W, H = 500, 320

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Nhập mật khẩu")
clock = pygame.time.Clock()

font_title = pygame.font.SysFont("arial", 30, bold=True)
font_input = pygame.font.SysFont("arial", 36)
font_small = pygame.font.SysFont("arial", 18)

BG = (30, 33, 46)
BOX = (50, 55, 75)
ACTIVE = (90, 140, 255)
WHITE = (240, 240, 245)
GREY = (150, 155, 175)
RED = (240, 90, 90)
GREEN = (90, 210, 130)

text = ""
show = False
message = ""
msg_color = WHITE
success = False

box = pygame.Rect(0, 0, 320, 60)
box.center = (W // 2, 150)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN and not success:
            if e.key == pygame.K_BACKSPACE:
                text = text[:-1]
                message = ""
            elif e.key == pygame.K_TAB:
                show = not show
            elif e.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if len(text) < DO_DAI:
                    message, msg_color = f"Cần đủ {DO_DAI} chữ cái!", RED
                elif text == PASSWORD_DUNG:
                    message, msg_color = "Đăng nhập thành công!", GREEN
                    success = True
                else:
                    message, msg_color = "Sai mật khẩu, thử lại.", RED
                    text = ""
            elif e.unicode and e.unicode.isalpha():
                if len(text) < DO_DAI:
                    text += e.unicode
                    message = ""
                else:
                    message, msg_color = f"Tối đa {DO_DAI} chữ cái!", RED

    screen.fill(BG)
    t = font_title.render("Nhập mật khẩu", True, WHITE)
    screen.blit(t, t.get_rect(center=(W // 2, 70)))

    pygame.draw.rect(screen, BOX, box, border_radius=10)
    pygame.draw.rect(screen, GREEN if success else ACTIVE, box, 3, border_radius=10)

    hien_thi = text if show else "*" * len(text)
    # con trỏ nhấp nháy
    if not success and (pygame.time.get_ticks() // 500) % 2 == 0:
        hien_thi += "|"
    s = font_input.render(hien_thi, True, WHITE)
    screen.blit(s, s.get_rect(midleft=(box.x + 15, box.centery)))

    d = font_small.render(f"{len(text)}/{DO_DAI} chữ cái", True, GREY)
    screen.blit(d, d.get_rect(midright=(box.right, box.bottom + 20)))

    if message:
        m = font_small.render(message, True, msg_color)
        screen.blit(m, m.get_rect(center=(W // 2, 235)))

    g = font_small.render("Enter: xác nhận  |  Backspace: xóa  |  Tab: hiện/ẩn", True, GREY)
    screen.blit(g, g.get_rect(center=(W // 2, 290)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()