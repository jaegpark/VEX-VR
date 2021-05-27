myVariable = 0
curDist = 0

def gG1():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > -105:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(GREEN):
        wait(5, MSEC)
    drivetrain.stop()
    magnet.energize(BOOST)

def gB1():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > -105:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(BLUE):
        wait(5, MSEC)
    drivetrain.stop()
    magnet.energize(BOOST)

def gR1():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > -100:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) < -495:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.stop()
    magnet.energize(BOOST)

def gB2():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 95:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(BLUE):
        wait(5, MSEC)
    drivetrain.stop()
    magnet.energize(BOOST)

def gG2():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 95:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) < -290:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(GREEN):
        wait(5, MSEC)
    drivetrain.stop()
    magnet.energize(BOOST)

def gR2():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 95:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) > 290:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(RED):
        wait(5, MSEC)
    drivetrain.stop()
    magnet.energize(BOOST)

def dG1():
    global myVariable, curDist
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) < 5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -790:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(DROP)
    drivetrain.drive_for(REVERSE, 800, MM)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.stop()

def dB1():
    global myVariable, curDist
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) > -5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -795:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(DROP)
    drivetrain.drive_for(REVERSE, 800, MM)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.stop()

def dB2():
    global myVariable, curDist
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) < 5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -790:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(DROP)
    drivetrain.drive_for(REVERSE, 800, MM)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.stop()

def dR1():
    global myVariable, curDist
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < 0:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) > -5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -795:
        wait(5, MSEC)
    magnet.energize(DROP)
    drivetrain.stop()

def dG2():
    global myVariable, curDist
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < 100:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) > -5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -795:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    magnet.energize(DROP)
    drivetrain.drive_for(REVERSE, 800, MM)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.stop()

def dR2():
    global myVariable, curDist
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < 100:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) < 5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -795:
        wait(5, MSEC)
    magnet.energize(DROP)
    drivetrain.stop()

def pickRedBlue():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 50:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) > 495:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not (down_eye.detect(BLUE) or down_eye.detect(RED)):
        wait(5, MSEC)
    magnet.energize(BOOST)
    drivetrain.stop()
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < 50:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) < 5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -400:
        wait(5, MSEC)

def dropOff():
    global myVariable, curDist
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not left_bumper.pressed():
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not left_bumper.pressed():
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) < 5:
        wait(5, MSEC)
    magnet.energize(DROP)
    drivetrain.drive(FORWARD)
    while not left_bumper.pressed():
        wait(5, MSEC)
    drivetrain.turn_to_heading(180, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) < -400:
        wait(5, MSEC)
    drivetrain.turn_to_heading(90, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) > -5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.stop()

def pickGreen():
    global myVariable, curDist
    drivetrain.drive(FORWARD)
    while not location.position(Y, MM) > 50:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(FORWARD)
    while not location.position(X, MM) < -495:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(FORWARD)
    while not down_eye.detect(GREEN):
        wait(5, MSEC)
    magnet.energize(BOOST)
    drivetrain.stop()
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < 50:
        wait(5, MSEC)
    drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(X, MM) > 5:
        wait(5, MSEC)
    drivetrain.turn_to_heading(0, DEGREES)
    drivetrain.drive(REVERSE)
    while not location.position(Y, MM) < -400:
        wait(5, MSEC)

def when_started1():
    global myVariable, curDist
    for repeat_count in range(2):
        gG1()
        dG1()
        wait(5, MSEC)
    for repeat_count2 in range(2):
        gB1()
        dB1()
        wait(5, MSEC)
    for repeat_count3 in range(2):
        gR1()
        dR1()
        wait(5, MSEC)
    # picks up last remaining blocks for each colour
    gB2()
    dB2()
    gG2()
    dG2()
    gR2()
    dR2()
    # hide remaining blocks
    for repeat_count4 in range(2):
        pickRedBlue()
        dropOff()
        wait(5, MSEC)
    pickGreen()
    dropOff()

vr_thread(when_started1())
