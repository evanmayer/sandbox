# Raise a simple exception for inspection.

# What line is it on? What does it mean? Is it fixable?

def main():
    res = []
    for exp in [-520, -100, 0, 100, 520]:
        val = float(10 ** exp)
        res.append(val)
    return res

if __name__ == '__main__':
    res = main()
    print(res)