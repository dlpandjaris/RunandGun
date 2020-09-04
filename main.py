import pyautogui as py
import time

py.moveTo(470, 750)
py.rightClick()
time.sleep(0.5)

py.moveTo(460, 560)
py.click()

time.sleep(2)
py.moveTo(400, 50)
py.click()
py.typewrite('https://www.learn4good.com/games/sports/runandgun.htm')
py.press('enter')

py.moveRel(0, 100)
time.sleep(2)
py.scroll(-1200)

py.moveTo(815, 350)
py.click()

py.moveTo(1105, 180)
py.click()

time.sleep(3)

py.moveTo(810, 520)
py.click()

py.moveRel(0, 20)
time.sleep(1)
for i in range(5):
    py.click()

time.sleep(3)
py.press('left')
py.press('enter')

#88, 76
empty = py.pixel(706, 541)
me = py.pixel(709, 466)
white = (255, 255, 255)

for i in [4, 3, 2]:
    for j in range(7):
        current = py.pixel(475 + 88 * j, 540 - 76 * i)
        if current != empty:
            if current != me:
                if current != white:
                    defense = current
                    break
print(defense)

while py.pixel(800, 555) != (187, 187, 188):
    py.press('left')
    py.press('enter')
    loc = 3
    while py.pixel(523, 364) != (255, 204, 0):
        grid = []
        first = py.pixel(475, 540)
        for i in range(6):
            gridi = []
            for j in range(7):
                current = py.pixel(475 + 88 * j, 540 - 76 * i)
                print(current)
                if current == defense:
                    gridi.append(-1)
                elif current == me:
                    gridi.append(0)
                else:
                    gridi.append(1)
            grid.append(gridi)
        #py.screenshot(r"C:\Users\Dylan Pandjaris\Documents\Code\Selenium\image.png")
        print(grid)
        #break
        if grid[3][loc] == 1:
            py.press('up')
            if grid[2][loc] == 1:
                py.press('up')
                if grid[1][loc] == 1:
                    py.press('up')
                    if grid[0][loc] == 1:
                        py.press('up')
        elif grid[4][loc - 1] == 1:
            py.press('left')
            loc -=1
        elif grid[4][loc + 1] == 1:
            py.press('right')
            loc += 1
        #break
    time.sleep(5)


