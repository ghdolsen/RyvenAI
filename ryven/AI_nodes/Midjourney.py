from ryven.NENV import *

class Midjourney(Node):
    title = 'Midjourney'
    init_inputs = [
        NodeInputBP(
            dtype=dtypes.String("sk-12341234123412341234123412341234123412341234"),
            label='API Key'
        ),
        NodeInputBP(
            dtype=dtypes.Data(),
            label='Image'
        ),
        NodeInputBP(
            dtype=dtypes.String(),
            label='Prompt'
        ),
    ]

    init_outputs = [
        NodeOutputBP(
            label='Out'
        ),
    ]

    def update_event(self, inp=-1):
        print(self.input(0))


nodes = [
    Midjourney,
]