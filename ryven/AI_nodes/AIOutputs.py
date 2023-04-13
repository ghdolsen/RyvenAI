from ryven.NENV import *

class AiHtmlOutput(Node):
    title = 'AI HTML Output'
    init_inputs = [
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
    AiHtmlOutput,
]