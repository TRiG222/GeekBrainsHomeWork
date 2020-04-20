from time import sleep


class TrafficLight:
    __color = ['\033[31mКрасный', '\033[33mЖелтый', '\033[32mЗеленый', '\033[33mЖелтый']

    def running(self):
        i = 0
        while True:
            if i >= 4:
                i = 0

            print(f'Светофор переключается \n{TrafficLight.__color[i]}')
            if i == 0:
                i += 1
                sleep(7)
            elif i == 1 or i == 3:
                sleep(2)
                i += 1
            elif i == 2:
                sleep(5)
                i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
