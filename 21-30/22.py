import turtle as t
nums = [6, 4, 10]

t.pensize(3)
t.penup()
t.goto(-300, 0)

for num in nums:
    t.pendown()

    for i in range(num):
        for j in range(4):
            t.fd(50)
            t.lt(90)

        t.lt(360/num)

    t.penup()
    t.fd(300)
