from websocket import create_connection
### checking if a connection can be established

TEST_WSS = "wss://socketsbay.com/wss/v2/2/demo/" ## test wss url

def websocket_test_connection():
    try:
        ws = create_connection(TEST_WSS)
        CONNECT = True
        ws.send("Test")
        SENT = True
        ws.recv()
        RECEIVE = True
        ws.close()
        return [CONNECT, SENT, RECEIVE]
    except Exception:
        return [False, False, False]
