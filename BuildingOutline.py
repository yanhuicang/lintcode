
def buildingOutline(self, buildings):
    s = [0, 0, 0]
    result = []
    for build in buildings:
        tmp = copy.deepcopy(result)
        for r in result:
            if build[1] >= r[2]:
                continue

            
