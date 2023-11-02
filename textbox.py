import pygame 

class TextBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, font):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))  # fill with black
        self.rect = self.image.get_rect(topleft=(x, y))
        self.font = font
        self.text_lines = [""]  # Initialize with one empty line
        self.input_active = False  # To check if the text box is active for input

    def render_text(self):
        self.image.fill((0, 0, 0))  # Clear previous text
        y_offset = 10
        for line in self.text_lines:
            text_surface = self.font.render(
                line, True, (255, 255, 255))  # Render text in white
            # Adjust the position as needed
            self.image.blit(text_surface, (10, y_offset))
            # Increase y_offset based on line height
            y_offset += self.font.size(line)[1]

    def add_text(self, new_text):
        # This is a simplified example; you might want to handle line breaks, text overflow, etc.
        self.text_lines[-1] += new_text  # Append new_text to the last line
        self.render_text()

    def handle_event(self, event):
        if self.input_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.add_text("")  # Add new empty line on Enter
                elif event.key == pygame.K_BACKSPACE:
                    if self.text_lines[-1]:  # If there is text in the last line
                        # Remove last character
                        self.text_lines[-1] = self.text_lines[-1][:-1]
                    elif len(self.text_lines) > 1:  # If there are multiple lines
                        self.text_lines.pop()  # Remove the last empty line
                else:
                    # Add the character to the last line
                    self.text_lines[-1] += event.unicode
                self.render_text()

    def set_input_active(self, active):
        self.input_active = active

    def get_user_input(self):
        user_input = ""
        while self.input_active:  # While input is active
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.input_active = False  # Deactivate input on Enter
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]  # Remove last character
                    else:
                        user_input += event.unicode  # Add character to input
        return user_input
