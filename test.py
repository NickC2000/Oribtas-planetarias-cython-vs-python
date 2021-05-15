# Entidad: Universidad Sergio Arboleda
# Integrantes: Nicolás Cifuentes
# Profesor: Jonh Corredor Phd.
# Asignatura: Computación paralela y distribuida
# Tema: Prueba de rendimiento Cython simulador orbitas planetarias

import time
import cy_simulator
import simulator
import matplotlib.pyplot as plt

def run_simulator(simulator):
    AU = (149.6e6 * 1000)
    sun = simulator.Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30

    earth = simulator.Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1 * AU
    earth.vy = 29.783 * 1000

    venus = simulator.Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000

    simulator.loop([sun, earth, venus])


def main():
    start = time.time()
    run_simulator(simulator)
    tiempoPy = time.time() - start

    start = time.time()
    run_simulator(cy_simulator)
    tiempoCy = time.time() - start

    speedUp = round(tiempoPy/tiempoCy, 3)
    print(f"Python time: {tiempoPy} \n")
    print(f"Cython time: {tiempoCy} \n")
    print(f"SpeedUp: {speedUp} \n")
    return tiempoPy, tiempoCy


if __name__ == '__main__':
    tiempoPy, tiempoCy = main()
    tiempos = [tiempoPy,tiempoCy]
    labels = ['Python','Cython']
    plt.barh(labels,tiempos,align='center',alpha=0.5,color=['blue','green'])
    plt.title('Rendimiento Cython vs Python')
    plt.xlabel('Tiempo')
    plt.savefig('rendimiento.png')
    plt.show()