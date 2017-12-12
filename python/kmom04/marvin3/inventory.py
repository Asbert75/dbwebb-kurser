#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains all of the inventory functions for Marvin (Dalek).
"""

def writeToInv():
    """
    Loads inventory for writing
    """
    inv = open("inv.data", "w")
    return inv

def readFromInv():
    """
    Loads inventory for reading
    """
    inv = open("inv.data", "r")
    return inv

def getItemList():
    """
    Checks if bags are full.
    """
    inv = readFromInv()

    items = list()
    for line in inv:
        line = line.rstrip()
        line = line.lower()
        items.append(line)

    return items


def display():
    """
    Displays Marvins current inventory.
    """
    inv = getItemList()
    invSize = len(inv)

    if invSize == 0:
        print("Dalek says: There are currently no items in my inventory.")
    else:
        print("Dalek says: These are the current items in my inventory:")
        for line in inv:
            print(line)


def pickItem(item):
    """
    Picks up a flower and puts it in Marvins inventory.
    """
    items = getItemList()
    inventorySize = len(items)

    if inventorySize <= 3:
        inv = writeToInv()
        items.append(item)

        for i in range(len(items)):
            inv.write(items[i]+"\n")
        print("Dalek put a(n)", item, "in his inventory.")
    else:
        print("Dalek says: I can't do that, my inventory is full.")


def dropItem(item):
    """
    Drops a flower (if there is one) from Marvins inventory.
    """
    items = getItemList()
    inventorySize = len(items)

    if inventorySize > 0:
        inv = writeToInv()
        deleted = False

        for i in range(len(items)):
            print(item, items[i])
            if item in items[i]:
                print("Deleted", item)
                items.pop(i)
                deleted = True

        for i in range(len(items)):
            inv.write(items[i]+"\n")

        if deleted:
            print(item, "was dropped from the inventory.")
        else:
            print(item, "could not be found in the inventory.")

def drop():
    """
    Dalek abandons his inventory, cleaning it out.
    """
    inv = writeToInv()
    inv.truncate()
    print("Inventory has been cleaned out.")
