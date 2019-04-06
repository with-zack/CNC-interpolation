def dda_line(x0, y0, x1, y1):
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    if dy >= dx:
        temp = dy
    else:
        temp = dx
    n = 1 
    while 2**n < temp:
        n += 1
    x_pulses = []
    y_pulses = []
    m = 2**n
    if dx == 0:
        delta_x = 0
    else:
        delta_x = (x1-x0)/dx
    if dy == 0:
        delta_y = 0
    else:
        delta_y = (y1-y0)/dy
    count = 0
    x_now = 0                                                                                                                                                       
    y_now = 0
    while count < m:
        x_now += dx
        if x_now >= m:
            x_pulses.append(1)  # 记录溢出脉冲为1
            x_now -= m
        else:
            x_pulses.append(0)
        y_now += dy
        if y_now >= m:
            y_pulses.append(1)  # 记录溢出脉冲为1
            y_now -= m
        else:
            y_pulses.append(0)
        count += 1

    # 每一步的坐标值
    x_coordinates = [x0]
    y_coordinates = [y0]
    for pulse in x_pulses:
        if pulse == 1:
            x_coordinates.append(x_coordinates[-1]+delta_x)

        else:
            x_coordinates.append(x_coordinates[-1])

    for pulse in y_pulses:
        if pulse == 1:
            y_coordinates.append(y_coordinates[-1] + delta_y)
        else:
            y_coordinates.append(y_coordinates[-1])

    # 输出计算过程

    output_string = "计算过程：\n"
    return x_coordinates, y_coordinates, output_string, m


def dda_arc(x0, y0, x1, y1):
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    if dy >= dx:
        temp = dy
    else:
        temp = dx
    n = 1 
    while 2**n < temp:
        n += 1
    m = 2**n
    J_vx = y0
    J_vy = x0
    J_rx = 0.0
    J_ry = 0.0
    if dx == 0:
        delta_x = 0
    else:
        delta_x = (x1-x0)/dx
    if dy == 0:
        delta_y = 0
    else:
        delta_y = (y1-y0)/dy
    count_x = dx
    count_y = dy
    x_pulses = []
    y_pulses = []
    while (count_x > 0 or count_y > 0):
        if count_x > 0 and count_y > 0:
            J_rx += J_vx
            if J_rx >= m:
                J_rx -= m
                x_pulses.append(1)
                J_vy += delta_x
                count_x -= 1
            else:
                x_pulses.append(0)
            J_ry += J_vy
            if J_ry >= m:
                J_ry -= m
                y_pulses.append(1)
                J_vx += delta_y
                count_y -= 1
            else:
                y_pulses.append(0)
        if count_y > 0 and count_x == 0:
            J_ry += J_vy
            if J_ry >= m:
                J_ry -= m
                y_pulses.append(1)
                J_vx += delta_y
                count_y -= 1
            else:
                y_pulses.append(0)
            x_pulses.append(0)
        if count_x >0 and count_y == 0:
            J_rx += J_vx
            if J_rx >= m:
                J_rx -= m
                x_pulses.append(1)
                J_vy += delta_x
                count_x -= 1
            else:
                x_pulses.append(0)
            y_pulses.append(0)
    x_coordinates = [x0]
    y_coordinates = [y0]
    for pulse in x_pulses:
        if pulse == 1:
            x_coordinates.append(x_coordinates[-1]+delta_x)

        else:
            x_coordinates.append(x_coordinates[-1])

    for pulse in y_pulses:
        if pulse == 1:
            y_coordinates.append(y_coordinates[-1] + delta_y)
        else:
            y_coordinates.append(y_coordinates[-1])
    output_string = "计算过程：\n"
    return x_coordinates, y_coordinates, output_string, m