from ryven.NENV import *

class AITextPrompt(Node):
    title = 'Text Prompt'
    init_inputs = [
    NodeInputBP(
            dtype=dtypes.String("Type your prompt here"),
            label='In'
        ),
    ]
    init_outputs = [
        NodeOutputBP(
            label='Out'
        ),
    ]

    def update_event(self, inp=-1):
        print(self.input(0))

class AIImagePrompt(Node):
    title = 'Image Prompt'
    init_inputs = [
    NodeInputBP(
            dtype=dtypes.String("File Path"),
            label='In'
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
    AITextPrompt,
    AIImagePrompt,
]