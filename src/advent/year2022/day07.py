from advent import read_input


class TreeNode:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent: TreeNode = parent
        self.size = size

    def __repr__(self):
        return f'{self.size} {self.name}'


class Dir(TreeNode):
    def __init__(self, name, parent, size):
        super().__init__(name, parent, size)
        self.content: list[TreeNode] = []

    def get(self, name):
        for item in self.content:
            if item.name == name:
                return item

    def find_file(self, name):
        subdirs = []
        for item in self.content:
            if item.name == name:
                return item
            if isinstance(item, Dir):
                subdirs.append(item)
        return any([subdir.find_file(name) for subdir in subdirs])


class FS:
    def __init__(self, cmds):
        self.root = Dir('/', parent=None, size=0)
        self.path: str = 'None'
        self.cmds = self.parse_commands(cmds)
        self.current_cmd = 0

    def process_command(self, cmd: tuple[str, list[str]]):
        cmd_input, output = cmd
        if cmd_input.startswith('cd '):
            self.run_cd(cmd_input)
        elif cmd_input.startswith('ls'):
            self.run_ls(cmd_input, output)
        return

    def has_commands(self):
        return self.current_cmd < len(self.cmds)

    def get_command(self):
        cmd = self.cmds[self.current_cmd]
        self.current_cmd += 1
        return cmd

    def run(self):
        while self.has_commands():
            self.process_command(self.get_command())

    def parse_commands(self, cmds: list[str]):
        commands = []
        for cmd in cmds:
            if cmd.startswith('$'):
                commands.append((cmd.strip().lstrip('$ '), []))
            else:
                commands[-1][1].append(cmd.strip())
        return commands

    def run_cd(self, cmd: str):
        cd, path = cmd.split()
        if path.startswith('/'):
            self.path = path
        elif path == '..':
            self.path = '/'.join(self.path.split('/')[:-1])
        else:
            self.path = self.path.rstrip('/') + f'/{path}'

    def run_ls(self, cmd_input, output):
        if cmd_input != 'ls':
            raise ValueError(f'Unknown command {cmd_input}, expect ls')
        for file in output:
            self.add_file_from_ls(file)

    def add_file_from_ls(self, file):
        size, filename = file.split()
        if size.isdigit():
            new_node = TreeNode(filename, self.current_node, int(size))
        else:
            new_node = Dir(filename, self.current_node, 0)
        self.current_node.content.append(
            new_node
        )

    def get_node(self, path) -> Dir:
        current_node = self.root
        for segment in path.split('/'):
            if not segment:
                continue
            current_node = current_node.get(segment)
        return current_node

    @property
    def current_node(self) -> Dir:
        return self.get_node(self.path)

    def find_file(self, name):
        return self.root.find_file(name)


def traverse(root: Dir, dirs, cond=None):
    size = 0
    for file in root.content:
        if isinstance(file, Dir):
            size += traverse(file, dirs, cond=cond)
        else:
            size += file.size
    if cond(size):
        dirs.append(root)
    root.size = size
    return size


def has_duplicates(root: Dir):
    filenames = set()
    for file in root.content:
        filenames.add(file.name)
        if isinstance(file, Dir):
            has_duplicates(file)
    if len(filenames) < len(root.content):
        print(f'duplicates found in {root.name}')
    return


lines = read_input('day07.txt')
fs = FS(lines)
fs.run()

dirs_below_100k = []
traverse(fs.root, dirs_below_100k, cond=lambda x: x < 100000)
# part 1
print(sum(map(lambda x: x.size, dirs_below_100k)))

# part 2
size_needed = fs.root.size - 40000000
candidates_to_delete = []
traverse(fs.root, candidates_to_delete, cond=lambda x: x >= size_needed)
print(min(candidates_to_delete, key=lambda x: x.size))
