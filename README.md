# Programming vacancies compare

This program searches for vacancies on websites [hh.ru](https://hh.ru/) and [superjob.ru](https://www.superjob.ru/) and outputs the average salary for each of the popular programming languages.

### How to install

Register [here](https://api.superjob.ru/register) and copy the Secret key.
Create a file .env with content.
```
SUPERJOB_KEY=[secret_key]
```
Paste your secret key instead of [secret_key].

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Example of running

```
main.py
```

### Example of output 

```
┌HeadHunter Moscow──────────────┬─────────────────────┬─────────┬────────────────┐
│ language    │ vacancies found │ vacancies processed │ skipped │ average salary │
├─────────────┼─────────────────┼─────────────────────┼─────────┼────────────────┤
│ JavaScript  │ 2312            │ 728                 │ 1272    │ 147189         │
│ Java        │ 1945            │ 432                 │ 1513    │ 189731         │
│ python      │ 1643            │ 360                 │ 1283    │ 168003         │
│ ruby        │ 172             │ 53                  │ 119     │ 193150         │
│ PHP         │ 1057            │ 479                 │ 578     │ 139910         │
│ c++         │ 131             │ 55                  │ 76      │ 143031         │
│ c#          │ 981             │ 282                 │ 699     │ 162091         │
│ c           │ 242             │ 110                 │ 132     │ 147956         │
│ go          │ 491             │ 117                 │ 374     │ 197893         │
│ Objective-C │ 190             │ 48                  │ 142     │ 205233         │
│ Scala       │ 189             │ 33                  │ 156     │ 237318         │
│ Swift       │ 348             │ 93                  │ 255     │ 194687         │
│ TypeScript  │ 595             │ 170                 │ 425     │ 183648         │
└─────────────┴─────────────────┴─────────────────────┴─────────┴────────────────┘
┌SuperJob Moscow────────────────┬─────────────────────┬─────────┬────────────────┐
│ language    │ vacancies found │ vacancies processed │ skipped │ average salary │
├─────────────┼─────────────────┼─────────────────────┼─────────┼────────────────┤
│ JavaScript  │ 11              │ 5                   │ 6       │ 47000          │
│ Java        │ 14              │ 4                   │ 10      │ 37291          │
│ python      │ 5               │ 3                   │ 2       │ 91666          │
│ ruby        │ 3               │ 1                   │ 2       │ 235000         │
│ PHP         │ 26              │ 8                   │ 18      │ 14687          │
│ c++         │ 14              │ 3                   │ 11      │ 60000          │
│ c#          │ 9               │ 3                   │ 6       │ 33333          │
│ c           │ 1               │ 1                   │ 0       │ 180000         │
│ go          │ 3               │ 1                   │ 2       │ 190000         │
│ Objective-C │ 0               │ 0                   │ 0       │ 0              │
│ Scala       │ 0               │ 0                   │ 0       │ 0              │
│ Swift       │ 0               │ 0                   │ 0       │ 0              │
│ TypeScript  │ 1               │ 1                   │ 0       │ 197500         │
└─────────────┴─────────────────┴─────────────────────┴─────────┴────────────────┘
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
