current_weight = float(input("请输入您当前的体重（kg）:"))

yearly_gain = 0.5
moon_gravity_ratio = 0.165

print("\n年份\t地球体重(kg)\t月球体重(kg)")
print("----------------------------------------")

for year in range(11):
    earth_weight = current_weight + (year * yearly_gain)
    moon_weight = earth_weight * moon_gravity_ratio
    
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
