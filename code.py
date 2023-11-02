from adafruit_motor import motor

left_motor_forward = board.GP15
left_motor_backward = board.GP14
right_motor_forward = board.GP12
right_motor_backward = board.GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000)
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000)


Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0

Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
Right_Motor_speed = 0

    def forward():
    Right_Motor_speed = .5
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(0)
    Left_Motor_speed = .5
    Left_Motor.throttle = Left_Motor_speed

    def backward():
    Right_Motor_speed = -0.5
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(0)
    Left_Motor_speed = -0.5
    Left_Motor.throttle = Left_Motor_speed

    def left():
    Right_Motor_speed = .5
    Right_Motor.throttle = Right_Motor_speed



    def right():
    Left_Motor_speed = 0.5
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed


    def stop():
    Right_Motor_speed =0
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(0)
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed

    while True:
    #forward
    Right_Motor_speed = .5
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(0)
    Left_Motor_speed = .5
    Left_Motor.throttle = Left_Motor_speed

    #right
    Left_Motor_speed = 0.5
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed
