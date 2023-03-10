import socket
import time
from math import cos, sin, pi
import pygame


class SocketServer:
    def __init__(self):
        sock = socket.socket()
        sock.bind(('192.168.43.105', 8000))
        sock.listen(1)
        self.conn, address = sock.accept()
        pygame.init()
        self.lcd = pygame.display.set_mode((640, 480))
        pygame.mouse.set_visible(False)
        self.lcd.fill((0, 0, 0))
        pygame.display.update()
        self.max_distance = 0

    def run(self):
        x_set, y_set = [], []
        while True:
            data = self.conn.recv(15)
            data = data.replace(b'\x00', b'')
            data = data.decode(errors="replace")
            if self.filtering(data):
                a, d = data.split("-")
                a, d = float(a), float(d)
                x_set.append(a)
                y_set.append(d)
                if len(x_set) >= 600:
                    self.visualize(x_set, y_set, data)
                    x_set.clear()
                    y_set.clear()
            else:
                continue

    @staticmethod
    def filtering(data):
        try:
            f, s = data.split("-")
            if len(f) == 6 and len(s) == 8:
                pass
            else:
                raise ValueError
            return True
        except ValueError:
            return False

    def visualize(self, aset, dset, data):
        self.lcd.fill((0, 0, 0))
        for a, d in zip(aset, dset):
            if d > 0:
                self.max_distance = max([min([5000, d]), self.max_distance])
                radians = a * pi / 180.0
                x = d * cos(radians)
                y = d * sin(radians)
                if x > 0 and y == 0:
                    print(data)
                point = (320 + int(x / self.max_distance * 119), 240 + int(y / self.max_distance * 119))
                self.lcd.set_at(point, pygame.Color(255, 255, 255))
        pygame.display.update()


server = SocketServer()
server.run()
