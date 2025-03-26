import time
import functools

def retry(retries=3, delay=2, backoff=2):
    """
    Decorador que adiciona lógica de retry a uma função.

    :param retries: Número máximo de tentativas.
    :param delay: Atraso inicial entre tentativas, em segundos.
    :param backoff: Fator de multiplicação para aumentar o atraso após cada tentativa.
    """
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            exceptions = (Exception,)  # Tipos de exceções que acionam o retry
            current_delay = delay  # Define o atraso inicial
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt < retries - 1:
                        print(f"Tentativa {attempt + 1} falhou: {e}. Tentando novamente em {current_delay} segundos...")
                        time.sleep(current_delay)
                        current_delay *= backoff  # Aumenta o atraso
                    else:
                        raise
        return wrapper
    return decorator_retry

# Exemplo de uso
@retry(retries=5, delay=1, backoff=2)
def unreliable_function():
    import random
    if random.choice([True, False]):
        raise RuntimeError("Erro aleatório ocorreu!")
    return "Sucesso!"

try:
    result = unreliable_function()
    print(result)
except Exception as e:
    print(f"Falha final: {e}")
