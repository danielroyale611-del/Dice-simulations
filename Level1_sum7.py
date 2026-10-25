import random

def simulate_sum_7(trials=100000):
    count = 0
    for _ in range(trials):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if d1 + d2 == 7:
            count += 1
    prob = count / trials
    print(f"Trials: {trials}")
    print(f"Count sum=7: {count}")
    print(f"Estimated probability: {prob:.4f}")
    print(f"Theoretical: {6/36:.4f}")

if __name__ == "__main__":
    simulate_sum_7()
