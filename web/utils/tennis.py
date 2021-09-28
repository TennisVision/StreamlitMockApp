import numpy as np

def as_point(obj):
    if isinstance(obj, Point):
        return obj
    return Point(obj[0], obj[1])

class Point:
    def __init__(self, x:float, y:float, z=None, name=None):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
    
    def __repr__(self):
        if self.name is None:
            return 'None: Point({}, {})'.format(self.x, self.y)
        return '{}: Point({}, {})'.format(self.name, self.x, self.y)

    def __add__(self, p):
        p = as_point(p)
        x = self.x + p.x
        y = self.y + p.y
        return Point(x, y, name=self.name)
    
    def __radd__(self, p):
        self.__add__(p)

    def __mul__(self, p):
        p = as_point(p)
        x = self.x * p.x
        y = self.y * p.y
        return Point(x, y, name=self.name)
    
    def __rmul__(self, p):
        self.__mul__(p)

    def __truediv__(self, p):
        p = as_point(p)
        x = self.x / p.x
        y = self.y / p.y
        return Point(x, y, name=self.name)
    
    @property
    def tuple(self):
        return (self.x, self.y)
    
    @property
    def nparray(self):
        return np.array([self.x, self.y])
    
    def isInArea(self, Box):
        ret = False
        if self.x >= Box.x1 and self.x <= Box.x2 \
           and \
           self.y >= Box.y1 and self.y <= Box.y2:
            ret = True
        return ret


class Line:
    def __init__(self, p1:Point, p2:Point, name=None):
        self.p1 = p1
        self.p2 = p2
        self.name = None
    
    def __repr__(self):
        if self.name is None:
            return 'None: Line({}, {})'.format(self.p1, self.p2)
        return '{}: Line({}, {})'.format(self.name, self.p1, self.p2)

    def __add__(self, p):
        p = as_point(p)
        p1 = self.p1 + p
        p2 = self.p2 + p
        return Line(p1, p2, name=self.name)
    
    def __radd__(self, p):
        self.__add__(p)

    def __mul__(self, p):
        p = as_point(p)
        p1 = self.p1 * p
        p2 = self.p2 * p
        return Line(p1, p2, name=self.name)
    
    def __rmul__(self, p):
        self.__mul__(p)

    def __truediv__(self, p):
        p = as_point(p)
        p1 = self.p1/p
        p2 = self.p2/p
        return Line(p1, p2, name=self.name)
    
    @property
    def length(self):
        u = self.p1.nparray - self.p2.nparray
        return np.linalg.norm(u)
    
    @property
    def is_vertical(self):
        if self.p1.x == self.p2.x:
            return True
        return False
    
    @property
    def is_horizontal(self):
        if self.p1.y == self.p2.y:
            return True
        return False            
    
    def internal_division(self, m, n):
        # 線分p1-p2をm:nに内分する点
        return (n*self.p1+m*self.p2)/(m+n)

    def n_division_points(self, n):
        # 線分をn等分割する点
        points = []
        diff_x = (self.p2.x - self.p1.x)/n
        diff_y = (self.p2.y - self.p1.y)/n
        for i in range(1, n):
            # n分割 -> n-1個の内分点
            x = self.p1.x + diff_x*i
            y = self.p1.y + diff_y*i
            points.append(Point(x, y))
        return points

class Box:
    def __init__(self, center:Point, width:float, height:float, name=None):
        self.center = center
        self.width = width
        self.height = height
    
    def __repr__(self):
        if self.name is None:
            return 'None: Box({}, {})'.format(self.x, self.y)
        return '{}: Box({}, {})'.format(self.name, self.x, self.y)

    def __add__(self, p):
        p = as_point(p)
        center = self.center + p
        return Box(center, self.width, self.height, name=self.name)
    
    def __radd__(self, p):
        self.__add__(p)

    def __mul__(self, p):
        p = as_point(p)
        width = self.width * p.x
        height = self.height * p.y
        return Box(self.center, width, height, name=self.name)
    
    def __rmul__(self, p):
        self.__mul__(p)

    def __truediv__(self, p):
        p = as_point(p)
        self.width = self.width / p.x
        self.height = self.height / p.y
        return Box(self.center, width, height, name=self.name)
    
    @property
    def x1(self):
        return self.center.x - self.width/2
    
    @property
    def x2(self):
        return self.center.x + self.width/2
    
    @property
    def y1(self):
        return self.center.y - self.height/2
    
    @property
    def y2(self):
        return self.center.y + self.height/2
    
    @property
    def nl(self):
        # Near Left
        return Point(self.x1, self.y1)
    
    @property
    def nr(self):
        # Near Right
        return Point(self.x2, self.y1)
    
    @property
    def fl(self):
        # Far Left
        return Point(self.x1, self.y2)
    
    @property
    def fr(self):
        # Far Right
        return Point(self.x2, self.y2)
    
    @property
    def farLine(self):
        return Line(self.fl, self.fr)
    
    @property
    def nearLine(self):
        return Line(self.nl, self.nr)
    
    @property
    def leftLine(self):
        return Line(self.fl, self.nl)
    
    @property
    def rightLine(self):
        return Line(self.fr, self.nr)
    
    def gridLines(self, m, n):
        lines = []
        # 縦にm分割するグリッド
        m_points_1 = self.farLine.n_division_points(m)
        m_points_2 = self.nearLine.n_division_points(m)
        for i, j in zip(m_points_1, m_points_2):
            lines.append(Line(i, j))
        # 横にn分割するグリッド
        n_points_1 = self.leftLine.n_division_points(n)
        n_points_2 = self.rightLine.n_division_points(n)
        for i, j in zip(n_points_1, n_points_2):
            lines.append(Line(i, j))
        return lines


