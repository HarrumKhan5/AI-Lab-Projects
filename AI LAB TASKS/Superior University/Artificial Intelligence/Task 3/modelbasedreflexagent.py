class ModelBasedReflexAgent:
    def __init__(self, temp):
        self.desired_temp = temp
        self.internal_state = None  
    def update_state(self, temp):
        self.internal_state = temp

    def percept(self, temp):
        self.update_state(temp)

    def act(self):
        if self.internal_state > self.desired_temp:
            return "Turn off the heater"
        else:
            return "Turn on the heater"
agent = ModelBasedReflexAgent(22)
agent.percept(16)
print(agent.act())
rooms = {
    "Living Room": 28,
    "Bedroom": 18,
    "Kitchen": 32
}
for room, temp in rooms.items():
    agent.percept(temp)
    print(f"{room}: {temp} ==> {agent.act()}")
