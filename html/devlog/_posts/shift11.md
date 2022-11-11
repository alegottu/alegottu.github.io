---
file: shift11
title: Knowing Your Game
date: 5/23/20
excerpt: 
---
After coming back to work on my project with a fresh mind, I realized that I had over engineered the mechanics concerning collision and allowing the player to push around objects. I replaced the need for two colliders on each side of the player by simply placing one on the front of the player, and of course having it match the side that the player is currently moving towards. With this done, I could also use the direction of the player's input to affect the direction that the object which the player pushes should go, rather than handling this separately for two different colliders. 

Speaking of removing extraneous code and utility, I'm also looking into optimizing the lists which keep track of the objects currently colliding with the player. Having lists for both separate sides of the player (to interact differently with the blunt and pointed end of the pin) and a combined list for all collisions only complicates maintaining the two of them. Optimizing this currently isn't my priority, as there quite literally isn't a need for the latter list yet, but I'm leaving a note for myself here that if there ever is, to simply search between both lists, or to devise a way to guarantee when you only need to look in one, such as using the already implemented raycasts to know what side of the player is more important to know about colliding objects. Sometimes, it's better to make educated assumptions about your data rather than chase your own tail accounting for every possible and often unfeasible situation.