class Court:
    width = 8.23 # シングルコートの横幅
    alley = 1.37 # アレー１個の横幅
    height = 23.77 # コートの縦幅
    sheight = 12.8 # Service Boxの縦幅(一面分, 半面分にするなら２で割る)

    def __init__(self):
        self.singlesBox     = Box(Point(0,0), width=self.width, height=self.height, name="SinglesBox")
        self.doublesBox     = Box(Point(0,0), width=self.width+2*self.alley, height=self.height, name="DoublesBox")
        self.serviceBox     = Box(Point(0,0), width=self.width, height=self.sheight, name="ServiceBox")

        self.centerLine     = Line(
            Point(0, -self.sheight/2),
            Point(0, self.sheight/2),
            name="CenterLine"
        )
        self.netLine        = Line(
            Point(-self.width/2-self.alley, 0),
            Point(self.width/2+self.alley, 0),
            name="NetLine"
        )

    @property
    def boxes(self):
        return [self.singlesBox, self.doublesBox, self.serviceBox]
    
    @property
    def lines(self):
        return [self.centerLine, self.netLine]


class Ball(Point):
    def __init__(self, x, y, stroke, spin, speed, result, hitpoint=None):
        super().__init__(x, y)
        self.stroke = stroke
        self.spin = spin
        self.speed = speed
        self.result = result
        self.hitpoint = hitpoint


from enum import Enum
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import plotly.graph_objects as go


class Drawer:
    def __init__(self, figsize=(3, 7)):
        self.fig, self.ax = plt.subplots(figsize=figsize)
    
    def show(self):
        # self.fig.show()
        plt.show()
    
    def save_fig(self, save_path):
        self.fig.savefig(save_path)

    def clear(self):
        self.ax.clear()
        self.fig.clear()
    
    def close(self):
        plt.close()
    
    def restart(self, figsize=(3, 7)):
        self.fig, self.ax = plt.subplots(figsize=figsize)
    
    def draw_point(self, point, radius=0.2, facecolor='k', edgecolor='k', fill=True, alpha=1):
        patch = patches.Circle(
            xy=(point.x, point.y), radius=radius,
            facecolor=facecolor, edgecolor=edgecolor, fill=fill
        )
        patch.set_alpha(alpha)
        self.ax.add_patch(patch)

    def draw_box(self, box, color="k", linewidth=1.0, alpha=1):
        patch = patches.Rectangle(
            xy = box.nl.tuple,
            width = box.width,
            height = box.height,
            fill=False,
            color=color,
            linewidth=linewidth
        )
        patch.set_alpha(alpha)
        self.ax.add_patch(patch)
    
    def draw_line(self, line, color="k", linestyle="solid", linewidth=1.0, alpha=1):
        # linestyles: solid, dashed
        if line.is_horizontal:
            y = line.p1.y
            xmin = min(line.p1.x, line.p2.x)
            xmax = max(line.p1.x, line.p2.x)
            self.ax.hlines(y=y, xmin=xmin, xmax=xmax, colors=color, linestyles=linestyle, linewidth=linewidth, alpha=alpha)
        elif line.is_vertical:
            x = line.p1.x
            ymin = min(line.p1.y, line.p2.y)
            ymax = max(line.p1.y, line.p2.y)
            self.ax.vlines(x=x, ymin=ymin, ymax=ymax, colors=color, linestyles=linestyle, linewidth=linewidth, alpha=alpha)
        else:
            x = np.linspace(line.p1.x, line.p2.x, 1000)
            def f(x):
                # y = (y2-y1)/(x2-x1)(x-x1)+y1
                u = (line.p2.y-line.p1.y)/(line.p2.x-line.p1.x)
                return u*(x-line.p1.x) + line.p1.y
            self.ax.plot(x, f(x), color=color, linestyle=linestyle, linewidth=linewidth, alpha=alpha)

    def draw_text(self, point, text, color="k", size=10, fontweight="bold", horizontalalignment="center"):
        x = point.x
        y = point.y
        self.ax.text(x, y, text, color=color, size=size, fontweight=fontweight, horizontalalignment=horizontalalignment)

    def draw_arrow(self, p1, p2, facecolor="gray", edgecolor="gray", fill=True, alpha=0.7):
        self.ax.annotate(
            '',
            xytext=p1.tuple, # 始点
            xy=p2.tuple, # 終点
            arrowprops=dict(
                shrink=0, width=1, headwidth=8, headlength=10,
                connectionstyle='arc3',facecolor=facecolor, edgecolor=edgecolor, fill=fill, alpha=alpha
            )
        )

