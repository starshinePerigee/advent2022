import pytest

from util import aocio


class File:
    draw_level = 0

    def __init__(self, name: str, size: int, parent: 'Directory' = None):
        self.name = name
        self.size = size
        self.parent = parent
        self.file = True

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<File {self.name}>"

    def __len__(self):
        return self.size

    def __iadd__(self, other: 'File'):
        raise NotImplementedError(f"Tried to call iadd on {self}")

    def summary(self) -> str:
        return f"{self.name} (file, size={self.size})"

    def print_tree(self) -> None:
        print(f"{'  '*self.draw_level} - {self.summary()}")


class Directory(File):
    def __init__(self, name: str, parent: 'Directory' = None):
        super().__init__(name, 0, parent)
        self.file = False
        self.files = []

    def __len__(self):
        return sum([len(x) for x in self.files])

    def __repr__(self):
        return f"<Directory {self.name}>"

    def __iadd__(self, other: File):
        self.files += [other]
        return self

    def summary(self) -> str:
        return f"{self.name} (dir)"

    def print_tree(self) -> None:
        print(f"{'  '*self.draw_level} - {self.summary()}")
        File.draw_level += 1
        for file in self.files:
            file.print_tree()
        File.draw_level -= 1

    def get_child(self, name: str) -> File:
        for file in self.files:
            if name == file.name:
                return file
        raise RuntimeError(f"File '{name}' not found in {self}")


class FileSystem:
    def __init__(self):
        self.root = Directory("")
        self.all_files = [self.root]
        self.cwd = self.root
        self._line = 0

    def parse_command(self, command: str) -> None:
        self._line += 1
        command = command.strip()
        if "$ cd" in command:
            # change directory
            if command[-2:] == "..":
                self.cwd = self.cwd.parent
                if self.cwd is None:
                    raise RuntimeError(f"Escape above root on line {self._line}: {command}")
            elif command[-1:] == "/":
                self.cwd = self.root
            else:
                self.cwd = self.cwd.get_child(command[5:])
        elif "$ ls" in command:
            pass
        else:
            size, name = command.split(" ", maxsplit=1)
            if size == "dir":
                new_dir = Directory(name, self.cwd)
                self.cwd += new_dir
                self.all_files += [new_dir]
            else:
                new_file = File(name, int(size), self.cwd)
                self.cwd += new_file
                self.all_files += [new_file]

    def cwd_str(self) -> str:
        return "/" + "/".join([str(x) for x in self.cwd[1:]])


@pytest.fixture
def fs():
    return FileSystem()

def test_root_dir(fs):
    assert len(fs.cwd) == 0
    assert fs.cwd.name == ""


def test_add_file(fs):
    fs.parse_command("14848514 b.txt")
    assert len(fs.root) == 14848514
    assert len(fs.root.files) == 1


def test_add_move_dir(fs):
    fs.parse_command("dir a")
    fs.parse_command("$ cd a")
    fs.parse_command("123 b.txt")
    assert fs.cwd.name == "a"
    assert len(fs.cwd) == 123
    assert len(fs.root) == 123
    assert fs.cwd is not fs.root
    print("")
    fs.root.print_tree()


def test_part_one(fs):
    commands = aocio.get_day(7, True)
    for command in commands.splitlines():
        fs.parse_command(command)
    fs.root.print_tree()
    assert len(fs.root) == 48381165
    assert len(fs.root.get_child("d")) == 24933642

    total_under = 0
    for file in fs.all_files:
        if not file.file:
            file_len = len(file)
            if file_len <= 100000:
                total_under += file_len
    assert total_under == 95437


def test_execute_part_one(fs):
    commands = aocio.get_day(7)
    for command in commands.splitlines():
        fs.parse_command(command)
    fs.root.print_tree()

    total_under = 0
    for file in fs.all_files:
        if not file.file:
            file_len = len(file)
            if file_len <= 100000:
                total_under += file_len
    print("Total under:" + str(total_under))