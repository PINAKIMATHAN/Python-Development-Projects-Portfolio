import pygame
from datetime import datetime
 
pygame.init()
 
screen = pygame.display.set_mode((470,180))
pygame.display.set_caption('Digital Clock')
 
 
smallFont = pygame.font.SysFont('DS-Digital',30)
bigFont = pygame.font.SysFont('DS-Digital',135)
 
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
 
days = ['Monday,', 'Tuesday,', 'Wednesday,' ,'Thursday,', 'Friday,', 'Saturday,', 'Sunday,']
months = ['January /', 'February /', 'March /', 'April /', 'May /', 'June /', 'July /', 'August /','September /', 'October /', 'November /', 'December /']
 
 
running = True
 
while running:
    screen.fill(green) 
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
 
 
    time_now = datetime.now()
    today = datetime.today()
 
    minute = time_now.strftime('%M:%S')
    hour = int(time_now.strftime('%H'))
 
    year = time_now.strftime("%d / %Y")
    month = int(time_now.strftime('%m'))
    day = today.weekday()
    day = days[day]
    month = months[month-1]
 
    am = 'AM'
    if hour > 12:
        hour = hour - 12
        am = 'PM'
 
    time = f'{hour}:{minute}'
 
    time_text = bigFont.render(time, True, blue)
    month_text = smallFont.render(month, True, red)
    year_text = smallFont.render(year, True, red)
    am_text = smallFont.render(am, True, blue)
    day_text = smallFont.render(day, True, red)
 
    screen.blit(time_text, (15,15))
    screen.blit(month_text, (150, 142))
    screen.blit(year_text, (260, 142))
    screen.blit(am_text, (380, 5))
    screen.blit(day_text, (30, 142))
 
    pygame.display.update()
