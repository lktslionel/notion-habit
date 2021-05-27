# notion-habit
Habit tracker backed by Notion API

## Install

```sh
pip install notion-habit
```

## Usage 


```sh
notion-habit help
```

## Commands

### init
Intialize the notion database to track your habits

```sh
notion-habit init --api-key "xxxxxxxxxxxx" --database-id "xxxxx-xxxxx-xxxx-xxxxx"
```

Credentials will be save to `$HOME/.notion-habit/config`



<!-- ### track
Add a new habit to track

```sh
notion-habit track --habit "Exercise at 3am" --category "Health"
#=> New habit[xxxxxx] added with id[00000]
``` -->

### list

List all register habits to track with their ids

```sh
notion-habit list --property-name "xyz"
#=> id: 00000, habit: xxxxxx
#=> id: 00000, habit: xxxxxx
#=> id: 00000, habit: xxxxxx
#=> id: 00000, habit: xxxxxx
```

### done
Mark an habit as done for a given date. If no date is given, it should default to the current date.

```sh
notion-habit done --habit-ids  [<HABIT_ID>,...] --date <DATE>
```

