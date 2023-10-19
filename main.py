from sypo.population import Population

if __name__ == '__main__':

    p = Population(5, 10)
    p.populate()

    for k in p.population:
        print(f"{k} => {k.decode()}")
