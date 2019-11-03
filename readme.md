# About Face

## Change Detector

Examines a series of binary dumps to find bytes or words that follow a given sequence of changes.

### Usage

```
python3 change_detector.py --bits 16 --endian little --sequence lgss FileName-*.dmp
```

Where `--sequence` is a series of `l`, `g`, `s`, or `d` to denote if a change between files is less-than, greater-than, the same, or different. There should be number-of-files minus 1 elements in the sequence.

## Decrement Detector

Examines a series of binary dumps to find bytes or words that descend between each dump. This is useful for analyzing RAM dumps when reverse-engineering emulator ROMs (i.e. find the address in memory responsible for lives or health).


### Usage

```
python3 decrement_detector.py --bits 16 --endian little FileName-*.dmp
```

"FileName-*.dmp" is a glob that expands to be a series of of sequentially-named files that are the memory dumps ordered by name oldest to newest. It's important that the naming of the files results in them being sorted correctly (i.e. FileName-00.dmp, FileName-01.dmp, FileName-02.dmp.. FileName-10.dmp.. FileName-20.dmp...)