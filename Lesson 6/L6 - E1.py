from time import sleep

class TrafficLight:
    # atr
    __color = ['Red', 'Yellow', 'Green', 'Yellow', 'Red']
    
    # methods
    def running(self):
        col = TrafficLight.__color
        for i in range(len(col)):
            print(f'Color is changing: {TrafficLight.__color[i]}')
            if i == 0 or i == 2:
                sleep(7)
            else:
                sleep(3)

traffic = TrafficLight()
traffic.running()
