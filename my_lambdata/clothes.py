class Polo():
    def __init__(self, style, size, color):
        self.style = style
        self.size = size
        self.color = color
        pass
    def pop_collar(self):
        print("popping this collar")
    
 #   def __init__():

if __name__ == "__main__":
    polo = Polo(style = "sheek", size = "L", color = "red")
    print(type(polo))
    print(polo.size)
    print(polo.color)
    print(polo.style)
    print(polo.pop_collar())

    polo2 = Polo(style = "sheek", size = "S", color = "green")
    print(type(polo2))
    print(polo2.size)
    print(polo2.color)
    print(polo2.style)
    print(polo2.pop_collar())