# monki-py
## Simple PyGame about monkey
My **first** game made in *Python*.

It's a pretty simple game. You play as a monkey that is a single sprite.
```
monkey_img = pygame.image.load("assets/sprites/monkey.png")
```

or generating bananas and bombs, it uses the random library and its `random.randint` function.

```
if random.randint(1, banana_interval) == 1:
    banana_x = random.randint(10, WIDTH - 75)
```

I made it for my college classes on the basics of *Python* programming. I'm not really sure what I should put here, so yeah... that's all.