import main as app
import threading
import time

app.create("sara", 23)
app.create("alia", 45, 50)
app.read("sara")
app.read("alia")
time.sleep(5)
# After 5 seconds
app.read("sara")
app.read("alia")
app.delete("sara")
app.delete("alia")

a = threading.Thread(target=app.create, args=("sian", 55, 10))
a.start()
a.join(10)
app.read("santa")
app.read("sian")

b = threading.Thread(target=app.create, args=("santa", 85, 100))
b.start()
b.join(0)
app.read("santa")
app.read("sian")
