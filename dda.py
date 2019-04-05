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
    delta_x = (x1-x0)/m
    delta_y = (y1-y0)/m
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
            x_coordinates.append(x_coordinates[-1]+delta_x/abs(delta_x))

        else:
            x_coordinates.append(x_coordinates[-1])

    for pulse in y_pulses:
        if pulse == 1:
            y_coordinates.append(y_coordinates[-1] + delta_y/abs(delta_y))
        else:
            y_coordinates.append(y_coordinates[-1])

    # 输出计算过程

    output_string = "计算过程：\n"
    return x_coordinates, y_coordinates, output_string, m
