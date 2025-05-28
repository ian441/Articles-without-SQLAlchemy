#!/usr/bin/env python3
"""Interactive debug console for testing database models"""

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def show_help():
    """Display available commands"""
    print("\n=== Available Commands ===\n")
    print("1. Create and save objects:")
    print("   author = Author('Name').save()")
    print("   magazine = Magazine('Mag Name', 'Category').save()")
    print("   article = Article('Title', author.id, magazine.id).save()\n")
    print("2. Find objects:")
    print("   Author.find_by_name('Name')")
    print("   Magazine.find_by_name('Mag Name')\n")
    print("3. View relationships:")
    print("   author.articles()")
    print("   author.magazines()")
    print("   magazine.articles()\n")
    print("Type 'exit()' to quit")

def main():
    print("\n=== Model Debug Console ===")
    print("Type 'show_help()' for commands\n")
    
    # Start interactive console with models pre-imported
    import code
    console = code.InteractiveConsole(locals())
    console.interact(banner="", exitmsg="")

if __name__ == "__main__":
    show_help()
    main()