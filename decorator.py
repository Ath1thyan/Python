txt = "t3"
phrase = {
    "buy msg" : {
        "t1": "buy samosa",
        "t2": "buy tea",
        "t3":  "buy coffee",
        "t4": "buy milk"
    }
}

def hi(call):
    global txt
    def hell(*args, **kwargs):
        msg = call(*args, **kwargs)
        return phrase[msg][txt]
    return hell

@hi
def say():
    msg = "buy msg"
    return msg
print(say())