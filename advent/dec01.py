from util import aocio


input = aocio.get_day(1)


elves = input.split("\n\n")

elf_totals = []
for elf in elves:
    elf_total = sum([int(s) for s in elf.split("\n") if len(s) > 0])
    elf_totals += [elf_total]

print(max(elf_totals))


