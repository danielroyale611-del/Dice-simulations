import random

def simulate_two_evens(trials=100000):
    count = 0
    for _ in range(trials):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        if d1 % 2 == 0 and d2 % 2 == 0:
            count += 1
    prob = count / trials
    print(f"Trials: {trials}")
    print(f"Both even: {count}")
    print(f"Estimated: {prob:.4f}, Theoretical: {9/36:.4f}")

if __name__ == "__main__":
    simulate_two_evens()
