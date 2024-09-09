import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Texas Hold'em")

# Define colors
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)

# Load card images (you'll need to download a card sprite sheet or individual card images)
# For simplicity, I'll assume that card images are named as 'AS.png', '2H.png', etc.
# You can store these images in a folder named 'cards'
CARD_WIDTH, CARD_HEIGHT = 71, 96  # Standard card size (adjust if necessary)

# Create the deck
SUITS = ['H', 'D', 'C', 'S']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def load_card_images():
    card_images = {}
    for suit in SUITS:
        for rank in RANKS:
            card = rank + suit
            image = pygame.image.load(f'cards/{card}.png')
            image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
            card_images[card] = image
    return card_images

card_images = load_card_images()

# Create deck
def create_deck():
    deck = [rank + suit for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    return deck

# Deal cards
def deal_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]
    for _ in range(2):  # Deal 2 cards per player
        for hand in hands:
            hand.append(deck.pop())
    return hands

# Draw the cards on the screen
def draw_cards(hands):
    x_offset = 50
    y_offset = HEIGHT - CARD_HEIGHT - 50
    for hand in hands:
        for card in hand:
            win.blit(card_images[card], (x_offset, y_offset))
            x_offset += CARD_WIDTH + 10
        x_offset = 50
        y_offset -= CARD_HEIGHT + 20  # Move to the next row for the next player's hand

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()

    # Create and shuffle the deck
    deck = create_deck()

    # Deal cards to two players
    hands = deal_cards(deck, 2)

    while run:
        clock.tick(60)  # 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fill the background
        win.fill(GREEN)

        # Draw the cards
        draw_cards(hands)

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
