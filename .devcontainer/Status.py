import time

class CookieClicker:
    """
    A class to represent the state of a Cookie Clicker game.
    """
    def __init__(self):
        # Core currency
        self.cookies = 0

        # Item counts
        self.cursors = 0
        self.grandmas = 0
        self.farms = 0

        # Item costs (can be made to increase dynamically)
        self.cursor_cost = 15
        self.grandma_cost = 100
        self.farm_cost = 1100

        # Cookies per second (CPS) for each item
        self.cursor_cps = 0.1
        self.grandma_cps = 1
        self.farm_cps = 8
        
        # Total CPS
        self.cps = 0.0

    def click_cookie(self):
        """Increments cookies by 1 for each manual click."""
        self.cookies += 1
        print("Click! You have {:.1f} cookies.".format(self.cookies))

    def update_cps(self):
        """Recalculates the total cookies per second (CPS)."""
        self.cps = (self.cursors * self.cursor_cps) + \
                   (self.grandmas * self.grandma_cps) + \
                   (self.farms * self.farm_cps)

    def buy_item(self, item_name):
        """Buys an item if the player has enough cookies."""
        item_name = item_name.lower()
        
        if item_name == 'cursor':
            if self.cookies >= self.cursor_cost:
                self.cookies -= self.cursor_cost
                self.cursors += 1
                self.cursor_cost = int(self.cursor_cost * 1.15) # Increase cost
                print(f"You bought a cursor! You now have {self.cursors}.")
            else:
                print("Not enough cookies for a cursor!")
        
        elif item_name == 'grandma':
            if self.cookies >= self.grandma_cost:
                self.cookies -= self.grandma_cost
                self.grandmas += 1
                self.grandma_cost = int(self.grandma_cost * 1.15)
                print(f"You bought a grandma! You now have {self.grandmas}.")
            else:
                print("Not enough cookies for a grandma!")
        
        elif item_name == 'farm':
            if self.cookies >= self.farm_cost:
                self.cookies -= self.farm_cost
                self.farms += 1
                self.farm_cost = int(self.farm_cost * 1.15)
                print(f"You bought a farm! You now have {self.farms}.")
            else:
                print("Not enough cookies for a farm!")
        
        else:
            print("Invalid item name.")
            
        self.update_cps() # Update CPS after any purchase

    def get_status(self):
        """Prints the current game status."""
        print("\n--- GAME STATUS ---")
        print(f"🍪 Cookies: {self.cookies:.1f}")
        print(f"📈 Cookies Per Second (CPS): {self.cps:.1f}")
        print("\n--- UPGRADES ---")
        print(f"👆 Cursors: {self.cursors} (Cost: {self.cursor_cost})")
        print(f"👵 Grandmas: {self.grandmas} (Cost: {self.grandma_cost})")
        print(f"🌾 Farms: {self.farms} (Cost: {self.farm_cost})")
        print("-------------------\n")

# --- Example Usage ---
if __name__ == "__main__":
    # Create a new game instance
    game = CookieClicker()

    # Simulate some actions
    for _ in range(20):
        game.click_cookie()

    time.sleep(1)
    game.buy_item('cursor')
    time.sleep(1)

    # Show the status
    game.get_status()
    
    # Simulate more clicks to afford a grandma
    for _ in range(100):
        game.click_cookie()
        
    time.sleep(1)
    game.buy_item('grandma')
    time.sleep(1)
    
    # Show the final status
    game.get_status()
