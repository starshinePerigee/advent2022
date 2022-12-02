from util import aocio


day_input = aocio.get_day(1)


elves = day_input.split("\n\n")

elf_totals = []
for i, elf in enumerate(elves):
    elf_total = sum([int(s) for s in elf.split("\n") if len(s) > 0])
    elf_totals += [(elf_total, i)]

sorted_elves = sorted(elf_totals, reverse=True)

total_calories = 0
for i in range(3):
    print(f"{i+1}: {sorted_elves[i]}")
    total_calories += sorted_elves[i][0]

print(total_calories)


# not so cursed oneliner
print(max([[sum(int(s) for s in e.split('\n') if len(s) > 0)] for e in aocio.get_day(1).split('\n\n')]))
