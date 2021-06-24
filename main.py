from schematic import Schematic


if __name__ == '__main__':
    schematic = Schematic('Out_file')

    schematic.add_input('ABC_input')
    schematic.add_output('XYZ_output')

    schematic.add_gain('ABC_input', '100.0', 'XYZ_output')

    schematic.generate_latex()
