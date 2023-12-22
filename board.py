import json
from item import *

# Board class
class Board:

    # List of items on the board
    items = []

    # Path to save at
    filepath = ""

    # Display name (in the window and stuff)
    display_name = "New Board"

    # Constructor for loading an existing board
    def __init__(self, filepath = ""):
        # If the filepath is not provided, just quit and use our default values
        if not filepath:
            return
        
        # Attempt to open and read the board file
        contents = ""
        try:
            # Open the file
            file = open(filepath)
            contents = file.read()
            file.close()

            # Say we are from a file
            self.filepath = filepath

        # Otherwise raise an exception to be handled by whatever is using this class
        except:
            raise BoardLoadingException("Could not read the board at " + filepath)
        
        # Convert the contents to JSON
        board_obj = json.loads(contents)

        # Extract values
        self.display_name = board_obj.title

        # Items
        for item in board_obj.items:

            # Convert the item object into an item
            match item.type:
                case "text":
                    self.items.append(Text(item))
                case "todo":
                    self.items.append(Todo(item))
                case "link":
                    self.items.append(Link(item))
                case "board_link":
                    self.items.append(BoardLink(item))
                case "item":
                    raise BoardLoadingException(f"Invalid item type '{item.type}'.")
                case _:
                    raise BoardLoadingException(f"Invalid item type '{item.type}'.")
        
class BoardLoadingException(Exception):
    pass
