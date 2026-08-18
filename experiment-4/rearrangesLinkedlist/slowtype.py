import sys, time

def slowtype(stn):
    for ch in stn:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


if __name__ == "__main__":
    slowtype(" Hello From Anu ")