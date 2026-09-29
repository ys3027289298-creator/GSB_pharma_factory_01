"""制药厂核心逻辑：原料、反应釜、洁净和质检。"""

import json


def new_game():
    return {"batches": {}, "reactor_load": 0, "reactor_capacity": 2, "material": 100, "safety": 100, "batch_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["batch_id"] += 1
    return state


def feed(state, batch_id, amount):
    state["batches"][batch_id] = {"amount": amount, "defect": False}
    state["material"] -= amount
    return True


def react(state, batch_id):
    state["reactor_load"] += 1
    return True


def check_temp(state, temp):
    if temp < 30:
        return "over"
    return "ok"


def cancel(state, batch_id):
    return True


def inspect(state, batch_id):
    if state["batches"][batch_id].get("defect"):
        return False
    return True


def produce(state, amount):
    return True


def pollute(state):
    state["safety"] -= 10
    state["safety"] -= 10
    return state["safety"]


def main():
    print("制药厂 - 命令: feed/react/temp/cancel/inspect/produce/pollute/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
