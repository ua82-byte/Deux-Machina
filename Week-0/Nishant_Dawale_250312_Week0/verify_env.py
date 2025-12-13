import sys


def main():
    ok = True
    try:
        import gymnasium as gym
        print("gymnasium:", gym.__version__)
    except Exception as e:
        print("gymnasium import error:", type(e).__name__, e)
        ok = False

    try:
        import Box2D
        print("Box2D: present")
    except Exception as e:
        print("Box2D: missing or import error:", type(e).__name__, e)

    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
