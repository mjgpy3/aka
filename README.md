# aka
A new kind of alias system for linux

## To use

Ensure you have `python` installed, and run the install script
```
. install.sh
```

Warning: installing this software will install aliases for all combinations of the characters `a`, `s`, `d`, and `f`

## Configuring (by example)

### Simple alias

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

### Exploding params

If you wanted the command
```
for i in PARAMS; do git push origin ":$i"; done
```
(where params is all parameters passed to the command)

to be aliased to
```
afsd gitdr
```

you could do so with
```
[
  {
    "token": "gitdr",
    "command": "for i in PARAMS_GO_HERE; do git push origin \":$i\"; done",
    "splatParamsInto": "PARAMS_GO_HERE"
  }
]
```
