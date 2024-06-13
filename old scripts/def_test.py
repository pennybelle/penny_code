# delay function is partially working, it sets the delay but doesn't keep the stored value when changed at the end
def delay_timer(modifier='*', alternative=1):
    delay = 0.1
    if delay > 0.00001:
        if modifier == '/':
            delay /= alternative
        elif modifier == '*':
            delay *= alternative
        delay -= 0.01
        return time.sleep(delay)
