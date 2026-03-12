# fractal_math.py - v2.0
def calculate_basic_fractal():
    print("初始化分形计算模型...")
    return True

# 新增的功能：计算分形维数
def calculate_fractal_dimension(n, r):
    import math
    return math.log(n) / math.log(1/r)

if __name__ == "__main__":
    calculate_basic_fractal()
    dim = calculate_fractal_dimension(4, 0.333)
    print(f"该几何体的分形维数为: {dim}")