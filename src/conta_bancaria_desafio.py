import threading
import time

saldo_conta = 0
NUM_OPERACOES = 100000
lock_bancario = threading.Lock()

def depositar():
    global saldo_conta
    for _ in range(NUM_OPERACOES):
        with lock_bancario:
            saldo_conta += 1

def sacar():
    global saldo_conta
    for _ in range(NUM_OPERACOES):
        with lock_bancario:
            saldo_conta -= 1

def main():
    global saldo_conta
    print(f" [*] Saldo Inicial: {saldo_conta}")

    t1 = threading.Thread(target=depositar, name="Thread-Caixa-1")
    t2 = threading.Thread(target=depositar, name="Thread-App-2")
    t3 = threading.Thread(target=sacar, name="Thread-Saque-3")

    inicio = time.time()

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    fim = time.time()

    # (100.000 + 100.000) - 100.000 = 100.000
    saldo_esperado = NUM_OPERACOES
    print(f" [*] Saldo Esperado: {saldo_esperado}")
    print(f" [*] Saldo Obtido: {saldo_conta}")
    print(f" [*] Tempo de Execucao: {fim - inicio:.4f} s")

    if saldo_conta != saldo_esperado:
        print("\n [ALERTA] Condicao de Corrida detectada! Houve perda de dados.")
    else:
        print("\n [OK] Resultado integro.")

if __name__ == "__main__":
    main()