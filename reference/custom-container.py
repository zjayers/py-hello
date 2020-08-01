class TagCloud:
    def __init__(self):
        self.__tags = {}

    def __getitem__(self, item):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, key, value):
        self.__tags[tag.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def add(self, tag: str):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

cloud = TagCloud()
cloud.add('Python')
cloud.add('python')
cloud.add('Python 3')

len(cloud)

cloud["python"] = 10

for tag in cloud:
    print(tag)