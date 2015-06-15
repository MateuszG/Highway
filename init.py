""" Definie what engine need """


def start_engine(pygame):
    # Initialize the game engine
    pygame.init()

    # Get all possible width and height of the screen
    print("Possible width and height of the screen: ", end="")
    print(pygame.display.list_modes())

    # Set the width and height of the screen
    screen_size = (pygame.display.list_modes())
    print("Engine will use: ", screen_size[0])
    screen = pygame.display.set_mode(screen_size[0], pygame.FULLSCREEN)

    # Get clear values width and height of the screen
    used_screen_sizes = screen_size[0]
    screen_width = int(used_screen_sizes[0])
    screen_height = int(used_screen_sizes[1])

    print("Height =", screen_height)
    print("Width =", screen_width)

    # Loop until the user clicks the close button.
    DONE = False

    # To small screen
    if ((screen_height < 480) and (screen_width < 640)):
        DONE = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Select the font to use. Default font, 25 pt size.
    font = pygame.font.Font(None, 25)
    # font = pygame.font.Font("C:/Windows/Fonts/ARIAL.TTF", 25)

    print("<< Game started >>")
    return (font, clock, screen, screen_width, screen_height, DONE)
