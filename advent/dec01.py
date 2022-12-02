from util import aocio


day_input = aocio.get_day(1)


elves = input.day_input("\n\n")

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
