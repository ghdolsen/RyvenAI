from NENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget()                    <- access to main widget


class Print_Node(Node):
    def __init__(self, params):
        super(Print_Node, self).__init__(params)

        self.special_actions['print something 1'] = {'method': self.print_something,
                                                     'data': 'hello!!'}
        self.special_actions['print something 2'] = {'method': self.print_something,
                                                     'data': 'HELLOO!?!?!?'}


    def update_event(self, input_called=-1):
        if input_called == 0:
            print(self.input(1))
            self.exec_output(0)

    def print_something(self, data):
        print(data)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass
        # ...


    def remove_event(self):
        pass