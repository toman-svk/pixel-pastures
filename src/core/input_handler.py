import pygame
import os
from typing import List
from src.entities.player import Player
from src.world.layering import Structure
from src.ui.popup import PopupManager
from src.ui.hud import Hud

moveKeysUp = [pygame.K_UP, pygame.K_w]
moveKeysDown = [pygame.K_DOWN, pygame.K_s]
moveKeysLeft =  [pygame.K_LEFT, pygame.K_a]
moveKeysRight = [pygame.K_RIGHT, pygame.K_d]
moveKeys = moveKeysUp + moveKeysDown + moveKeysLeft + moveKeysRight
harvestKey = pygame.K_e

class InputHandler:
    def __init__(self, player: Player, structures: List[Structure], popup: PopupManager, hud: Hud):
        self.player = player
        self.structures = structures
        self.popup = popup
        self.actionCooldown = 0
        self.hud = hud
        return
    
    def cooldown(self):
        if self.actionCooldown > 0:
            self.actionCooldown -= 1

    def handle_move(self, keys):
        directions = []
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            collider = pygame.Rect(self.player.rect)
            collider.y -= 5
            isColliding = False
            for s in self.structures:
                if isColliding: break
                if not hasattr(s, 'growthStage'):
                    for point in [collider.topleft, collider.topright]:
                        if s.get_rect().collidepoint(point):
                            isColliding = True
                            break
            if isColliding == False:
                directions.append('up')
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            collider = pygame.Rect(self.player.rect)
            collider.y += 5
            isColliding = False
            for s in self.structures:
                if isColliding: break
                if not hasattr(s, 'growthStage'):
                    for point in [collider.bottomleft, collider.bottomright]:
                        if s.get_rect().collidepoint(point):
                            isColliding = True
                            break
            if isColliding == False:
                directions.append('down')
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            collider = pygame.Rect(self.player.rect)
            collider.x -= 5
            isColliding = False
            for s in self.structures:
                if isColliding: break
                if not hasattr(s, 'growthStage'):
                    for point in [collider.topleft, collider.bottomleft]:
                        if s.get_rect().collidepoint(point):
                            isColliding = True
                            break
            if isColliding == False:
                directions.append('left')
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            collider = pygame.Rect(self.player.rect)
            collider.x += 5
            isColliding = False
            for s in self.structures:
                if isColliding: break
                if not hasattr(s, 'growthStage'):
                    for point in [collider.topright, collider.topright]:
                        if s.get_rect().collidepoint(point):
                            isColliding = True
                            break
            if isColliding == False:
                directions.append('right')
        self.player.move(directions)

    def handle_harvest(self):
        if self.actionCooldown > 0:
            return
        playerCollider = [self.player.rect.topleft, self.player.rect.topright, self.player.rect.bottomleft, self.player.rect.bottomright]
        hasHarvested = False
        for s in self.structures:
            for point in playerCollider:
                if hasattr(s, 'growthStage') and s.get_rect().collidepoint(point) and hasHarvested == False and s.growthStage == 5:
                    score = s.harvest()
                    self.popup.show_popup("Crop harvested!")
                    self.hud.add_score(score) # add crop's score
                    hasHarvested = True
                    break
            if hasHarvested: 
                self.actionCooldown = 20
                break

    def handle_input(self, keys):
        if (keys[harvestKey]):
            self.handle_harvest()
        else:
            if (any(moveKeys[key] for key in keys)):
                self.handle_move(keys)