from abc import ABC, abstractmethod


class Block(ABC):
    @abstractmethod
    def get_equation(self):
        pass


class Gain(Block):
    result_string = [r'\begin{equation*}'+'\n']

    def __init__(self, _input, gain_value, _output):
        self.input = _input.replace('_', r'\_')
        self.gain_value = gain_value
        self.output = _output.replace('_', r'\_')

    def get_equation(self):
        self.result_string.append('\t' + self.output + ' = ' + str(self.gain_value) + '*' + self.input + '\n')
        self.result_string.append(r'\end{equation*}'+'\n')

        return self.result_string
