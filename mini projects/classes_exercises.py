class Pet:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving..."


dog = Pet('Peca')
print(dog.move())


class Tag:
    # 3. Write a simple Tag class to encapsulate HTML tags, for example
    def __init__(self, paragraph):
        self.paragraph = paragraph

    def render(self):
        return f"<p>{self.paragraph}</p>"


my_tag = Tag("I am a paragraph")
print(my_tag.render())

# Using inheritance, create subclasses for Paragraph (tag is as above) and
# ListItem (tag looks like <li>I am a list item</li>)


class Paragraph(Tag):
    def __init__(self, paragraph, my_item):
        super().__init__(paragraph)
        self.my_item = my_item

    def list_item(self):
        return f"<li>{self.my_item}</li>"


my_text = Paragraph("Article's Title", "Text in the article")
print("\n", my_text.paragraph, "\n", my_text.render(), "\n", my_text.my_item, "\n", my_text.list_item())


# 5. Create an abstract base class, Shape, with a single abstract method, draw.
# Implement two child classes, Elipse and Rectangle, that override the draw method. For the implementation,
# you can substitute a stub (a simple string printout saying what the class is drawing).


class Shape:
    def __init__(self):
        pass

    def draw(self):
        return 'draw has been called'


print("\n")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        for i in range(self.height):
            print("*" * self.width)


class Ellipse(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def draw(self):
        pass


my_polygon = Rectangle(8, 5)
my_polygon.draw()

my_polygon_2 = Shape()
print(my_polygon_2.draw())

