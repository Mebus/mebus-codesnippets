# Taskwarrior

## How to end a recurring task?

 * `task recurring`
 * Pick an `<id>`.
 * `task <id> modify until:now`

## Create a recurring task

```
task add "Staubsaugen" project:wohnen  recur:biweekly due:eow until:2030-01-01
```

## Weblinks

 * https://taskwarrior.org/docs/