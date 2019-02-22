import ddd_message

ddd_message.send_message.send("hello")

result = ddd_message.receive_message.receive()
print(result)