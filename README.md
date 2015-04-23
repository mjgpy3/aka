# aka
A new kind of alias system for linux

## To use

Ensure you have `python` installed, and run the install script
```
. install.sh
```

## Configuring (by example)

If you wanted the command
```
git log
```

to be aliased to
```
afsd g l
```

you could do so with
```
[
  {
    "token": "g",
    "command": "git",
    "branches": [
      {
        "token": "l",
        "command": "log"
      }
    ]
  }
]
```
