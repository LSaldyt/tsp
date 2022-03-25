class FunctionMinimization:
    def __init__(self, f=lambda x : x**2):
        self.f = f

    def neighbor(s, settings, T):
        return s + settings.rng.normal(loc=0, scale=np.abs(T)) # Random walk

    def initial(rng):
        return rng.random() * 20. - 10. # -10., 10.

    def cost(s):
        return f(s)
