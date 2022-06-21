from empit import EmpIT
from emmkt import EmpMKT

#creat object employee IT
mike = EmpIT("001","MIke",60000)
mike.add_skill("Python , JavaSrcipt")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#creat object employee MKT
anna = EmpMKT("002","Anna",35000)
anna.emp_detail()
anna.mkt_salary()

#พนักงานแผนการตลาดชื่อ Paul มีเงินเดือน 45000 ได้รับคอมมิชชัน 35% โดยทำงานอยู่จังหวัดเชียงใหม่
paul = EmpMKT("003","Paul",45000)
paul.add_commission(35)
paul.add_location("Chaing Mai")
paul.emp_detail()
paul.mkt_salary()