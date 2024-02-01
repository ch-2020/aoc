
class ReadFileObject:
    def __init__(self) -> None:
        pass

    def get_lines_from_file(self, filepath):
        try:
            with open(filepath) as file:
                lines = file.readlines()
                return True, lines
        except:
            return False, []


