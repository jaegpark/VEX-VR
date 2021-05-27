vexcode_brain_precision = 0
myVariable = 0
perimeter = 0
area = 0

def when_started1():
    global myVariable, perimeter, area, vexcode_brain_precision
    perimeter = 0
    pen.move(DOWN)
    for repeat_count in range(4):
        pen.set_pen_color(RED)
        drivetrain.drive_for(FORWARD, 189, MM)
        perimeter = perimeter + 189
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        pen.set_pen_color(GREEN)
        drivetrain.drive_for(FORWARD, 189, MM)
        perimeter = perimeter + 189
        drivetrain.turn_for(LEFT, 90, DEGREES)
        pen.set_pen_color(BLUE)
        drivetrain.drive_for(FORWARD, 189, MM)
        perimeter = perimeter + 189
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)
    area = 0
    area = area + ((perimeter / 120) * (perimeter / 120)) * 5
    brain.print("The area is ")
    brain.print(area, precision=vexcode_brain_precision)
    brain.print(" cm^2")

vr_thread(when_started1())
