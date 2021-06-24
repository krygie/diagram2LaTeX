from block_library import *


class Schematic:
    inputs = []
    outputs = []
    helpers = []
    blocks = []
    latex_data = []

    def __init__(self, file_name='generated_results.tex'):
        if file_name[-4:].lower() != '.tex':
            if '.' not in file_name:
                file_name += '.tex'
            else:
                # TODO: Flush out argument checks
                raise Exception('Filename is incorrect.')
        self.file_name = file_name

    def add_input(self, input_name):
        # TODO: Check for good arguments
        self.inputs.append(input_name)

    def add_output(self, output_name):
        # TODO: Check for good arguments
        self.outputs.append(output_name)

    def add_helper(self, helper_name):
        # TODO: Check for good arguments
        self.helpers.append(helper_name)

    def add_divide(self, param, param1, param2):
        pass

    def add_gain(self, _input, gain, _output):
        self.blocks.append(Gain(_input, gain, _output))

    def generate_latex(self):
        self.latex_data = [r'\documentclass{article}'+'\n',
                           r'\usepackage{amsmath}'+'\n',
                           r'\begin{document}'+'\n'
                           ]

        for block in self.blocks:
            new_string = block.get_equation()
            self.latex_data.append('\n')
            self.latex_data.extend(new_string)

        self.latex_data.append('\n')
        self.latex_data.append(r'\end{document}]')

        with open(self.file_name, 'w') as out_file:
            out_file.writelines(self.latex_data)
        print('LateX file generated! :)')
