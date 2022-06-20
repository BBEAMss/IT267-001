from measure import Measure 

"""if __name__ == '__main__':
    m1 = Measure(56)
    m2 = Measure(78)
    m3 = Measure(14)
    m4 = Measure(250)
    print(m1.inch_cm())
    print(m2.inch_cm())
    print(m3.cm_inch())
    print(m4.cm_inch())"""

"""inch_lish = [52,18,20,40]
for item in inch_lish:
     m = Measure(item)
     print(m.inch_cm())"""

num = float(input("Enter number: "))
ch = input("Choose I(inch->cm), C(cm->inch):").upper()
m = Measure(num)
if ch == 'I':
    print(m.inch_cm())
elif ch == 'C':
    print(m.cm_inch())
else:
    print("Wrong Character")
