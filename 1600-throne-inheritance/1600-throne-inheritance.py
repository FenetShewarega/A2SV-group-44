class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.kingdom = {kingName: []}
        self.dead = set()
        self.c = 0

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.kingdom:
            self.kingdom[parentName] = [childName]
        else:
            self.kingdom[parentName].append(childName)
        self.c += 1

    def death(self, name: str) -> None:
        self.dead.add(name)
        self.c -= 1

    def getInheritanceOrder(self) -> List[str]:
        inh = []

        def dfs(parent):
            if parent not in self.dead:
                inh.append(parent)
            if parent in self.kingdom:
                for child in self.kingdom[parent]:
                    dfs(child)

        dfs(self.kingName)
        return inh