class CourtDrawer(Drawer):
    def __init__(self, figsize):
        super().__init__(figsize=figsize)
        self.ax.axis("off")
    
    def draw_court(self, court, color="k", linewidth=3.0, alpha=1.0):
        for box in court.boxes:
            self.draw_box(box, color=color, linewidth=linewidth, alpha=alpha)
        for line in court.lines:
            self.draw_line(line, color=color, linewidth=linewidth, alpha=alpha)

    def draw_balls(self, balls, colorEnum=None):
        for ball in balls:
            if colorEnum:
                color = getattr(colorEnum, ball.stroke.replace(' ', '')).value
            else:
                color = "#00ff00"
            ball.y = abs(ball.y)
            if ball.result=='Net':
                ball.y = 0
            fill = True if ball.result=='In' else False
            alpha = 0.5  if fill else 1
            self.draw_point(ball, facecolor=color, edgecolor=color, fill=fill, alpha=alpha)
    
    def draw_serves(self, balls, colorEnum=None):
        for ball in balls:
            if colorEnum:
                color = getattr(colorEnum, ball.stroke.replace(' ', '').replace('1st', "First").replace("2nd", "Second")).value
            else:
                color = "#00ff00"
            
            ball.y = abs(ball.y)
            if ball.result=='Net':
                ball.y = 0
            
            fill = True if ball.result=='In' else False
            alpha = 0.5  if fill else 1
            self.draw_point(ball, facecolor=color, edgecolor=color, fill=fill, alpha=alpha)
    
    def draw_hitpoints(self, balls, colorEnum=None):
        for ball in balls:
            if colorEnum:
                color = getattr(colorEnum, ball.stroke.replace(' ', '')).value
            else:
                color = "#00ff00"
            if ball.hitpoint.y > 0:
                # 点対称
                ball.hitpoint.x = -ball.hitpoint.x
                ball.hitpoint.y = -ball.hitpoint.y
            fill = True if ball.result=='In' else False
            alpha = 0.5  if fill else 1
            self.draw_point(ball.hitpoint, facecolor=color, edgecolor=color, fill=fill, alpha=alpha)
    
    def draw_directions(self, balls, colorEnum=None):
        """
        打点から落下点までの矢印を描く
        """
        for ball in balls:
            if colorEnum:
                color = getattr(colorEnum, ball.stroke.replace(' ', '')).value
            else:
                color = "#00ff00"
            if ball.result=='Net':
                ball.y = 0
            if ball.hitpoint.y > 0:
                # コート手前から奥に矢印を書く
                ball.x = -ball.x
                ball.y = -ball.y
                ball.hitpoint.x = -ball.hitpoint.x
                ball.hitpoint.y = -ball.hitpoint.y
            fill = True if ball.result=='In' else False
            self.draw_arrow(ball.hitpoint, ball, facecolor=color, edgecolor=color, fill=fill)
            
        

    def draw_legends(self, colorEnum):
        legend_elements = [
            patches.Patch(facecolor=e.value, edgecolor="k", label=e.name)
            for e in colorEnum
        ]
        self.ax.legend(
            handles=legend_elements, bbox_to_anchor=(0.5, 1.08),
            loc='center', borderaxespad=0, fontsize=10, ncol=2
        )
    
    def draw_grid(self, box, m, n):
        """
        Box内にグリッド線を描画, 縦にm分割, 横にn分割
        """
        grids = box.gridLines(m, n)
        for line in grids:
            self.draw_line(line, linestyle="dashed")
    
    def draw_percent(self, box, m=3, n=3, xpercents=[], ypercents=[], size=7):
        # 内分点の中点に描画するのでmを2倍してる
        points = box.farLine.n_division_points(m*2)
        for point, percent in zip(points[::2], xpercents):
            text = str(percent) + "%"
            self.draw_text(point+(0, 0.5), text, size=size)
        
        points = box.leftLine.n_division_points(n*2)
        for point, percent in zip(points[::2], ypercents):
            text = str(percent) + "%"
            self.draw_text(point+(-2.5, 0), text, size=size)