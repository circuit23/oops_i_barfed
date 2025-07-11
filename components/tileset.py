import tcod


def tile_set():
    """
    Set up the tile set, and whether to use sprites.
    """
    tileset = tcod.tileset.load_tilesheet(
        "Zilk_16x16.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )
    # follow the format of these old codepoint assignments to use new ones
    # tileset.remap(0x100000, 2, 5)  # Assign codepoint 0x100000 to a character sprite
    # tileset.remap(0x100001, 3, 5)  # Orcs
    # tileset.remap(0x100002, 4, 5)  # Trolls
    # tileset.remap(0x100003, 5, 5)  # Scrolls
    # tileset.remap(0x100004, 6, 5)  # Potions
    # tileset.remap(0x100005, 7, 5)  # sword
    # tileset.remap(0x100008, 10, 5)  # dagger
    # tileset.remap(0x100006, 8, 5)  # armor
    # tileset.remap(0x100007, 9, 5)  # downstairs
    # tileset.remap(0x100009, 0, 5)  # wall
    # tileset.remap(0x100010, 1, 5)  # floor

    return tileset