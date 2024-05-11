def setup():
    size(480, 480)
    noFill()

def m(a, b):
    return (a[0]-b[0])/(a[1]-b[1])

def v(a, b):
    return (a[0]**2 - b[0]**2 + a[1]**2 - b[1]**2) / (2*a[1] - 2*b[1])

def cir(a, b, c):
    # Center of circle on three points lies where two lines intersect,
    # the line perpendicular to AB and the line perpendicular to BC
    x_a, y_a = a

    # Rise/run of both lines
    m_ab = m(a,b)
    m_bc = m(b,c)

    # y-intercept of both lines
    v_ab = v(a,b)
    v_bc = v(b,c)

    # Set both lines equal to each other, solve for x
    x_p = (v_bc - v_ab) / (m_bc - m_ab)
    
    # y = xm + v (both ab and bc work)
    y_p = -x_p * m_ab + v_ab

    # radius of circle
    r = ((x_a - x_p)**2 + (y_a - y_p)**2)**(0.5)

    return x_p, y_p, r

points = set()

def mouseClicked():
    x,y = float(mouseX), float(mouseY)
    points.add((x,y))
    circle(x, y, 10)

def draw():
    if len(points) == 3:
        a, b, c = list(points)
        print('points:', a, b, c)
        x_p, y_p, r = cir(a,b,c)
        print(x_p, y_p, r)
        circle(x_p, y_p, 2*r)
        points.clear()
