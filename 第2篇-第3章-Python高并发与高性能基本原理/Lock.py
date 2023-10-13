import dis
import threading

m_lock = threading.Lock()

with m_lock:
    a = 1
    a += 1
