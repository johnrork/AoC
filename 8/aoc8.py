import read
import copy


functions = {
    'nop': lambda arg, val, ln: (val, ln + 1),
    'jmp': lambda arg, val, ln: (val, ln + arg),
    'acc': lambda arg, val, ln: (val + arg, ln + 1)
}


instructions = []
for line in read.file_into_line_groups('instructions.txt')[0]:
    inst, arg = line.split(' ')
    instructions.append([inst, int(arg)])


def run(instruction_list):
    ln, val = (0, 0)
    visited_lns = set()
    while ln != len(instruction_list):
        if ln in visited_lns:
            return val, False
        visited_lns.add(ln)
        fn, arg = instruction_list[ln]
        val, ln = functions[fn](arg, val, ln)
    return val, True


val, clean = run(instructions)
if not clean:
    print("Part 1:", val)


for i, (inst, _) in enumerate(instructions):
    if inst == 'acc':
        continue

    mod_instructions = copy.deepcopy(instructions)
    mod_instructions[i][0] = 'nop' if inst == 'jmp' else 'jmp'

    val, clean = run(mod_instructions)
    if clean:
        print("Part 2:", val)
        break
