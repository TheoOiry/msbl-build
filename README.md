# MSBL-BUILD

A tool to easily retrieve a build from character stats

`build` -> find the equipments part for stats

`stats` -> retrieve the stats with equipments parts

`best` -> find the best build with stats type

## Example

### Build
```
py build.py rosalina 11/8/20/5/19
5633
```

### Stats
```
py stats.py rosalina 5633
11/8/20/5/19
```

### Best

Check all possible builds to find the builds with the best
stats in the defined stats type.

The order is important, in this example it is to find all 
the builds where the technic is greater than or equal 
to the shoot stat.

Then it takes the builds with the highest sum of the specified
stats. (can return several builds if several builds have the 
same sum)

```
py best.py rosalina technic shoot
(5653): 11/8/18/5/21
```
