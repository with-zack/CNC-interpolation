#从起点(x0,y0)到终点(x1,y1)做直线插补

import math

def dda_line(x0, y0, x1, y1):

    #找出最小的n使2^n >= max(|x1 - x0|,|y1 - y0|)
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

    #向x轴+(-)方向 delta_x = 1 (-1) y轴同理
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

    #'x_now'X积分累加器
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





#从起点(x0,y0)到终点(x1,y1)做圆弧插补

def dda_arc(x0, y0, x1, y1, R_input):
    
    #向x轴+(-)方向 delta_x = 1 (-1) y轴同理
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    if dx == 0:
        delta_x = 0
    else:
        delta_x = (x1-x0)/dx
    if dy == 0:
        delta_y = 0
    else:
        delta_y = (y1-y0)/dy
    
    
    if R_input>0:
        clockwise_anticlockwise_parameter = 1
    else:
        clockwise_anticlockwise_parameter = -1
        
    #通过起终点(x0 , y0)(x1 , y1), 半径R(输入参数传至R)来计算圆心(xc , yc),起终点与水平线夹角为a
    xc = 0
    yc = 0
    R = abs(R_input)
    l = ( (x1 - x0)**2 + (y1 - y0)**2 ) ** 0.5 / 2

    if R < l:
        #报错，不存在这样的轨迹
        return -1
        
    else:
        #判断圆弧所处象限并计算圆心坐标
        if ( delta_x >= 0 and delta_y <= 0 ):
            a = math.atan( ( y0 - y1 ) / ( x1 - x0 ) )
            xc = (x0 + x1) / 2 - ( R**2 - l**2 ) ** 0.5 * math.sin( a ) * clockwise_anticlockwise_parameter
            yc = (y0 + y1) / 2 - ( R**2 - l**2 ) ** 0.5 * math.cos( a ) * clockwise_anticlockwise_parameter
            
        elif( delta_x <= 0 and delta_y <= 0 ):
            a = math.atan( ( y0 - y1 ) / ( x0 - x1 ) )
            xc = (x0 + x1) / 2 - ( R**2 - l**2 ) ** 0.5 * math.sin( a ) * clockwise_anticlockwise_parameter
            yc = (y0 + y1) / 2 + ( R**2 - l**2 ) ** 0.5 * math.cos( a ) * clockwise_anticlockwise_parameter
            
        elif( delta_x <= 0 and delta_y >= 0 ):
            a = math.atan( ( y0 - y1 ) / ( x1 - x0 ) )
            xc = (x0 + x1) / 2 + ( R**2 - l**2 ) ** 0.5 * math.sin( a ) * clockwise_anticlockwise_parameter
            yc = (y0 + y1) / 2 + ( R**2 - l**2 ) ** 0.5 * math.cos( a ) * clockwise_anticlockwise_parameter
            
        elif( delta_x >= 0 and delta_y >= 0 ):
            a = math.atan( ( y0 - y1 ) / ( x0 - x1 ) )
            xc = (x0 + x1) / 2 + ( R**2 - l**2 ) ** 0.5 * math.sin( a ) * clockwise_anticlockwise_parameter
            yc = (y0 + y1) / 2 - ( R**2 - l**2 ) ** 0.5 * math.cos( a ) * clockwise_anticlockwise_parameter
            
    #将圆心(xc , yc)移至原点，将起终点(x0 , y0)(x1 , y1)移至(x0 - xc, y0 - yc)(x1 - xc , y1 - yc)
    x0 = x0 - xc
    y0 = y0 - yc
    x1 = x1 - xc
    y1 = y1 - yc


    #找出最小的n使2^n >= max(|x1 - x0|,|y1 - y0|)
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
    J_vx = x1
    J_vy = y1
    J_rx = 0.0
    J_ry = 0.0

    count_x = dx
    count_y = dy
    x_pulses = []
    y_pulses = []

    


        
    #象限修正参数(圆弧所处象限不同，插补方向不同，故引入参数修正)
    if ( delta_x >= 0 and delta_y >= 0 ) or ( delta_x <= 0 and delta_y <= 0 ):
        quadrant = 1
    else:
        quadrant = -1

        
    #插补开始
    while (count_x > 0 or count_y > 0):
        
        if count_x > 0 and count_y > 0:
            
            #积分运算并判断是否溢出
            J_rx += abs(J_vx)
            
            if J_rx >= m:
                J_rx -= m
                x_pulses.append(1)
                #插补方向与圆弧起终点、顺逆与象限均有关
                J_vy -= delta_x * clockwise_anticlockwise_parameter * quadrant
                count_x -= 1
            else:
                x_pulses.append(0)
                
            J_ry += abs(J_vy)
            
            if J_ry >= m:
                J_ry -= m
                y_pulses.append(1)
                J_vx -= delta_y * clockwise_anticlockwise_parameter * quadrant
                count_y -= 1
            else:
                y_pulses.append(0)
                
        if count_y > 0 and count_x == 0:
            J_ry += abs(J_vy)
            
            if J_ry >= m:
                J_ry -= m
                y_pulses.append(1)
                J_vx -= delta_y * clockwise_anticlockwise_parameter * quadrant
                count_y -= 1
            else:
                y_pulses.append(0)
            x_pulses.append(0)
            
        if count_x >0 and count_y == 0:
            J_rx += abs(J_vx)
            
            if J_rx >= m:
                J_rx -= m
                x_pulses.append(1)
                J_vy -= delta_x * clockwise_anticlockwise_parameter * quadrant
                count_x -= 1
            else:
                x_pulses.append(0)
                
            y_pulses.append(0)

    #将圆心移回(xc , yc)，将起终点从(x0 - xc, y0 - yc)移回(x1 - xc , y1 - yc)(x0 , y0)(x1 , y1)
    x0 = x0 + xc
    y0 = y0 + yc
    x1 = x1 + xc
    y1 = y1 + yc
    
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
