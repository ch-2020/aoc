class DrawCoordMap:
    def __init__(self, coords: list):
        self.coords = coords
    
    def draw_map(self, maxwidth = 9999999):
        minx = min([ele for ele in zip(*self.coords)][0])
        maxx = max([ele for ele in zip(*self.coords)][0])
        miny = min([ele for ele in zip(*self.coords)][1])
        maxy = max([ele for ele in zip(*self.coords)][1])

        lenx = min(maxx-minx, maxwidth)

        lines = []
        lines.append(u'\u2517' + u'\u2501'*(lenx+1) + u'\u251B')
        for y in range(miny, maxy+1):
            show = u'\u2503'
            for x in range(minx, minx + lenx +1):
                if (x, y) in self.coords:
                    show += "#"
                else:
                    show += " "
            show += u'\u2503'
            lines.append(show)
        lines.append(u'\u250F' + u'\u2501'*(lenx+1) + u'\u2513')

        for l in lines[::-1]:
            print(l)

if __name__ == "__main__":
    map = DrawCoordMap([(0,0), (15,30), (2, 49)])
    map.draw_map()