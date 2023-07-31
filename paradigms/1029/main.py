class Memoize:
    memory = {}
    
    def remember(self, n, r):
        restoration = self.memory.get(n, None)
        if restoration is None:
            self.memory[n] = r
mem = Memoize()

def memoize():
    memory = {}
    
    def function(n):
        print(memory)
        if (v := memory.get(n)) is not None:
            print(f"hit: fib({n}) = {v}")
            return v
        print(v)
        v = fib(n)
        memory[n] = v
        
        return v
    
    return function

def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    fibmem = memoize()
    
    print(fibmem(1))
    print(fibmem(2))
    print(fibmem(20))
    print(fibmem(5))
